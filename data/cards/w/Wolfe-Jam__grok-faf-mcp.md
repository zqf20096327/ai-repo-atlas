# Wolfe-Jam/grok-faf-mcp

⭐ 19 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/Wolfe-Jam/grok-faf-mcp) · [官网](https://faf.one) · 个人维护

**面向 xAI Grok 的持久项目上下文 MCP 服务器（.faf 格式）**

为 Grok/xAI 开发者提供的 MCP 服务器：以 IANA 注册的 .faf（application/vnd.faf+yaml）文件承载项目上下文，让 Grok 会话跨次保留项目信息。支持两种部署：托管在 Cloudflare Workers 的 URL 端点（mcpaas.live/grok/mcp/v1，WASM 纯工具）与本地 stdio 路径（brew/bunx，含文件系统操作）。提供 12 个核心工具（创建/检测/评分/同步/RAG 检索）与 34 个高级工具，评分由 always-33 WASM 内核执行。限制：RAG 查询需 xAI Collection；编排工具设计为偶发调用而非逐轮轮询。

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

- IANA 注册的 .faf 格式（vnd.faf+yaml）承载项目上下文
- URL 端点托管部署（Cloudflare Workers）与本地 stdio 两种路径
- 12 个核心工具 + 34 个高级工具（FAF_SHOW_ADVANCED=true）
- always-33 评分内核（Rust→WASM），本地与托管同分

## 适用场景

- 让 Grok 会话跨次保留项目栈与架构信息，避免重复说明
- 为 xAI 项目生成并评分 AI 可读的项目上下文文件
- 通过 refresh_faf/refresh_fafm 检测上下文与记忆层漂移
- 同步 .faf 到 CLAUDE.md 等平台上下文文件

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7:  Persistent Project Context for xAI Grok.
> L53: [mcp_servers.grok-faf-mcp]
> L87: |**WHERE** does it work?|Cloudflare Workers (`mcpaas.live/grok/mcp/v1`) • Any MCP client supporting native `url=` c

## 星数曲线

```mermaid
xychart-beta
    title "Wolfe-Jam/grok-faf-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `3093ff211085` · [字段定义](../../DATASET.md)*
