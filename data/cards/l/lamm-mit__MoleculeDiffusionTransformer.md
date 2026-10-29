# lamm-mit/MoleculeDiffusionTransformer

⭐ 23 · Jupyter Notebook · Apache-2.0 · 推送 2026-01-07 · [GitHub](https://github.com/lamm-mit/MoleculeDiffusionTransformer) · [官网](https://github.com/lamm-mit/MoleculeDiffusionTransformer) · 组织维护

**从分子属性生成新分子结构的扩散/Transformer 模型库**

面向分子设计的深度学习代码库：提供四类模型——前向扩散与前向 Transformer（从 SMILES 预测分子属性）、逆向扩散与自回归 Transformer（从目标属性生成 SMILES 分子结构，求解逆问题）。基于 QM9 数据集训练，提供 Dropbox 预训练权重下载与各模型的基本用法示例，另含 SMILES 绘制等工具函数。安装走 conda 环境加 pip install -e .，模型框架可改写用于其他序列数据的条件生成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四类模型覆盖属性预测（前向）与分子设计生成（逆向）
- 提供全部预训练权重下载（Dropbox 链接）
- 基于 QM9 数据集训练
- 附 SMILES 绘制等工具函数，架构可迁移到其他序列数据条件生成

## 适用场景

- 从目标分子属性出发生成新分子 SMILES 结构
- 由 SMILES 输入预测分子属性
- 复用扩散/Transformer 架构做其他序列数据的条件生成

## 场景标签

 · 领域:分子设计/生成模型

## 证据(README 行号)

> L37: 1. Forward diffusion model (predicts molecular properties from SMILES input)
> L39: 3. Generative inverse diffusion model (predicts molecular designs via SMILES codes from molecular properties input,

## 星数曲线

```mermaid
xychart-beta
    title "lamm-mit/MoleculeDiffusionTransformer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0e24fc669b13` · [字段定义](../../DATASET.md)*
