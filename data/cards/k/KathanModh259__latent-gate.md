# KathanModh259/latent-gate

⭐ 25 · Python · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/KathanModh259/latent-gate) · [官网](https://kathanmodh259.github.io/latent-gate/) · 个人维护

**MCP 服务器：在 AI 读取前压缩日志/JSON/文档/网页以省 token**

面向使用 AI 编码工具与 LLM 应用的开发者：以 MCP 服务器形式接入 Claude Code、Claude Desktop、Cursor、Cline、Continue、Zed 等，在内容送入云端模型前做确定性压缩（66% 省率，日志 90%+，~3ms，无需 API key）。优化器工具完全离线；图像/文本压缩可选用本地 Ollama（llava:7b、llama3:8b）做事实核查压缩。另提供 Python API、FastAPI REST 服务、Docker Compose 部署与 Prometheus/Grafana 监控栈，支持多远程提供商切换与 SQLite 成本追踪。注意 License 为 Proprietary；默认 balanced 级别折叠近重复行会丢失个别 ID。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性 token 优化器：离线、~3ms、无 API key，代码块/URL/引号字节级保留
- MCP 接入 Claude Code / Desktop / Cursor / Cline / Continue / Zed
- 可选本地 Ollama 做图像描述与事实核查文本压缩
- 提供 REST API、Docker Compose 全栈与 Prometheus/Grafana 监控

## 适用场景

- 让 Claude/Cursor 等 AI 编码工具读大日志和 JSON 时少花 token
- 本地压缩长提示词、对话与 RAG 文档再送云端模型
- 为 LLM 应用部署带监控与成本追踪的压缩 API 服务

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: **An MCP server that shrinks logs, JSON, docs and web pages before your AI reads them — offline, deterministic, in ~
> L89: LatentGate plugs into Claude as an MCP server. Its optimizer tools work **offline, with no
> L368: LatentGate works as a Model Context Protocol (MCP) server with every major AI coding tool. Your AI assistant autom

## 星数曲线

```mermaid
xychart-beta
    title "KathanModh259/latent-gate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a900cb8d2e07` · [字段定义](../../DATASET.md)*
