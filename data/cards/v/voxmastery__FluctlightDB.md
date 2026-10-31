# voxmastery/FluctlightDB

⭐ 13 · Jupyter Notebook · MIT · 推送 2026-10-05 · [GitHub](https://github.com/voxmastery/FluctlightDB) · [官网](https://github.com/voxmastery/FluctlightDB) · 组织维护

**面向 AI agent 的嵌入式记忆数据库引擎：写入、按线索回忆、溯源**

以记忆操作为原生接口的嵌入式数据库：experience() 写入记忆、activate() 按线索混合回忆（FTS5+向量+图扩散）、checkpoint() 持久化，Rust 核心，每个 agent 一个 brain 目录。提供 provenance 机制让已验证证据优先于对话内容，引擎内做整合/遗忘（Ebbinghaus 复习、时间 DAG 等 Fabric 模块）。支持 embedded/chorus/project 多种连接模式、MCP 集成、Docker HTTP 服务器与 WebGL 记忆查看器。基准数字为维护者自报，尚未有独立复现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 记忆原生 API：experience()/activate()/checkpoint()，Rust 核心
- 混合回忆：FTS5 + 向量 + 图扩散在一次 activate(cue) 中
- provenance 机制：已验证证据优先于聊天内容排序
- Docker HTTP 服务器与 WebGL Living Brain 查看器

## 适用场景

- 让长期运行的 agent 重启后仍保留所学记忆
- 用户换一种问法仍能召回相关记忆
- 在多工具 monorepo 中让多个 agent 共享记忆与交接

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Embedded memory database for AI agents** — `experience()` / `activate()` / `checkpoint()`, Rust core, one brain di
> L75: |**FluctlightDB**|What did the agent learn, and what should recall return for this cue?|`experience()` / `activate(

## 星数曲线

```mermaid
xychart-beta
    title "voxmastery/FluctlightDB 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d170a3af2be5` · [字段定义](../../DATASET.md)*
