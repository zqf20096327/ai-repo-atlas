# Costasgk/ScoreCast

⭐ 19 · Python · MIT · 推送 2026-09-12 · [GitHub](https://github.com/Costasgk/ScoreCast) · 个人维护

**自托管的足球/篮球赛事比分与结果预测工具，附对庄家盘口的公开评测**

基于 Flask 的自托管 Web 应用：用 Dixon-Coles 泊松模型逐联赛拟合 36 个足球联赛，用对手调整岭回归处理 EuroLeague/EuroCup 篮球，输出胜平负概率、期望进球、全场比分分布、BTTS 与大小球等。内置 benchmark.py 以 walk-forward 方式对去水收盘赔率评测 log loss 与 Brier，并公布与市场的差距。数据从 football-data.co.uk、ESPN/FBref、euroleague.net 拉取，无需 API key；支持 docker compose 部署与 cron 定时刷新。附明确限制清单（升班马无评级、季后赛不建模等）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Dixon-Coles 泊松模型覆盖 36 个足球联赛，篮球用对手调整岭回归
- walk-forward 对去水收盘赔率评测 log loss / Brier 并公布差距
- 剩余赛季 10,000 次模拟得出夺冠/欧战/降级概率
- docker compose 一键部署，非特权运行，stats 页默认需鉴权

## 适用场景

- 自建服务查看足球/篮球赛事预测与比分分布
- 用收盘赔率基准检验自建预测模型的校准
- 模拟赛季剩余赛程的夺冠与降级概率

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: Match prediction for **36 football leagues** and **two basketball competitions**, scored
> L12: Football fixtures are predicted with a **Dixon-Coles Poisson model** fitted per league;
> L65: FootballData.py  →  fixtures.py  →  ScorelineModel.py  →  Flask web app

## 星数曲线

```mermaid
xychart-beta
    title "Costasgk/ScoreCast 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `5ff142579bc4` · [字段定义](../../DATASET.md)*
