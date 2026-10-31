# Logos-Flux/mnemo

⭐ 14 · TypeScript · MIT · 推送 2026-05-25 · [GitHub](https://github.com/Logos-Flux/mnemo) · 组织维护

**用 Gemini 上下文缓存为 AI 助手提供扩展记忆的 MCP server**

面向 Claude 等 AI 助手的 MCP server：将 GitHub 仓库（含私有）、任意 URL、PDF、JSON API、本地文件加载进 Gemini 的 1M token 上下文缓存，助手通过 6 个 MCP 工具（context_load/query/list/evict/stats/refresh）以自然语言查询缓存内容，缓存 TTL 为 60-86400 秒。提供本地服务器、自部署 Cloudflare Worker 与托管托管三种部署方式；Gemini API key 必需，API 用量始终由用户承担，缓存输入价格低于常规输入。CLI 尚未发布到 npm，需本地构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 加载 GitHub 仓库/URL/PDF/JSON API/本地目录到 Gemini 上下文缓存
- 6 个 MCP 工具：加载、自然语言查询、列出、清除、统计（含成本追踪）、刷新
- 三种部署方式：本地服务器、自部署 Cloudflare Worker、托管托管
- 缓存输入较常规输入有 75-90% 折扣，缓存存储约 $4.50/1M tokens/小时

## 适用场景

- 让 Claude 直接查询整个代码库或文档站点而无需自建 RAG 管线
- 为 Claude.ai 提供可从外网访问的扩展记忆端点（Cloudflare Worker 部署）
- 追踪多份大文档的缓存 token 用量与成本

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L17: Extended memory for AI assistants via Gemini context caching.
> L19: **Mnemo** (Greek: memory) gives AI assistants like Claude access to large codebases, documentation sites, PDFs, and
> L136: |`context_load`|Load GitHub repos, URLs, PDFs, or local dirs into Gemini cache|

## 星数曲线

```mermaid
xychart-beta
    title "Logos-Flux/mnemo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `c615a360dca2` · [字段定义](../../DATASET.md)*
