# wengroup/matten

⭐ 45 · Python · 推送 2026-05-28 · [GitHub](https://github.com/wengroup/matten) · [官网](https://doi.org/10.1039/D3DD00233K) · 组织维护

**等变图神经网络模型，预测晶体的弹性张量等张量性质**

MatTen 是基于 e3nn 构建的等变图神经网络，用于预测晶体材料的张量性质（如弹性张量），覆盖全部七种晶系。用户可通过 Python API 加载预训练模型对 pymatgen Structure 对象做预测，也可用自有数据训练模型。安装依赖 PyTorch>=2.0.0，采用 git clone 后 pip install -e 的源码安装方式。仓库附带 100 个晶体示例数据，完整数据集发布于 Zenodo。相关论文发表于 Digital Discovery（2024）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 e3nn 的等变图神经网络，覆盖七种晶系的弹性张量预测
- predict 接口对 pymatgen Structure（含列表）直接返回弹性张量
- 支持用自有数据训练模型，附 100 晶体示例数据与 Zenodo 完整数据集
- 提供论文与 Bibtex 引用（Digital Discovery 2024）

## 适用场景

- 对晶体结构预测弹性张量，免去昂贵的第一性原理计算
- 用自己的晶体数据训练弹性预测模型
- 材料力学性质筛选与数据集构建研究

## 场景标签

 · 领域:材料科学/机器学习

## 证据(README 行号)

> L3: This repo contains the Materials Tensor (MatTen) model for predicting tensorial
> L6: MatTen is an equivariant graph neural network built using e3nn.

## 星数曲线

```mermaid
xychart-beta
    title "wengroup/matten 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-28 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `298caa629e9e` · [字段定义](../../DATASET.md)*
