#!/usr/bin/env python3
"""韶音科技 - VPC 基础设施 CDK 骨架"""
import aws_cdk as cdk
from constructs import Construct


class ShokzVpcStack(cdk.Stack):
    """
    目标架构（请让 Claude Code 帮你补全）：

    1. VPC:
       - CIDR: 10.0.0.0/16
       - 2 个可用区

    2. 子网:
       - 每个 AZ 一个 Public Subnet (/24)
       - 每个 AZ 一个 Private Subnet (/24)
       - 每个 AZ 一个 Isolated Subnet (/24)（给数据库用）

    3. NAT Gateway:
       - 至少 1 个 NAT Gateway（放在 Public Subnet）
       - Private Subnet 的路由指向 NAT Gateway

    4. 其他:
       - VPC Flow Logs 开启
       - S3 Gateway Endpoint
       - 合理的标签（Environment, Project, Team）
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # TODO: 让 Claude Code 帮你在这里补全 VPC 基础设施
        pass


app = cdk.App()
ShokzVpcStack(app, "ShokzVpcStack",
    env=cdk.Environment(
        account="123456789012",
        region="cn-northwest-1"
    )
)
app.synth()
