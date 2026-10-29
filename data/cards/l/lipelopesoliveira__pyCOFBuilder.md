# lipelopesoliveira/pyCOFBuilder

⭐ 67 · Python · MIT · 推送 2026-08-11 · [GitHub](https://github.com/lipelopesoliveira/pyCOFBuilder) · [官网](https://lipelopesoliveira.github.io/pyCOFBuilder/) · 个人维护

**按网状化学规则自动组装共价有机框架（COF）结构的 Python 包**

面向计算化学与材料科学研究者：基于指定构筑单元、拓扑与官能团，按 reticular approach 自动生成 COF 晶体结构，支持高通量批量构建。包内定义一套命名规则（构筑单元-网络-堆积），可从名称直接解读结构特征；底层使用 pymatgen 构建结构，输出支持 cif/xyz/vasp/qe 等 10 种格式。README 声明项目仍在开发中。以 pip 包、conda 环境文件及 Google Colab notebook 形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按构筑单元+拓扑+官能团自动组装 COF 结构
- 结构命名规则可从名称直接解读结构特征
- 输出支持 cif/xyz/vasp/qe 等 10 种结构文件格式
- 基于 pymatgen 构建，附论文（J. Chem. Inf. Model. 2024）

## 适用场景

- 高通量生成 COF 结构用于材料筛选与数据集构建
- 按命名规则快速指定并复现特定 COF 结构
- 为机器学习/材料信息学研究批量生成标注结构数据

## 场景标签

 · 领域:计算化学/材料科学

## 证据(README 行号)

> L15: **pyCOFBuilder** is a simple and powerful python package to automatically assembly COF structures with specifics bu
> L23: > In case you want to use pyCOFBuilder without installing it, you can use the Google Colab notebook available here.

## 星数曲线

```mermaid
xychart-beta
    title "lipelopesoliveira/pyCOFBuilder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-29 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `090f39ce2b1e` · [字段定义](../../DATASET.md)*
