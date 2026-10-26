# xRiskLab/pearsonify

⭐ 26 · Python · MIT · 推送 2026-02-20 · [GitHub](https://github.com/xRiskLab/pearsonify) · 组织维护

**二分类预测概率的置信区间生成库：Pearson 残差+保形预测**

轻量级 Python 包，围绕二分类预测概率生成分类区间（如 95% 置信区间）。方法上基于 Pearson 残差与保形预测（conformal prediction）原理，在无强分布假设下量化不确定性；模型无关，可与任何输出概率估计的模型（如 sklearn SVC）配合使用。依赖精简，通过 pip 从 PyPI 或 GitHub 安装，附示例脚本可生成带区间的可视化图。面向需要在分类任务中量化预测不确定性的开发者与科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Pearson 残差与保形预测生成分类区间
- 模型无关：兼容任何输出概率估计的模型
- 不依赖强分布假设，最小化依赖库
- 附示例脚本生成带 95% 置信区间的可视化

## 适用场景

- 给二分类模型的预测概率附上不确定性区间
- 科研或风控场景中量化分类预测的置信水平
- 集成进现有 sklearn 工作流做保形区间校准

## 场景标签

 · 领域:机器学习/统计

## 证据(README 行号)

> L4: **Pearsonify** is a lightweight 🐍 Python package for generating **classification intervals** around predicted probab
> L6: It uses **Pearson residuals** and **principles of conformal prediction** to quantify uncertainty without making stro

## 星数曲线

```mermaid
xychart-beta
    title "xRiskLab/pearsonify 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-26 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `09088f6551e9` · [字段定义](../../DATASET.md)*
