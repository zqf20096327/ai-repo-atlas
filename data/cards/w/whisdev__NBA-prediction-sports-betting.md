# whisdev/NBA-prediction-sports-betting

⭐ 90 · TypeScript · 推送 2026-09-14 · [GitHub](https://github.com/whisdev/NBA-prediction-sports-betting) · 个人维护

**NBA 博彩研究 CLI：XGBoost 模型预测胜负并对比盘口计算期望值**

TypeScript 编写的命令行研究工具：抓取当晚 NBA 赛程与指定博彩公司（FanDuel、DraftKings 等 7 家）的实时盘口，从 NBA stats API 拉取球队效率、节奏与近期状态，结合赛程计算休息天数，用两个 XGBoost ONNX 模型（胜负与大小分）输出胜率预测，并与盘口价格对比计算期望值，可选输出 Kelly 仓位建议。README 声明为研究工具而非荐号服务，模型基于历史常规赛数据训练，一次仅能对比一家博彩公司。需要 Node.js 20+，可选 Redis 缓存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两个 XGBoost ONNX 模型：胜负预测与大小分预测
- 支持 7 家博彩公司盘口拉取并计算期望值（EV）
- 可选 Kelly 仓位计算与 Redis 缓存
- 提供从 XGBoost JSON 导出重新生成 ONNX 模型的脚本

## 适用场景

- 赛前对比模型胜率与博彩公司盘口寻找正 EV 投注
- 获取当晚 NBA 大小分倾向与置信度
- 用 Kelly 公式参考仓位大小

## 场景标签

 · 领域:体育/博彩分析

## 证据(README 行号)

> L74: 4. **Predict** — Two ONNX models: **moneyline winner** and **over/under** vs the book total.
> L5:  Moneyline model · ~69% validation accuracy &nbsp;|&nbsp;

## 星数曲线

```mermaid
xychart-beta
    title "whisdev/NBA-prediction-sports-betting 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 89 --> 91
    line [90, 90]
```

2026-10-18 90 → 2026-10-24 90（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `da9153b2820c` · [字段定义](../../DATASET.md)*
