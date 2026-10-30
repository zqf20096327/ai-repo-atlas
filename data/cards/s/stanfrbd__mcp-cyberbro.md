# stanfrbd/mcp-cyberbro

⭐ 19 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/stanfrbd/mcp-cyberbro) · [官网](https://docs.cyberbro.net/integrations/Use-Cyberbro-MCP-for-LLM/) · 个人维护

**Cyberbro 威胁情报分析的 MCP 服务器，供 AI 助手调用**

Model Context Protocol 服务器，把 Cyberbro 威胁分析平台的观测对象分析能力（IP、域名、URL、哈希等）接入 MCP 兼容助手。提供 analyze_observable、get_analysis_results、get_engines 等工具，支持 stdio、sse、streamable-http 三种传输方式，需配置 CYBERBRO_URL 指向 Cyberbro 实例。以 Python 包（uvx/pip）与 Docker 镜像分发，附 Claude Desktop、Cursor、VSCode 等客户端接入配置示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个 MCP 工具：观测对象分析、结果查询、引擎列表等
- 支持 stdio/sse/streamable-http 三种传输
- uvx、pip、Docker（ghcr.io 镜像）多种分发方式
- 需外部 Cyberbro 实例（CYBERBRO_URL 必填）

## 适用场景

- 在 MCP 助手中直接提交 IP/域名/哈希做威胁分析
- 对可疑观测对象生成 OSINT 调查报告
- 在 Claude Desktop/Cursor/VSCode 中集成威胁情报查询

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L11: Model Context Protocol server for Cyberbro.
> L20: - Analyze observables (IP, domain, URL, hash, etc.) via Cyberbro engines.
> L93: You can use this server with Claude Desktop, Claude Code, Cursor, OpenAI-compatible MCP clients, or any other MCP c

## 星数曲线

```mermaid
xychart-beta
    title "stanfrbd/mcp-cyberbro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `957af49baf59` · [字段定义](../../DATASET.md)*
