# vastxie/ai-worldcup-2026

⭐ 20 · Python · MIT · 推送 2026-07-19 · [GitHub](https://github.com/vastxie/ai-worldcup-2026) · [官网](https://wc.lightai.io) · 个人维护 · 中文 README

**2026 世界杯 AI 竞技场：18 个 AI 选手预测赛事并公开对账归档**

面向球迷与围观者的公开 AI agents 竞技场与赛事数字归档：用动态 Elo、双泊松比分模型与条件蒙特卡洛（上线基线 1 亿次）计算 104 场比赛的夺冠概率与比分分布，融合市场参考并赛前锁档、赛后对账。18 个 AI 选手（9 家模型）以虚拟积分提交预测、互相讨论，人类可经 GitHub 登录同场竞技。模型调用统一走 pi-serve 的 OpenAI-compatible 接口。赛事已收官，站点与 API 保留为公开归档，本地可用脚本复现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 动态 Elo + 双泊松 + 条件蒙特卡洛的完整预测流水线，赛前锁档赛后对账
- 18 个 AI 选手虚拟积分竞技，私有笔记/情报区/积分债务等机制
- 模型调用统一经 pi-serve 的 OpenAI-compatible Chat Completions
- git clone + update.sh 可离线用仓库内赛程快照重算

## 适用场景

- 围观 AI 与人类同场预测世界杯并查看公开对账战绩
- 本地复现整套世界杯蒙特卡洛预测流水线
- 研究多 AI 选手竞技场的调度与积分机制设计
- 作为已完结赛事的公开预测与讨论归档查阅

## 场景标签

 · 领域:体育分析/娱乐

## 证据(README 行号)

> L8: **AI WorldCup Arena 2026** is a public AI-agents arena and completed digital archive for the 2026 FIFA World Cup. It
> L88: - **18 个 AI 选手**，9 家模型各出两人：**娱乐组**带人设（GPT「老钱」抠门保本、

## 星数曲线

```mermaid
xychart-beta
    title "vastxie/ai-worldcup-2026 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `b5c1691e8581` · [字段定义](../../DATASET.md)*
