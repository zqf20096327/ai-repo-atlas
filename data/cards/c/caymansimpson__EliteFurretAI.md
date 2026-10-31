# caymansimpson/EliteFurretAI

⭐ 17 · Python · MIT · 推送 2026-07-20 · [GitHub](https://github.com/caymansimpson/EliteFurretAI) · 个人维护

**构建宝可梦 VGC 对战的超人类 AI 对战机器人**

个人研究项目，目标是用强化学习与模仿学习训练出超越人类水平的宝可梦 VGC（双打）对战 bot。当前已训练出一个约 3090 万参数的 Transformer 监督模型（TransformerThreeHeadedModel）预测人类玩家动作，Top-1 动作准确率 55.0%，Top-3 为 83.5%，换人/队伍预览预测准确率超过 99%。后续计划基于 RNaD 做自博弈 RL、联盟训练与队伍构建推导，最终打造以 Furret 为核心的队伍。README 未给出安装运行命令，当前处于 RL 阶段早期，方案可能调整。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- TransformerThreeHeadedModel 监督模型预测人类动作，Top-1/3 准确率 55.0%/83.5%
- 包含 mega 进化支持与 active-slot 位置特征
- 计划采用 RNaD 自博弈 RL 与联盟训练（ghosts/exploiters/启发式对手）
- 换人/强制换人/队伍预览预测准确率均超过 99.6%

## 适用场景

- 研究 VGC 双打这类不完美信息博弈的 AI 方法
- 复用其监督学习模型做 VGC 动作预测实验
- 跟踪超人类宝可梦对战 bot 的训练进展

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L2: **The goal of this project is to build a superhuman bot to play Pokemon VGC**. It is not to further research, nor is
> L50: Currently, I've built a supervised deep learning model (`TransformerThreeHeadedModel`) that predicts a human's acti
> L66: - RNaD based on the recent superhuman performance of the algorithm in Stratego, which is very similar to Pokemon

## 星数曲线

```mermaid
xychart-beta
    title "caymansimpson/EliteFurretAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `467dbff8fe4d` · [字段定义](../../DATASET.md)*
