# oil-oil/wolfcha

⭐ 754 · TypeScript · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/oil-oil/wolfcha) · [官网](https://wolf-cha.com) · 个人维护 · 中文 README

**AI 狼人杀：玩家坐一个座位，LLM 填满其余席位**

基于 Next.js 的 AI 狼人杀游戏：1 名真人玩家加入 8–12 席对局，其余玩家由 LLM 驱动。每个 AI 有稳定个性叠加隐藏游戏身份，具备基于牌桌的记忆机制（跟随发言、投票、死亡与怀疑变化），按阵营目标决定指认、辩护、 bluff 或隐忍。支持 8 种角色（含预言家、女巫、猎人、守卫等），对话实时生成；提供复古视觉、口型同步动画、可选 AI 语音播放与观战模式。本地运行需 Node.js 和 pnpm，provider 通过 .env.local 配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 玩家具备角色个性与牌桌记忆（发言/投票/死亡/怀疑）
- 8 种经典狼人杀角色可选，对话实时生成
- 口型同步动画、昼夜过渡与可选 AI 语音播放
- 衍生自 Watcha × ModelScope Global Hackathon 项目

## 适用场景

- 凑不齐人时单人开一局狼人杀
- 体验与 LLM 驱动的多角色进行推理博弈
- 观战一桌 AI 玩家的社交推理对局

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5:  You take one seat. AI players fill the rest.
> L6:  An AI-native Werewolf game for deduction, bluffing, and chaos on demand.
> L31: You can play as **Villager, Werewolf, White Wolf King, Seer, Witch, Hunter, Guard, or Idiot**. Conversations are ge

## 星数曲线

```mermaid
xychart-beta
    title "oil-oil/wolfcha 星数(近 17 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-26", "2026-10-27", "2026-10-29", "2026-10-30", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-14", "2026-11-18", "2026-11-20", "2026-11-24"]
    y-axis "stars" 735 --> 753
    line [736, 737, 738, 739, 740, 742, 743, 744, 745, 738, 745, 746, 748, 749, 751, 752, 752]
```

2026-10-22 736 → 2026-11-24 752（+16）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `46b33c80bcf1` · [字段定义](../../DATASET.md)*
