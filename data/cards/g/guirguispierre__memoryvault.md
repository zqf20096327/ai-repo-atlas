# guirguispierre/memoryvault

⭐ 14 · TypeScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/guirguispierre/memoryvault) · 个人维护

**自托管的图感知 MCP 记忆服务器，供 AI 客户端跨会话存取记忆**

部署在 Cloudflare Workers + D1 上的记忆服务器，通过 Model Context Protocol 为 Claude、ChatGPT 等 AI 客户端提供跨会话持久记忆：存储笔记、事实与日志条目，将相关记忆以类型化关系连成知识图谱，支持路径查找与邻域遍历；检索采用词法+语义（Vectorize 与 Workers AI bge 嵌入）混合搜索并做 RRF 融合。提供 40 余个 MCP 工具、多租户隔离 brain、OAuth+PKCE 认证与 Web 查看器。限制：语义搜索需 Workers AI/Vectorize 绑定，完整功能需远程开发模式运行。

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

- 40+ MCP 工具：记忆 CRUD、图谱链接、冲突检测、快照、目标管理等
- 词法+语义混合检索（Vectorize + Workers AI 嵌入）+ RRF 融合
- 类型化关系的知识图谱：路径查找、邻域遍历、推断链接
- 多租户隔离 brain 与 OAuth+PKCE 标准认证

## 适用场景

- 让 Claude/ChatGPT 等客户端在多会话间保留用户记忆
- 把笔记、事实与日志组织为可检索的知识图谱
- 多用户场景下为每个用户维护隔离的记忆空间

## 场景标签

`知识图谱` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: A self-hosted, graph-aware memory server for AI assistants. Built on Cloudflare Workers + D1.
> L5: MemoryVault gives AI clients (Claude, ChatGPT, etc.) persistent memory across sessions via the Model Context Protoco
> L104: **Tech stack:** Cloudflare Workers, D1 (SQLite), Vectorize, Workers AI (`@cf/baai/bge-base-en-v1.5`), MCP SDK

## 星数曲线

```mermaid
xychart-beta
    title "guirguispierre/memoryvault 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5c1af6dc9a67` · [字段定义](../../DATASET.md)*
