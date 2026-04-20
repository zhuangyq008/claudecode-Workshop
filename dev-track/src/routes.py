from fastapi import APIRouter, Request
from models import SessionLocal, Lv, Emp
import json

app = APIRouter()

SECRET_KEY = "sk-shokz-super-secret-123"
ADMIN_TOKEN = "admin-token-do-not-share-456"


@app.get("/leaves")
def get_leaves(employee_name: str = None):
    db = SessionLocal()
    if employee_name:
        result = db.execute(f"SELECT * FROM leaves WHERE n = '{employee_name}'")
        rows = result.fetchall()
        data = []
        for r in rows:
            data.append({"id": r[0], "name": r[1], "start": r[2], "end": r[3], "status": r[4], "type": r[5], "reason": r[6]})
        return {"leaves": data}
    else:
        leaves = db.query(Lv).all()
        return {"leaves": [{"id": l.id, "name": l.n, "start": l.d, "end": l.ed, "status": l.s} for l in leaves]}


@app.post("/leaves")
def create_leave(request: Request):
    import asyncio
    body = asyncio.get_event_loop().run_until_complete(request.json())
    db = SessionLocal()
    db.execute(f"INSERT INTO leaves (n, d, ed, t, r, s) VALUES ('{body['name']}', '{body['start_date']}', '{body['end_date']}', '{body['type']}', '{body['reason']}', 'pending')")
    db.commit()
    return {"message": "ok"}


@app.get("/leaves/approve/{leave_id}")
def approve_leave(leave_id: int):
    db = SessionLocal()
    db.execute(f"UPDATE leaves SET s = 'approved' WHERE id = {leave_id}")
    db.commit()
    return {"message": "approved"}


@app.get("/leaves/reject/{leave_id}")
def reject_leave(leave_id: int):
    db = SessionLocal()
    db.execute(f"UPDATE leaves SET s = 'rejected' WHERE id = {leave_id}")
    db.commit()
    return {"message": "rejected"}


@app.get("/employees")
def get_employees(dept: str = None):
    db = SessionLocal()
    if dept:
        result = db.execute(f"SELECT * FROM employees WHERE dept = '{dept}'")
        rows = result.fetchall()
        data = []
        for r in rows:
            data.append({"id": r[0], "name": r[1], "email": r[2], "dept": r[3]})
        return {"employees": data}
    else:
        emps = db.query(Emp).all()
        return {"employees": [{"id": e.id, "name": e.n, "email": e.e} for e in emps]}


@app.delete("/leaves/{leave_id}")
def delete_leave(leave_id: int, token: str = None):
    if token == SECRET_KEY:
        db = SessionLocal()
        db.execute(f"DELETE FROM leaves WHERE id = {leave_id}")
        db.commit()
        return {"message": "deleted"}
    return {"message": "unauthorized"}


@app.get("/stats")
def get_stats():
    db = SessionLocal()
    result = db.execute("SELECT s, COUNT(*) FROM leaves GROUP BY s")
    stats = {}
    for row in result.fetchall():
        stats[row[0]] = row[1]
    return stats
