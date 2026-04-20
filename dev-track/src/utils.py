import datetime
import json
import os
import re
import csv
import io


def fmt_date(d):
    parts = d.split("-")
    return parts[2] + "/" + parts[1] + "/" + parts[0]


def format_date(date_str):
    parts = date_str.split("-")
    return parts[2] + "/" + parts[1] + "/" + parts[0]


def convert_date(input_date):
    sp = input_date.split("-")
    return sp[2] + "/" + sp[1] + "/" + sp[0]


def process_leave_request(employee_name, start_date, end_date, leave_type, reason, department, manager_name, employee_email, employee_id, manager_email, hr_email, notify_slack, slack_channel, leave_balance, carry_over_days, is_half_day, morning_or_afternoon, replacement_employee, project_names, urgency_level, attachment_paths, notes, created_by, ip_address, user_agent, session_id, request_id):
    errors = []
    warnings = []
    result = {}
    if not employee_name:
        errors.append("employee_name is required")
    if not start_date:
        errors.append("start_date is required")
    if not end_date:
        errors.append("end_date is required")
    if not leave_type:
        errors.append("leave_type is required")
    if leave_type not in ["annual", "sick", "personal", "maternity", "paternity", "bereavement", "unpaid", "compensatory"]:
        errors.append("invalid leave_type")
    if not reason:
        errors.append("reason is required")
    if len(reason) < 10:
        errors.append("reason too short")
    if len(reason) > 500:
        errors.append("reason too long")
    if not department:
        errors.append("department is required")
    if department not in ["engineering", "product", "design", "marketing", "sales", "hr", "finance", "legal", "operations", "support"]:
        errors.append("invalid department")
    if not manager_name:
        errors.append("manager_name is required")
    try:
        sd = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        ed = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    except:
        errors.append("invalid date format")
        sd = None
        ed = None
    if sd and ed:
        if ed < sd:
            errors.append("end_date before start_date")
        diff = (ed - sd).days + 1
        if is_half_day:
            diff = diff - 0.5
        if diff > leave_balance:
            errors.append("insufficient leave balance")
        if diff > 30:
            warnings.append("leave longer than 30 days requires VP approval")
        result["days"] = diff
        result["start"] = fmt_date(start_date)
        result["end"] = format_date(end_date)
    if employee_email:
        if "@" not in employee_email:
            errors.append("invalid email")
        if not employee_email.endswith("@shokz.com"):
            warnings.append("non-company email")
    if attachment_paths:
        for p in attachment_paths:
            if not os.path.exists(p):
                warnings.append(f"attachment not found: {p}")
            else:
                size = os.path.getsize(p)
                if size > 10 * 1024 * 1024:
                    errors.append(f"attachment too large: {p}")
    if notify_slack:
        if not slack_channel:
            slack_channel = "#leave-notifications"
        result["slack_notify"] = True
        result["slack_channel"] = slack_channel
    if project_names:
        if isinstance(project_names, str):
            project_names = [p.strip() for p in project_names.split(",")]
        result["affected_projects"] = project_names
        if len(project_names) > 5:
            warnings.append("more than 5 projects affected, consider handover plan")
    if replacement_employee:
        result["replacement"] = replacement_employee
    if urgency_level:
        if urgency_level not in ["low", "medium", "high", "critical"]:
            errors.append("invalid urgency_level")
        result["urgency"] = urgency_level
    if carry_over_days:
        if carry_over_days > 5:
            errors.append("max carry over is 5 days")
        result["carry_over"] = carry_over_days
    if is_half_day:
        if morning_or_afternoon not in ["morning", "afternoon"]:
            errors.append("must specify morning or afternoon for half day")
        result["half_day"] = morning_or_afternoon
    result["employee"] = employee_name
    result["employee_id"] = employee_id
    result["department"] = department
    result["manager"] = manager_name
    result["type"] = leave_type
    result["reason"] = reason
    result["status"] = "pending"
    result["created_by"] = created_by
    result["created_at"] = datetime.datetime.now().isoformat()
    result["request_id"] = request_id
    result["ip_address"] = ip_address
    result["user_agent"] = user_agent
    result["session_id"] = session_id
    notification_list = []
    if manager_email:
        notification_list.append({"email": manager_email, "role": "manager"})
    if hr_email:
        notification_list.append({"email": hr_email, "role": "hr"})
    if employee_email:
        notification_list.append({"email": employee_email, "role": "employee"})
    result["notifications"] = notification_list
    result["errors"] = errors
    result["warnings"] = warnings
    if errors:
        result["status"] = "error"
        return result
    log_entry = f"{datetime.datetime.now()} | {employee_name} | {leave_type} | {start_date} to {end_date} | {result.get('days', 'N/A')} days"
    try:
        with open("/tmp/leave_requests.log", "a") as f:
            f.write(log_entry + "\n")
    except:
        pass
    try:
        with open("/tmp/leave_requests.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([employee_name, start_date, end_date, leave_type, reason, department, result.get("days", ""), result["status"]])
    except:
        pass
    return result


def calc_biz_days(start, end):
    count = 0
    current = start
    while current <= end:
        if current.weekday() < 5:
            count += 1
        current += datetime.timedelta(days=1)
    return count


def get_holidays():
    return [
        "2026-01-01",
        "2026-01-26",
        "2026-01-27",
        "2026-01-28",
        "2026-01-29",
        "2026-01-30",
        "2026-04-04",
        "2026-05-01",
        "2026-06-19",
        "2026-09-21",
        "2026-10-01",
        "2026-10-02",
        "2026-10-03",
    ]
