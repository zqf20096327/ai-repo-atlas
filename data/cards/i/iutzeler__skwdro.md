# iutzeler/skwdro

⭐ 25 · Python · BSD-3-Clause · 推送 2026-03-12 · [GitHub](https://github.com/iutzeler/skwdro) · [官网](https://skwdro.readthedocs.io) · 组织维护

**Python 库：为 sklearn/PyTorch 模型提供 Wasserstein 分布鲁棒版本**

skwdro 是一个 Python 包，提供大量估计器的 WDRO（Wasserstein 分布鲁棒优化）版本：一方面扩展 scikit-learn 估计器（如线性回归、逻辑回归）并可作为 drop-in 替换，仅需额外指定不确定度半径 rho；另一方面为自定义 PyTorch 模块提供 wrapper 以构建自定义鲁棒模型与优化器。项目源于研究项目，发表于 JMLR，BSD 3-Clause 许可。安装支持 pip、uv、conda 与 hatch 开发模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供大范围估计器的 Wasserstein 分布鲁棒（WDRO）版本
- scikit-learn 接口：鲁棒估计器可 drop-in 替换原生估计器
- PyTorch 接口：支持自定义模型与优化器的 robustify 封装
- 研究项目产出，配套 JMLR 论文与 ReadTheDocs 文档

## 适用场景

- 把现有 sklearn 回归/分类模型换成不确定半径可控的鲁棒版本
- 为自定义 PyTorch 模块添加分布鲁棒训练能力
- 复现或研究 Wasserstein DRO 相关论文实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L52: ``skwdro`` is a Python package that offers **WDRO versions** for a large range of estimators, either by extending *
> L91: Robust estimators from ``skwdro`` can be used as drop-in replacements for ``scikit-learn`` estimators (they actuall

## 星数曲线

```mermaid
xychart-beta
    title "iutzeler/skwdro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `cd095dc369be` · [字段定义](../../DATASET.md)*
