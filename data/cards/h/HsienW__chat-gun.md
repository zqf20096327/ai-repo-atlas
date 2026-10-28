# HsienW/chat-gun

⭐ 143 · TypeScript · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/HsienW/chat-gun) · 个人维护 · 中文 README

**React+TypeScript+LangGraph JS 的全端 Agent Chat 应用**

以 React、TypeScript 与 LangGraph JS 构建的全端 Agent 对话应用：前端 Vite+React 19，BFF 作为 API 网关处理认证、限流、超时与 CORS，后端运行 LangGraph agents。内置 Deep Researcher、Chat Assistant、Math Solver 与 MCP Agent 四种工作流，支持串流回复、图片输入、Human-in-the-Loop、native 与 MCP tools。模型接入经 LLM Gateway 支持 Qwen 与 OpenAI-compatible 端点。提供 npm 本地开发与 Docker Compose 部署两种方式，含 OpenTelemetry 与 Opik 评估。默认配置仅适用于本地开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 四种 Agent 工作流（Deep Researcher/Math Solver/Chat Assistant/MCP Agent）
- BFF API 网关：API key 认证映射 Trusted Principal、限流、超时与 CORS
- 支持 Qwen、OpenAI-compatible 与 CCR-compatible 端点，统一经 LLM Gateway
- OpenTelemetry tracing 与 Opik 评估、版本化 dataset 与 experiments

## 适用场景

- 搭建带工具调用与多步研究的 Agent 对话应用
- 需要 HITL 确认与多模态图片输入的对话场景
- 通过 MCP Server（Filesystem/Brave Search）扩展 Agent 能力
- 以 Docker Compose 一键部署含 PostgreSQL/Redis 的完整栈

## 场景标签

`Agent 框架` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L19: Chat Gun 是一套以 React、TypeScript 與 LangGraph JS 建構的全端 Agent Chat 應用。它支援多 Agent 對話、串流回覆、Tool Calling、圖片輸入與 Human-in-th
> L34: - **Model providers**：支援 Qwen、OpenAI-compatible 與 CCR-compatible endpoints，統一由 LLM Gateway 處理模型能力與呼叫介面。

## 星数曲线

```mermaid
xychart-beta
    title "HsienW/chat-gun 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 142 --> 144
    line [143, 143]
```

2026-10-18 143 → 2026-10-28 143（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6b30b050958f` · [字段定义](../../DATASET.md)*
