# safe-graph/GNN-FakeNews

⭐ 556 · Python · Apache-2.0 · 推送 2025-12-11 · [GitHub](https://github.com/safe-graph/GNN-FakeNews) · 组织维护

**GNN 假新闻检测模型集合与 UPFD 数据集基准**

提供一系列基于图神经网络（GNN）的假新闻检测模型的 PyTorch-Geometric 实现，统一在 UPFD（用户偏好感知假新闻检测）框架下以图分类任务形式实现与评估。收录 GNN-CL、GCNFN、BiGCN、UPFD-GCN/GAT/SAGE 六个模型，配套从 Politifact 与 Gossipcop 事实核查信息构建的 Twitter 新闻传播图数据集（含 BERT/spaCy/profile/content 四类节点特征），数据集已集成进 PyG 与 DGL 官方库。可本地手动安装运行，也可在 Code Ocean 上复现。

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

- 六个 GNN 假新闻检测模型实现（GNN-CL/GCNFN/BiGCN/UPFD-GCN/GAT/SAGE）
- UPFD 数据集：Politifact 314 图、Gossipcop 5464 图，已集成 PyG 与 DGL 官方库
- 四种节点特征：bert(768维)、spacy(300维)、profile(10维)、content(310维)
- 支持 Code Ocean 在线复现与 PaperWithCode 基准跟踪

## 适用场景

- 研究人员对比不同 GNN 模型在假新闻检测上的表现
- 用 UPFD 数据集训练与评测自己的图分类模型
- 复现 SIGIR'21 UPFD 论文实验结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L6: This repo includes the Pytorch-Geometric implementation of a series of Graph Neural Network (GNN) based fake news de
> L7: All GNN models are implemented and evaluated under the User Preference-aware Fake News Detection (UPFD) framework.
> L8: The fake news detection problem is instantiated as a graph classification task under the UPFD framework.

## 星数曲线

```mermaid
xychart-beta
    title "safe-graph/GNN-FakeNews 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 555 --> 557
    line [556, 556]
```

2026-10-18 556 → 2026-10-24 556（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `1642d1374fe4` · [字段定义](../../DATASET.md)*
