# berksudan/GCN-Text-Classification

⭐ 26 · Python · MIT · 推送 2026-07-08 · [GitHub](https://github.com/berksudan/GCN-Text-Classification) · 组织维护

**用 GCN/GAT 做文本分类的 PyTorch 实验项目，含 8 个数据集**

Inzva AI Projects #4 的实验代码库：以图卷积网络（GCN）与图注意力网络（GAT）结合 NLP 技术处理文本分类问题。支持 20ng、R8、R52、ohsumed、mr、cora、citeseer、pubmed 共 8 个数据集，流程分两步：preprocess.py 预处理、train.py 训练，通过 build.sh 创建虚拟环境并安装依赖。README 声明仅适用于 Linux 发行版，需联网下载依赖。参考实现来自 pyGAT 与 pygcn。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GCN/GAT 用于文本分类的 PyTorch 实现
- 内置 8 个可用数据集（新闻/医学摘要/影评/引文）
- build.sh 一键创建虚拟环境并安装依赖
- 提供 preprocess 与 train 两步运行命令及示例输出

## 适用场景

- 在标准数据集上复现 GCN/GAT 文本分类结果
- 学习图神经网络在 NLP 分类任务中的用法
- 对比不同数据集上的图模型训练表现

## 场景标签

 · 领域:NLP/图神经网络

## 证据(README 行号)

> L6: Our project aims to tackle text classification problem with novel approaches Graph Convolutional Networks and Graph 
> L33: ```bash

## 星数曲线

```mermaid
xychart-beta
    title "berksudan/GCN-Text-Classification 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-29 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `15c907342357` · [字段定义](../../DATASET.md)*
