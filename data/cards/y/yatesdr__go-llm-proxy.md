# yatesdr/go-llm-proxy

⭐ 43 · Go · MIT · 推送 2026-10-22 · [GitHub](https://github.com/yatesdr/go-llm-proxy) · [官网](https://go-llm-proxy.com) · 个人维护

**单二进制 LLM 代理：连接编码助手与本地/上游模型**

用 Go 编写的单二进制 LLM 代理，面向自托管模型或上游安全供应商（Azure、Bedrock 等）的开发者：在 Anthropic Messages、OpenAI Responses、Chat Completions、Bedrock Converse 等协议间自动双向翻译；将本地 GPU 服务器、云 API 与第三方供应商聚合为单一端点，并提供本地后端缺乏的附加工具——网页搜索（Tavily/Brave）、图像描述、PDF 文本提取与 PaddleOCR 排版解析、Whisper 语音路由、Qdrant 代理。支持按 key 的模型限制、SQLite 用量记录、管理后台与自助发 key。以二进制或 Docker Compose 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Anthropic/OpenAI/Bedrock 等多协议自动双向翻译
- 本地与云端后端聚合为单一端点，统一模型列表
- 代理侧补足网页搜索、图像描述、PDF/OCR 文档处理
- 按 key 发放与模型限制、SQLite 用量记录与管理后台

## 适用场景

- 让 Claude Code、Codex 等编码助手接入自托管或混合模型后端
- 团队通过自助链接申请带模型限制的代理 API key
- 为纯文本模型透明地补齐视觉、文档、网页搜索能力

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: A single-binary LLM proxy that connects coding assistants and AI agents to local and upstream models. Translates bet
> L13: - **Protocol translation** — Claude Code speaks Anthropic Messages. Codex speaks OpenAI Responses. Your vLLM speaks
> L14: - **Model multiplexing** — Aggregate local GPU servers, cloud APIs, and third-party providers behind one endpoint. 

## 星数曲线

```mermaid
xychart-beta
    title "yatesdr/go-llm-proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-28 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `916246c76141` · [字段定义](../../DATASET.md)*
