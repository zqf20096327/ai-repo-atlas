# totocaster/arrowhead

⭐ 44 · Rust · MIT · 推送 2026-08-12 · [GitHub](https://github.com/totocaster/arrowhead) · [官网](https://ttvl.co/arrowhead) · 个人维护

**Obsidian 知识库的常驻索引守护进程，供人与 AI agent 快速检索**

Rust 编写的跨平台 CLI 与守护进程，持续监视 Obsidian vault 或任意 Markdown 目录，构建全文（SQLite FTS5）与语义向量（fastembed + sqlite-vec）索引，提供混合搜索、笔记 CRUD、图谱分析（反链/孤儿/未解析链接）与发现工具。通过标准 MCP 协议（stdio 与 HTTP 传输，支持 token 认证、CIDR 白名单）将能力暴露给 Claude Code、Claude.app、OpenClaw、Codex 等 agent。语义模式需加载约 90MB ONNX 模型，空闲时典型内存占用约 1GB，可用 --fts-only 降级为纯全文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 后台守护进程实时监视文件并维护全文+向量双索引
- MCP stdio/HTTP 双传输，含 token 认证与 CIDR 白名单
- fastembed 语义向量存于 sqlite-vec，支持 FTS/语义/混合搜索
- 图谱分析：反链、正向链接、孤儿笔记、未解析链接

## 适用场景

- 为 Claude Code / OpenClaw 等 agent 提供本地笔记的搜索与发现工具
- 对 Obsidian vault 做混合检索和知识图谱探索
- 通过 MCP 远程访问自己的知识库

## 场景标签

`知识库管理` `知识图谱` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L5: Arrowhead is a cross-platform CLI and daemon that keeps your Obsidian vault indexed around the clock. It combines fa
> L24: - Notes CRUD, graph analytics, and discovery helpers via CLI or MCP tool surface.
> L164: - `arrowhead --mcp[(-server)]` — launch the stdio or HTTP MCP transport with shared handlers, token auth, CIDR fil

## 星数曲线

```mermaid
xychart-beta
    title "totocaster/arrowhead 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-25 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `12406e7b317a` · [字段定义](../../DATASET.md)*
