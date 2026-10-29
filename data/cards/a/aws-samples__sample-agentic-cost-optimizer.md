# aws-samples/sample-agentic-cost-optimizer

⭐ 17 · Python · MIT-0 · 推送 2026-10-26 · [GitHub](https://github.com/aws-samples/sample-agentic-cost-optimizer) · 组织维护

**分析 AWS Lambda 成本并生成优化建议报告的 AI agent 示例**

AWS 官方 samples 组织的示例项目：基于 Strands Agents 与 Amazon Bedrock 模型（默认 Claude Sonnet 4.5）、部署在 Bedrock Agent Core 上的成本优化 agent。两阶段工作流——分析阶段发现 Lambda 函数、采集 CloudWatch 指标与日志并识别优化机会，报告阶段生成含预估节省额与实施步骤的报告，存入 S3 并以 DynamoDB 记录审计。编排用 Step Functions + EventBridge，基础设施用 AWS CDK (TypeScript) 部署，需 Python 3.12+、uv、Node.js 20+ 与 AWS CLI。README 自述为进行中的示例项目，默认分析 us-east-1 区域。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT-0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 两阶段工作流：Lambda 资源发现与指标分析 → 成本优化报告生成
- 4 个工具：use_aws 采集数据、calculator 计算、storage 存 S3、journal 记 DynamoDB
- AWS CDK 一键部署，支持定时（每日 6am UTC）与手动触发
- AgentCore 在线评测（Evals）与 CloudWatch 可观测性配置

## 适用场景

- 我在 AWS 上跑了大量 Lambda 函数，想自动得到内存与调用模式的成本优化建议
- 参考其代码结构学习如何用 Strands Agents 和 Bedrock Agent Core 构建 agent
- 以定时任务形式周期性生成成本报告并存档审计

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L6: An AI agent that analyzes your AWS Lambda functions and generates cost optimization reports. It discovers AWS Lambda
> L19: - **Agent Runtime**: Python agent using Strands Agents and Amazon Bedrock models

## 星数曲线

```mermaid
xychart-beta
    title "aws-samples/sample-agentic-cost-optimizer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-29 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `946d7c9f93ff` · [字段定义](../../DATASET.md)*
