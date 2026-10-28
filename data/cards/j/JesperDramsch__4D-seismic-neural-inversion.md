# JesperDramsch/4D-seismic-neural-inversion

⭐ 31 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/JesperDramsch/4D-seismic-neural-inversion) · 个人维护

**复现 4D 地震压力-饱和度反演深度网络论文结果的代码库**

复现两篇 2019 年出版物（EAGE Workshop 论文与 arXiv:1904.02254）的代码仓库，主题为基于深度神经网络的地图式 4D 地震压力-饱和度反演，并与北海数据的贝叶斯反演进行对比。网络架构在输入数据中引入基础物理（AVO）以学习含噪梯度并学习残差，属于物理信息机器学习方向。README 仅描述架构与结果，未给出安装或运行说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 复现 EAGE 2019 与 arXiv:1904.02254 论文结果
- AVO 物理信息深度神经网络架构
- 在输入中引入 AVO 物理以学习含噪梯度与残差

## 适用场景

- 复现或验证 4D 地震压力-饱和度反演论文结果
- 研究物理信息（AVO）深度学习在地球物理反演中的应用

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository reproduces the results in the following publications:
> L10: The network architecture includes basic physics (AVO) on the input data to learn noisy gradients and learn the resi

## 星数曲线

```mermaid
xychart-beta
    title "JesperDramsch/4D-seismic-neural-inversion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `5434d8f21e41` · [字段定义](../../DATASET.md)*
