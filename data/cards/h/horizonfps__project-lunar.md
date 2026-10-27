# horizonfps/project-lunar

⭐ 42 · Python · 推送 2026-09-07 · [GitHub](https://github.com/horizonfps/project-lunar) · 个人维护

**LLM 驱动的本地优先叙事 RPG 引擎：作者建世界，AI 讲故事**

开源叙事 RPG 引擎而非单一游戏：作者用设定向导构建含剧情、NPC、阵营的场景，玩家通过 DO/SAY/CONTINUE/META 行动推进冒险，由 LLM 实时叙述。核心机制包括 4 层记忆金字塔（SHORT→MEDIUM→LONG→MEMORY，每 4 次行动自动结晶）、带见证过滤的独立 NPC 心智、基于创意评分（连贯/创意/语境 40/40/20）的无 HP 战斗、Neo4j 知识图谱与 RAG 动态故事卡。经 litellm 支持 DeepSeek/Anthropic/OpenAI 运行时切换，英葡双语。需 Python 3.10+、Node.js 18+、Docker（Neo4j）与至少一个 LLM API key，从源码安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 层记忆金字塔：每 4 次行动结晶一次，人名保真与见证过滤
- 创意评分战斗：无 HP/法力，LLM 评估双方战力并可用剧情卡 NPC 锚定
- 独立 NPC 心智：跟踪情感、目标、对玩家看法与秘密计划
- 多 LLM 运行时切换（DeepSeek/Anthropic/OpenAI），自动检测上下文窗口

## 适用场景

- 作为作者构建带设定向导的自定义叙事场景
- 以玩家身份进行由 AI 实时叙述的互动冒险
- 长战役（200+ 行动）中保持记忆与世界观一致性

## 场景标签

 · 领域:游戏/互动叙事

## 证据(README 行号)

> L18: Project Lunar is a **local-first** narrative RPG **engine**, not a single game. Authors build scenarios — fantasy, 
> L40: |**Multi-LLM**|Runtime Switching|DeepSeek V4 (1M ctx), Anthropic Sonnet/Opus 4.6 (1M ctx), OpenAI GPT-5.6 Sol — swi
> L192: Project Lunar supports multiple LLM providers via litellm. Switch providers at runtime in the Settings panel.

## 星数曲线

```mermaid
xychart-beta
    title "horizonfps/project-lunar 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-27 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `386f51bcdd86` · [字段定义](../../DATASET.md)*
