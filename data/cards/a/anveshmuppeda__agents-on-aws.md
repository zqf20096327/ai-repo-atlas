# anveshmuppeda/agents-on-aws

⭐ 3 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/anveshmuppeda/agents-on-aws) · 个人维护

**面向开发者的 AWS AgentCore AI 代理实操教程集（66 篇）**

围绕 Amazon Bedrock AgentCore 的动手教程仓库，规划 66 篇指南，目前已发布 001–011 篇并经真实 AWS 账户验证。每篇包含源代码、CDK Python 基础设施、shell 部署脚本、Mermaid 架构图与成本估算，覆盖 Runtime、Memory、Gateway、Identity、Browser、Code Interpreter、Observability 等服务。使用前需安装 Node.js CLI 工具、配置 AWS 凭证并执行 cdk bootstrap；测试后需运行 destroy.sh 停止计费。作者为个人维护者，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 已发布 11 篇经过部署验证的 AgentCore 实操指南
- 每篇指南含 CDK 基础设施、deploy.sh 部署脚本与成本估算
- 支持任意代理框架（Strands/LangGraph/CrewAI）与模型（Nova/Claude/GPT-4o）
- 规划覆盖 AgentCore 全部服务模块共 66 篇指南

## 适用场景

- 按学习路径从本地代理入门到部署 AgentCore Runtime
- 为团队搭建 AWS 上的代理系统准备基础设施代码模板
- 学习 AgentCore 会话隔离、内存、MCP 网关等具体机制

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L63: Agents on AWS — 66 Hands-On Guides
> L89: This repo is a **complete, hands-on guide** to building AI agents on AWS using Amazon Bedrock AgentCore.
> L82: ✅ **Runnable, Not Theoretical** — Every guide deploys real AWS infrastructure with CDK Python; `bash deploy.sh` and

## 星数曲线

```mermaid
xychart-beta
    title "anveshmuppeda/agents-on-aws 星数(近 2 点)"
    x-axis ["2026-10-30", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-30 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `ef6edfc9c974` · [字段定义](../../DATASET.md)*
