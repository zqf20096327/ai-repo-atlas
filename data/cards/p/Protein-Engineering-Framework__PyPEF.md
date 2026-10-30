# Protein-Engineering-Framework/PyPEF

⭐ 26 · Python · NOASSERTION · 推送 2026-09-06 · [GitHub](https://github.com/Protein-Engineering-Framework/PyPEF) · 个人维护

**面向蛋白质工程的序列机器学习框架：从序列预测蛋白质适应度**

Python 3 编写的蛋白质工程命令行框架，读取 FASTA 野生型序列与 CSV 变体-适应度数据，用 One-hot、AAindex 描述符、DCA 共进化编码及 ESM/ProSST 蛋白质语言模型嵌入训练回归模型（PLS/Ridge/SVR/RF/MLP 等）预测变体适应度；支持 DCA+PLM 混合建模、少样本微调、差分进化优化集成权重、LoRA 微调与高斯过程嵌入优化，并提供虚拟定向进化（Metropolis-Hastings）与变体重组预测集生成。面向计算生物学/蛋白质设计研究者的科研工具，通过 pip 或 Docker 安装，可选 GUI；GPU 为可选加速，PLM 微调需较高显存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多种序列编码（One-hot/AAindex/DCA/PLM 嵌入）配合 7 种回归模型预测适应度
- DCA+多 PLM 混合建模，支持 LoRA 微调与高斯过程嵌入优化（Kermut 复合核方法）
- Metropolis-Hastings 虚拟定向进化与双/三/四位点重组预测集系统生成
- 提供 CLI、可选 GUI、Docker 镜像与 Jupyter notebook 教程

## 适用场景

- 用已有变体-适应度数据训练模型，预测未测变体的适应度
- 通过虚拟定向进化或重组预测集寻找高适应度蛋白变体
- 组合 DCA 与 ESM/ProSST 嵌入做混合建模与少样本微调

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L15: a framework written in Python 3 for performing sequence-based machine learning-assisted protein engineering to pred
> L24: When incorporating DCA and PLM features, both models are fine-tuned via few-shot learning on a subset of the traini

## 星数曲线

```mermaid
xychart-beta
    title "Protein-Engineering-Framework/PyPEF 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `609db6fc2a5d` · [字段定义](../../DATASET.md)*
