# action-ai-institute/MABEL-dataset

⭐ 34 · MIT · 推送 2026-06-12 · [GitHub](https://github.com/action-ai-institute/MABEL-dataset) · 组织维护

**恶意软件分析基准数据集：400+ 家族的二进制静态特征**

面向机器学习与 AI 建模的恶意软件分析数据集，覆盖 400+ 恶意软件家族及其关联二进制样本，样本由 vx-underground 提供。数据以多个分片文件发布，需拼接为单一数据集使用。每条记录包含二进制元数据（多种哈希、文件类型、架构、熵值、PE 头信息）与来自反汇编代码深度检查的静态特征（助记符、函数调用、分支、中断、指令计数等）。关联论文发表于 ESORICS 2025 国际研讨会（动态异构学习集成用于恶意软件家族分类），要求使用者引用该出版物。当前为首次发布，后续将增加非特定家族的恶意软件语料分析。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 400+ 恶意软件家族的首次数据集发布
- 含二进制元数据特征：多算法哈希、ClamAV/YARA 扫描结果、熵值、PE 结构信息
- 含反汇编深度检查特征：函数调用计数、分支/中断/指令统计
- 数据分片需拼接为单一数据集使用

## 适用场景

- 训练与评测恶意软件家族分类模型
- 恶意软件检测研究的基准数据
- 二进制静态特征工程与分析研究

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Welcome to the MABEL malware analysis dataset release for machine learning and AI modeling.
> L5: This is our initial dataset release. There are multiple file segments in our initial dataset. These files should be 

## 星数曲线

```mermaid
xychart-beta
    title "action-ai-institute/MABEL-dataset 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-25 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fdf9ae4c6bb9` · [字段定义](../../DATASET.md)*
