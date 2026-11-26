# PabloTheThinker/hermespace

⭐ 10 · Python · MIT · 推送 2026-08-22 · [GitHub](https://github.com/PabloTheThinker/hermespace) · [官网](https://github.com/PabloTheThinker/hermespace) · 个人维护

**为 Hermes Agent 提供有界工作台与世界模型的 Python 配套工具**

Hermespace 是 Hermes Agent 的配套组件（自述非官方 Nous Research 产品，非第二运行时），MIT 许可。它为每次回合提供有界访问工作台（FOA≤4、双解码输出、技能与记忆织物排序注入）、持久化世界模型（JSONL 归档、belief 置信度、因果链、四阶段 epoch 演化）与自治网格、pulse 定时任务。可选软导入 HermesCube 与 Insight 插件而不改写已有插件与记忆配置。通过 hermes 插件钩子接入，需 Hermes Agent v0.20.0+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 持久化世界模型：epoch 演化、belief 置信度、因果链追踪与 evolve 五阶段循环
- 有界工作台：FOA≤4、双解码（用户短报告+模型单次精简注入）、≤9k 硬上限的上下文注入
- 十类 Hermes 插件钩子（会话、LLM 调用、工具、skill、kanban 等）与 hs CLI 全套命令
- Neural FOA 支持 Ollama embeddings，无后端时哈希回退

## 适用场景

- 为运行 Hermes Agent 的会话提供持久世界状态与记忆连续性
- 控制注入上下文体积，保持用户聊天不含中间推理内容
- 通过 CLI 审计、渲染与演化 agent 的长期状态

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L18: **Hermespace gives Hermes Agent a bounded, session-safe working room.** It
> L121: |**Skills + Memory Fabric**|Ranks Hermes skills per goal; injects MEMORY.md / USER.md excerpts|
> L253: Built by PabloTheThinker. Hermespace is an independent companion for Hermes Agent, not an official Nous Research p

## 星数曲线

```mermaid
xychart-beta
    title "PabloTheThinker/hermespace 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-24 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `fdc46d077f5a` · [字段定义](../../DATASET.md)*
