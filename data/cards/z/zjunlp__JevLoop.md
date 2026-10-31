# zjunlp/JevLoop

⭐ 24 · TypeScript · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/zjunlp/JevLoop) · 组织维护 · 中文 README

**零依赖的 TypeScript Agent 循环运行时：决策交给决策模型，LLM 只负责写作**

面向 Agent 开发者的可运行框架：把循环中每个分叉（是否行动、选哪个工具、是否安全、是否完成、能否交付）从 LLM 生成调用改路由到决策模型（Jev API 或本地 Laya），LLM 仅在写作环节调用。核心机制是可编译的 DECISION.md：结构块转为决策模型的问题与策略，散文转为系统提示；含 frame 声明、闭合谓词词表、阈值覆盖校验与一致性检查。提供 CLI、Web UI、基准与对比脚本，需 Node ≥ 22.6，零依赖、零构建步骤，离线 demo 无需 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分叉决策路由到决策模型（noul/choice/score 三原语），LLM 仅负责写作
- DECISION.md 可编译：结构块生成问题与策略，加载时解析并报出问题行号
- 阈值可用 --gate/JEVLOOP_GATES 覆盖，未知键致命、生效值记入 journal
- 零依赖、零构建步骤，离线 demo 无需 API key，附 Web UI 与 ReAct 对比脚本

## 适用场景

- 构建把循环决策与文本生成分离的 Agent 应用
- 用声明式文件管理 Agent 的门控、路由与风险策略
- 度量决策式循环与传统 ReAct 循环在调用数、token 与耗时上的差异

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: It is a **runnable harness**, not a demo: the loop, the backend seams, the accounting and a web UI — all of it in on
> L45: |Question the loop asks|Conventional agent|JevLoop|
> L104: npm run demo -- --laya     # local Laya sidecar on :7789 (open weights, free)

## 星数曲线

```mermaid
xychart-beta
    title "zjunlp/JevLoop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-31 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `578c6d4270ec` · [字段定义](../../DATASET.md)*
