# KSroido/Kagi-Session2API-MCP

⭐ 44 · Python · 推送 2026-05-26 · [GitHub](https://github.com/KSroido/Kagi-Session2API-MCP) · 个人维护 · 中文 README

**用 Kagi 会话 token 免费调用搜索与摘要的 MCP 服务器**

面向 MCP 客户端（Claude Desktop、Cursor、Windsurf、Cline 等）的 Kagi 搜索服务器：以 Kagi 会话 token 替代官方付费 API key，通过 HTML 抓取实现 kagi_search_fetch 网页搜索与 kagi_summarizer URL 摘要两个工具。支持多 token 轮换池、每 token 5 req/s 令牌桶限速、过期 token 自动停用，输出格式与官方 kagimcp 一致。支持 stdio 与 HTTP 两种传输。README 明示此用法可能违反 Kagi 服务条款，存在账号被封风险；摘要功能依赖 Kagi 内部端点，标记为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 会话 token 替代官方 API key，无付费成本
- 多 token 轮换池 + 每 token 5 req/s 令牌桶限速
- 提供 kagi_search_fetch 与 kagi_summarizer 两个 MCP 工具
- 支持 stdio 与 HTTP 传输，兼容任意 MCP 客户端

## 适用场景

- 让 Claude Desktop / Cursor 等 AI 编程助手调用 Kagi 搜索
- 多 token 池提升搜索吞吐（每 token 5 req/s）
- 对任意 URL 生成摘要（prose 或要点模式）

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L29: - **Two tools**: `kagi_search_fetch` (web search) and `kagi_summarizer` (URL summarization)
> L36: Works with any MCP-compatible client:
> L164: MCP Client → FastMCP Server → TokenPool (round-robin) → httpx.AsyncClient → kagi.com

## 星数曲线

```mermaid
xychart-beta
    title "KSroido/Kagi-Session2API-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f6a47a13de60` · [字段定义](../../DATASET.md)*
