# AndreaGriffiths11/agent-context-system

⭐ 26 · Shell · MIT · 推送 2026-10-29 · [GitHub](https://github.com/AndreaGriffiths11/agent-context-system) · [官网](https://agents.mainbranch.dev/) · 个人维护

**AI agent 的本地记忆管理库：日志、压缩与上下文索引**

面向 AI agent 开发者的记忆系统工具库：以纯 markdown 文件存储追加式每日日志，提供带评分的关键词搜索、上下文窗口感知的索引（上限 200 行/25KB），以及 9:1 压缩比的四阶段合并流程（Orient→Gather→Consolidate→Prune）与防并发锁机制。零依赖、完全离线，通过 pip 从 GitHub 仓库安装，Apache-2.0 许可，README 中附与 mem0、supermemory、mempalace 的功能对比表。

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

- 追加式每日日志，保留完整审计轨迹
- 自动合并实现 9:1 压缩（107KB→11.6KB），带锁机制防并发
- 上下文窗口感知：MEMORY.md 上限 200 行/25KB
- 零依赖、纯 markdown、完全离线

## 适用场景

- 为离线运行的 agent 维护带审计日志的记忆
- 在上下文窗口受限的 agent 中获取压缩后的记忆索引
- 对 agent 历史记录做带评分的关键词检索

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Production-tested memory system for AI agents**
> L41: |`memory.append()`|Write to daily log (auto-timestamped)|
> L45: |`memory.consolidate()`|4-phase consolidation (Orient → Gather → Consolidate → Prune)|

## 星数曲线

```mermaid
xychart-beta
    title "AndreaGriffiths11/agent-context-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `04e8dd216841` · [字段定义](../../DATASET.md)*
