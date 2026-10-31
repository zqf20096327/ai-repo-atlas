# danilop/MCP2Lambda

⭐ 109 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/danilop/MCP2Lambda) · 个人维护

**把 AWS Lambda 函数作为 LLM 工具暴露的 MCP 服务器桥接层**

MCP2Lambda 是一个 MCP 服务器，作为 MCP 客户端与 AWS Lambda 之间的桥接：自动发现账户中以 mcp2lambda- 为前缀或白名单内的 Lambda 函数，并将其注册为 LLM 可调用的工具（Pre-Discovery 模式）或通过 list/invoke 两个通用工具访问（Generic 模式），无需修改函数代码。面向需要让模型访问私有资源（VPC 内数据、内部应用）的场景，通过职责分离限制模型直接访问 AWS 服务的权限。需 Python 3.12+ 与已配置的 AWS 凭证，可配合 Amazon Bedrock Converse API 或 Claude Desktop 使用，附三个示例函数与 SAM 部署流程。

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

- 自动发现并注册 Lambda 函数为 LLM 工具（前缀或白名单过滤）
- 两种策略：Pre-Discovery（逐函数注册）与 Generic（list/invoke 通用工具）
- 职责分离安全模型：客户端仅需调用 Lambda 的凭证，函数角色负责访问其他 AWS 服务
- 提供 Amazon Bedrock Converse API 客户端实现与三个示例函数

## 适用场景

- 让 Claude 等模型访问 VPC 内私有数据库或内部应用而无需公网暴露
- 把现有 Lambda 函数复用为 LLM 工具而无需改代码
- 用 Lambda 沙箱让模型执行任意 Python 代码做计算与数据处理

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: Run any AWS Lambda function as a Large Language Model (LLM) **tool** without code changes using Anthropic's Model Co
> L16: This MCP server acts as a **bridge** between MCP clients and AWS Lambda functions, allowing generative AI models to
> L68: The server uses the MCP protocol, which standardizes the way AI models can access external tools.

## 星数曲线

```mermaid
xychart-beta
    title "danilop/MCP2Lambda 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-10-31"]
    y-axis "stars" 108 --> 110
    line [109, 109]
```

2026-10-28 109 → 2026-10-31 109（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `b990c1a11414` · [字段定义](../../DATASET.md)*
