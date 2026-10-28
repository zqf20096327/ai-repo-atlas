# aliencube/open-chat-playground

⭐ 53 · C# · MIT · 推送 2025-11-17 · [GitHub](https://github.com/aliencube/open-chat-playground) · [官网](https://bit.ly/openchat-playground) · 组织维护

**多平台 LLM 接入的 Blazor Web UI 聊天应用**

基于 .NET 9 / Blazor 的聊天 Web 应用，通过统一界面连接多家 LLM 平台：Amazon Bedrock、Azure AI Foundry、GitHub Models、Google Vertex AI、Docker Model Runner、Foundry Local、Hugging Face、Ollama、Anthropic、LG、OpenAI、Upstage 等。支持本地运行、本地容器运行与部署到 Azure，另暴露 OpenAPI 风格的聊天 API（/api/chat/responses）。提供单元测试与基于 Playwright 的集成测试（依赖本地 Ollama）。运行需 Azure 订阅、.NET SDK 9、Docker Desktop 等前置条件；Naver 已从支持列表移除。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 13 家 LLM 平台的统一 Web 聊天界面
- 提供本地、容器与 Azure 三种运行方式
- 暴露 /api/chat/responses API（OpenAPI 文档仅本地可见）
- 含单元测试与依赖本地 Ollama 的 Playwright 集成测试

## 适用场景

- 在同一界面切换使用多家 LLM 提供商
- 本地通过 Ollama 或 Docker Model Runner 运行模型对话
- 以 API 形式调用集成的多家 LLM

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: Open Chat Playground (OCP) is a web UI that is able to connect virtually any LLM from any platform.
> L9: - [x] Amazon Bedrock
> L63: - Use Amazon Bedrock

## 星数曲线

```mermaid
xychart-beta
    title "aliencube/open-chat-playground 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-28 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b5af97abd278` · [字段定义](../../DATASET.md)*
