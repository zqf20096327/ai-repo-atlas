# guyernest/step-functions-agent

⭐ 35 · Python · MIT · 推送 2026-02-24 · [GitHub](https://github.com/guyernest/step-functions-agent) · 个人维护

**AWS CDK 框架：用 Lambda 与 Step Functions 构建无服务器 AI Agent**

基于 AWS CDK 的无服务器 AI Agent 构建框架，由两部分组成：Agent 运行时（Lambda + Step Functions 编排，支持多 LLM 提供商切换、用任意语言编写工具、内置 Human-in-the-Loop 审批）与基于 Amplify 的管理 UI（Agent 配置、工具注册、执行监控、成本分析、Cognito 认证）。LLM 调用通过统一的 Rust LLM 服务或各提供商 Lambda 完成，API key 存于 Secrets Manager。附 10 余个内置工具（SQL、Web 研究、代码执行、CloudWatch 等）。需 AWS 账户、Python 3.12+、Node.js 18+，以 CDK 部署。

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

- 多提供商 LLM 支持：Anthropic/OpenAI/Gemini/Bedrock/xAI/DeepSeek，切换无需改代码
- 工具与语言无关：Python/TypeScript/Rust/Go/Java 均可编写工具 Lambda
- 统一 Rust LLM 服务提供与提供商无关的调用接口
- 管理 UI 提供执行监控、成本追踪、Agent 动态配置与测试回放

## 适用场景

- 在 AWS 上以无服务器架构部署生产级 AI Agent
- 统一管理多个 Agent 的模型选择、工具分配与执行成本
- 为企业运营团队提供带鉴权与审计的 Agent 管理界面

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: The Step Functions AI Agent Framework consists of two integrated components:
> L11: ### 1. **AI Agent Runtime** (Lambda + Step Functions)
> L13: - **Any LLM Provider**: Anthropic Claude, OpenAI GPT, Google Gemini, Amazon Bedrock, xAI Grok, DeepSeek

## 星数曲线

```mermaid
xychart-beta
    title "guyernest/step-functions-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-25 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `64c50f7f2e5a` · [字段定义](../../DATASET.md)*
