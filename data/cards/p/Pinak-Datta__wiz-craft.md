# Pinak-Datta/wiz-craft

⭐ 16 · Python · MIT · 推送 2026-07-22 · [GitHub](https://github.com/Pinak-Datta/wiz-craft) · [官网](https://pypi.org/project/wiz-craft/) · 个人维护

**面向初学者的 CSV 数据预处理 CLI 工具，可审计并生成可复用清洗配方**

基于命令行的数据预处理工具：通过交互式 CLI 或命令对 CSV 文件执行统计查看、空值填补（均值/中位数/众数/KNN）、one-hot 编码、数值归一化/标准化，并保存修改后的数据集。`wizcraft doctor` 子命令在建模前审计数据质量问题（缺失值、重复行、ID 列、文本列、离群值、目标不平衡、疑似目标泄漏等），推断建模任务类型，报告可导出为 JSON/HTML/Markdown。清洗步骤可存为 recipe.json 在其他 CSV 上重放。基于 pandas 与 scikit-learn 构建，从 PyPI 以 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Dataset Doctor 审计 13 类建模前数据质量问题并建议清洗配方
- 交互式预处理：空值填补、one-hot 编码、归一化/标准化
- 预处理步骤保存为 recipe.json，可在后续 CSV 上重放
- 报告支持终端、JSON、HTML、Markdown 四种输出格式

## 适用场景

- 建模前快速检查 CSV 数据质量并发现泄漏或不平衡问题
- 把清洗流程固化为配方，在新的数据文件上重复应用
- 作为 ML 入学者用示例数据集练习预处理步骤

## 场景标签

 · 领域:数据科学/机器学习数据准备

## 证据(README 行号)

> L14: WizCraft is a beginner-friendly CLI that audits messy CSV files, explains what needs attention, and creates repeata
> L19: - Spot missing values, IDs, text-heavy columns, date columns, outliers, duplicates, leakage risks, and target imbal
> L45: - Normalize and standardize numerical features for better model performance.

## 星数曲线

```mermaid
xychart-beta
    title "Pinak-Datta/wiz-craft 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e1641e770671` · [字段定义](../../DATASET.md)*
