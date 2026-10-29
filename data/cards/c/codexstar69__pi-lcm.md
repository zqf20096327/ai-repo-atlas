# codexstar69/pi-lcm

⭐ 19 · TypeScript · MIT · 推送 2026-04-02 · [GitHub](https://github.com/codexstar69/pi-lcm) · 个人维护

**Pi 编程助手的无损上下文管理扩展：SQLite 存档+DAG 压缩摘要**

面向 Pi（Pi 0.58+ 编码 agent）的 TypeScript 扩展，解决 Pi 默认 compaction 丢弃原始消息的问题：每条消息持久化到 SQLite（FTS5 全文检索），压缩时生成层级 DAG 摘要而非单一扁平摘要，agent 可通过 lcm_grep/lcm_describe/lcm_expand 三个工具检索并回溯压缩节点恢复原始内容。摘要使用廉价快速模型（可配置），DAG 深度对数增长，保留 prompt caching。经 npm 或 pi install 安装，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每条消息持久化到 SQLite，支持 FTS5 全文搜索
- 压缩为层级 DAG 摘要，可通过三个 agent 工具回溯恢复原始消息
- 摘要使用廉价模型（cerebras/anthropic 可配置）而非会话模型
- 含 XML 围栏防注入、FTS5 查询消毒、ReDoS 上限等安全措施

## 适用场景

- 长会话编程时保留全部历史消息避免扁平摘要丢信息
- agent 在压缩后仍可搜索并回溯任意历史细节
- 跨会话保留同一项目的历史记录

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L17: Pi's default compaction throws away old messages when the context window fills up. A single flat summary replaces e
> L19: pi-lcm fixes this. Every message is stored permanently in SQLite. When compaction triggers, messages are summarized
> L35: 2. When Pi triggers compaction, pi-lcm creates hierarchical DAG summaries instead of flat text

## 星数曲线

```mermaid
xychart-beta
    title "codexstar69/pi-lcm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8b26cce0c90f` · [字段定义](../../DATASET.md)*
