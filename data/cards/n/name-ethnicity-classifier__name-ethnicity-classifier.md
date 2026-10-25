# name-ethnicity-classifier/name-ethnicity-classifier

⭐ 33 · Python · AGPL-3.0 · 推送 2026-09-06 · [GitHub](https://github.com/name-ethnicity-classifier/name-ethnicity-classifier) · [官网](https://pypi.org/project/n2e/) · 组织维护

**基于姓名预测族裔的 Python 包与 CLI 工具（n2e）**

name-ethnicity 研究项目提供的 Python 包 n2e，通过分析姓名的语言特征预测族裔/国籍，输出预测类别与置信度，可输出完整分布。提供 CLI（读取 CSV 姓名列，写出预测 CSV）与 Python API（predict_ethnicities）。内置多种模型配置（2 至 28 类，准确率 66.7%–99.3%），模型作为 GitHub release 资产首次使用时自动下载并缓存于 ~/.cache/n2e/。支持 GPU/CPU 设备选择，可在官网请求自定义模型或用配套仓库本地训练。定位用于研究者在教育、就业、医疗等场景检测潜在偏见。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CLI 与 Python API 两种使用方式，输入输出均为 CSV
- 8 种模型配置，覆盖 2 至 28 个族裔/国籍类别
- 模型自动下载并缓存于 ~/.cache/n2e/，可选 gpu/cpu 运行
- 支持完整概率分布输出（--distribution / get_distribution）

## 适用场景

- 批量为 CSV 中的姓名列预测族裔并导出结果
- 在社会科学研究中检测教育、就业等场景的潜在偏见
- 在 Python 程序中直接调用获取姓名族裔预测与置信度

## 场景标签

 · 领域:社会科学/机器学习

## 证据(README 行号)

> L6: Name-ethnicity classification is the process of using a person's name to predict their ethnicity. It involves analyz
> L8: This project contains a Python package and CLI tool called `n2e`.
> L39: The project was tested with **Python ≥ 3.10**. The following packages are installed and used as dependencies: ``Num

## 星数曲线

```mermaid
xychart-beta
    title "name-ethnicity-classifier/name-ethnicity-classifier 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-25 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `790f4b2cdeee` · [字段定义](../../DATASET.md)*
