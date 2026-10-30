# d-roho/CSGOPredictor

⭐ 16 · Python · 推送 2026-05-05 · [GitHub](https://github.com/d-roho/CSGOPredictor) · 个人维护

**为 CS:GO 观赛生成实时回合胜负概率预测的 Python 程序**

通过 CS:GO 内置的 Game State Integration 功能，在比赛观战时捕获回合快照数据，经解析清洗生成 23 个属性（地图、剩余时间、炸弹下包状态、双方存活人数/总血量、武器装备等），输入预训练的逻辑回归模型，输出 CT/T 双方回合胜率概率，打印到终端并写入 predictions.txt 供其他程序（如 GUI 动态预测条）使用。模型基于 12 万余条高水平锦标赛快照数据训练，以校准度为主要指标。需在本地安装 Python 3 与依赖后运行，并将 GSI 配置文件复制到游戏 cfg 目录；暂停功能目前仅在 Anaconda 环境下可用。

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

- 基于 GSI 捕获回合快照并解析为 23 个属性输入模型
- 预训练逻辑回归模型输出 CT/T 回合胜率概率
- 训练数据为 122,411 条高水平锦标赛快照
- 附带 GUI 动态预测条与命令行参数（延迟、禁用欢迎信息等）

## 适用场景

- 观战 CS:GO 比赛时查看实时回合胜负概率
- 将预测结果写入文本文件供其他程序使用
- 通过 GUI 预测条可视化查看双方胜率变化

## 场景标签

 · 领域:电竞/体育预测分析

## 证据(README 行号)

> L48: ### ***CSGOPredictor is a python program that generates live round winner predictions of CS:GO Competitive matches.
> L61: 3. Finally, `MainApp.py` runs the pre-trained Logistic Regression model to generate probability prediction for roun

## 星数曲线

```mermaid
xychart-beta
    title "d-roho/CSGOPredictor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8664e3bdf7cc` · [字段定义](../../DATASET.md)*
