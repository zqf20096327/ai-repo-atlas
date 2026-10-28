# kieranmrhunt/teaching-notebooks

⭐ 21 · Jupyter Notebook · 推送 2026-10-05 · [GitHub](https://github.com/kieranmrhunt/teaching-notebooks) · 组织维护

**气象学与机器学习教学的可运行 Jupyter 笔记本集**

由雷丁大学气象系 Kieran Hunt 维护的教学笔记本仓库：包含从数学原理构建类 XGBoost 学习器并演示梯度、正则化、约束、SHAP 等概念的引导式笔记本，以及复现 Jin 系列延迟记忆 ENSO 振子实验的非线性随机振荡器笔记本（含诊断评分卡、机制消融、50,000 年极端事件控制）。笔记本可在 GitHub 或 Google Colab 打开，本地运行通过 requirements.txt 安装完整教学环境后用 Jupyter Lab 执行，数据在笔记本内生成或存于 data/ 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从数学原理构建 XGBoost 类学习器并覆盖正则化/约束/SHAP/防泄漏验证
- 复现 Jin 系列延迟记忆 ENSO 实验，含 50,000 年极端事件控制
- 支持 Google Colab 启动与本地 venv + Jupyter Lab 运行
- ENSO 环境可用 MODE=quick 做短时冒烟测试

## 适用场景

- 教学场景中讲解梯度提升的数学原理与气象数据应用
- 复现与学习 ENSO 延迟记忆振荡器实验
- 学生学习时间感知验证与特征重要性分析

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: Runnable notebooks for teaching meteorology, machine learning, and data science.
> L9: This guided notebook builds a compact XGBoost-like learner from the mathematics upwards, then uses simulated weather
> L25: This notebook reproduces the Jin, Jin++, and Jin++ delayed-memory ENSO experiments, including the diagnostic scorec

## 星数曲线

```mermaid
xychart-beta
    title "kieranmrhunt/teaching-notebooks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6dcab5a0dd79` · [字段定义](../../DATASET.md)*
