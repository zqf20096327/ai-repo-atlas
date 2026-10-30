# DaoyuanLi2816/molgen

⭐ 16 · Python · MIT · 推送 2026-07-11 · [GitHub](https://github.com/DaoyuanLi2816/molgen) · [官网](https://pypi.org/project/molgen/) · 个人维护

**给药物发现研究者的轻量级 de novo 分子生成工具包**

基于深度序列模型的分子生成工具包：提供原子级 SMILES 与 SELFIES 分词器、Transformer β-TC-VAE / CharRNN / MolGPT 三种生成模型，支持混合精度训练（CUDA AMP）、温度/top-k/top-p 采样，以及 MOSES 风格评估（有效性、独特性、新颖性、骨架、QED/logP 等）。VAE 支持潜空间插值与邻近采样，并可通过微调向目标性质（如药物相似度 QED）双向调控生成。规模小到单 GPU 数分钟可训练。以 Python 库与 CLI 形式提供，PyPI 可安装；VAE 命令需 0.2.0+，当前 PyPI 版本为 0.1.1，需从源码安装使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SMILES 与 SELFIES 双分词器（SELFIES 模式保证解码分子语法有效）
- CharRNN / MolGPT / Transformer β-TC-VAE 三种生成架构，统一 trainer/sampler
- MOSES 风格评估套件（validity/uniqueness/novelty/骨架/性质摘要）
- 目标导向生成：微调单个基模型可双向调控 QED 分布

## 适用场景

- 在 MOSES/QM9/ZINC 数据集上训练并采样生成新分子
- 通过 VAE 潜空间进行分子插值与邻近分子探索
- 向高（或低）药物相似度方向调控生成分子

## 场景标签

 · 领域:计算化学/药物发现

## 证据(README 行号)

> L1: molgen — lightweight de novo molecular generation: SMILES and SELFIES tokenizers, Transformer β-TC-VAE / CharRNN / M
> L21: - **Models** — a Transformer β-TC-VAE, a GRU/LSTM `CharRNN`, and a
> L27: - **Metrics** — validity, uniqueness, novelty, internal diversity, unique

## 星数曲线

```mermaid
xychart-beta
    title "DaoyuanLi2816/molgen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b8cda0b95170` · [字段定义](../../DATASET.md)*
