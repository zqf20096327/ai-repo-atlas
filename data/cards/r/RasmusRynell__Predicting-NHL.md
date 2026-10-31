# RasmusRynell/Predicting-NHL

⭐ 14 · Python · MIT · 推送 2026-06-16 · [GitHub](https://github.com/RasmusRynell/Predicting-NHL) · 个人维护

**用机器学习预测 NHL 冰球比赛射正数的个人研究项目**

Python 编写的体育数据分析项目：从 NHL 官方免费数据库拉取比赛数据存入本地 sqlite 数据库，结合约 5000 条来自博彩网站的射正数（Shots on goal）赔率，生成含球员、所属球队与对手球队统计的 CSV 文件，用逻辑回归、SVM、高斯朴素贝叶斯、随机树/森林及简单神经网络等 ML 技术做预测，并与博彩公司赔率对比评估。以终端命令方式运行（help/und/gen/pre 等命令），README 多处标注 Under construction，功能仍在建设中。安装方式为 git clone 源码 + venv + pip 依赖，需 Python 3.9 以上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 从 NHL 官方数据库拉取数据并存入本地 sqlite 数据库
- 数据库含约 5000 条来自多家博彩网站的射正数赔率
- 生成包含球员与双方球队统计的预测数据 CSV
- 已测试逻辑回归、SVM、朴素贝叶斯、随机森林及简单神经网络

## 适用场景

- 研究机器学习方法在冰球比赛统计预测中的应用
- 对比自建模型预测与博彩公司赔率的表现
- 学习体育数据的采集、存储与预处理流程

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L4: This project explores the idea of using different machine learning techniques to determine different stats in NHL ga
> L32: While working on the project a fair bit of different techniques has been tested, these include:

## 星数曲线

```mermaid
xychart-beta
    title "RasmusRynell/Predicting-NHL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `0f5ceffbb0a6` · [字段定义](../../DATASET.md)*
