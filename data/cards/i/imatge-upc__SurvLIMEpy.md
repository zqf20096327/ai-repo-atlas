# imatge-upc/SurvLIMEpy

⭐ 27 · Python · GPL-3.0 · 推送 2026-10-06 · [GitHub](https://github.com/imatge-upc/SurvLIMEpy) · 组织维护

**生存分析模型的局部可解释性 Python 库**

实现 SurvLIME 算法的 Python 包：对生存分析模型做局部模型无关解释（Local Interpretable Model-agnostic Explanation），面向使用 Cox 比例风险模型、Random Survival Forest、XGBoost AFT 生存回归（xgbse）、DeepHit、DeepSurv 等模型的研究者与开发者。兼容机制为：只要模型的 predict 函数输出长度 q≤m（唯一事件时间数）的向量即可被解释。通过 PyPI 以 pip install survlimepy 安装，内含 PBC、Lung、UDCA、Veterans 等数据集加载器，配套论文发表于 Expert Systems with Applications。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 SurvLIME 局部解释算法
- 兼容 sksurv/xgbse/pycox 中的多种生存模型
- 内置 PBC、Lung、UDCA、Veterans 数据集加载
- 模型兼容条件明确：predict 输出长度 q≤m 向量即可

## 适用场景

- 解释生存模型的单样本预测（特征贡献）
- 临床/时间到事件建模中对黑箱模型做局部可解释性分析
- 对比不同生存模型解释结果的科研工作

## 场景标签

 · 领域:机器学习可解释性/生存分析

## 证据(README 行号)

> L7: **SurvLIMEpy** implements SurvLIME algorithm (**Survival Local Interpretable Model-agnostic Explanation**), a local 
> L27: Our package can manage multiple types of survival models as long as the functionality that predicts is implemented 

## 星数曲线

```mermaid
xychart-beta
    title "imatge-upc/SurvLIMEpy 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-26 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `383486a82187` · [字段定义](../../DATASET.md)*
