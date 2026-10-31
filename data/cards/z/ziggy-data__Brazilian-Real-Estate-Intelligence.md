# ziggy-data/Brazilian-Real-Estate-Intelligence

⭐ 40 · Python · 推送 2026-04-19 · [GitHub](https://github.com/ziggy-data/Brazilian-Real-Estate-Intelligence) · 个人维护

**巴西 Zap 房产网站爬取、ETL 与房价线性回归分析项目**

个人数据科学项目：以 Jupyter notebook 对巴西 Zap-Imoveis 房产网站做 web scraping（400 页、含 URL 异常处理、RegEx 从描述提取信息），产出 4 个 CSV 数据集（共约 3.2 万条房产记录，数据采集于 2022-02-12），并用 scikit-learn 线性回归在里约房屋数据集上建模，模型报告 43% 的价格预测准确率；另提供两个 Power BI 嵌入式仪表盘链接，展示每平方米价格等指标。面向学习与展示用途，无安装命令或打包交付。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 爬取 400 页并含 URL/站点不可达的异常处理，3 种备用链接
- 4 个 CSV 数据集：巴西全国房屋/公寓、里约房屋等样本
- RegEx 从房源描述中提取信息
- 线性回归模型报告 43% 价格预测准确率

## 适用场景

- 获取巴西房产市场的结构化数据样本做分析
- 学习 web scraping、ETL 与线性回归建模的组合流程
- 在 Power BI 仪表盘中查看里约房产每平米价格等指标

## 场景标签

`网页抓取` `数据分析` `教程课程` · 领域:效率与自动化

## 证据(README 行号)

> L24: Neste notebook estou aplicando tecnicas de regressão linear com o dataset: `dataset-casas-rj.csv`
> L26: O modelo apresentou um acerto de 43% em relação ao preços dos imóveis considerando todas as variáveis numéricas pre

## 星数曲线

```mermaid
xychart-beta
    title "ziggy-data/Brazilian-Real-Estate-Intelligence 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-31 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4236ba5c2cf1` · [字段定义](../../DATASET.md)*
