# gerritnowald/budget_book

⭐ 49 · Jupyter Notebook · MIT · 推送 2026-06-09 · [GitHub](https://github.com/gerritnowald/budget_book) · [官网](https://gerritnowald.wordpress.com/2023/02/23/managing-spending-with-python-pandas/) · 个人维护

**银行流水记账分析工具：自动下载并用机器学习分类交易**

本地 CSV 数据库形式管理银行流水的 Python 脚本集：transaction_importer 通过德国 comdirect 银行 API（或 CSV 导入）下载新交易并入数据库，基于描述文本用 sklearn 训练的模型自动分类（两层类别结构）；transaction_editor 提供控制台界面修正分类与拆分交易；分析在 Jupyter notebook 中完成（plotly 旭日图等）。需自行在 config.ini 配置并训练自己的分类模型，作者声明其非易用产品、需编程知识，原则上适用于所有可导出 CSV 流水的银行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- comdirect API 自动下载新交易并入 CSV 数据库
- 基于描述文本的 sklearn 机器学习自动分类（两层类别）
- 控制台界面修正分类与拆分交易
- Jupyter notebook 生成分期消费报告

## 适用场景

- 替代已停用的 comdirect Finanzmanager 管理个人流水
- 自动分类消费记录并按时间段分析支出
- 从任意可导出 CSV 的银行流水建立本地记账数据库

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L6: - `transaction_importer` downloads new transactions using the *comdirect bank* API and appends them to the database.
> L50: Use `categorizer_training.ipynb` to train a machine learning model on your transactions with your categories, see a
> L118: - sklearn (for ML categorization)

## 星数曲线

```mermaid
xychart-beta
    title "gerritnowald/budget_book 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-29"]
    y-axis "stars" 47 --> 50
    line [48, 49, 49]
```

2026-10-18 48 → 2026-10-29 49（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `11c8e9c6a58d` · [字段定义](../../DATASET.md)*
