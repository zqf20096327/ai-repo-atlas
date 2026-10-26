# kk7nc/RMDL

⭐ 427 · Python · GPL-3.0 · 推送 2026-04-22 · [GitHub](https://github.com/kk7nc/RMDL) · [官网](https://rmdl.readthedocs.io/) · 个人维护

**随机多模型深度学习集成分类库（DNN+CNN+RNN 集成）**

RMDL 是一个面向分类任务的 Python 集成深度学习库：并行训练多组随机结构的 DNN、CNN 与 RNN（LSTM 或 GRU）模型并合并结果，以减少人工挑选网络结构的工作量。提供 RMDL_Text 与 RMDL_Image 两类接口，支持文本、图像、视频与符号数据分类；文本路径使用 GloVe 预训练词向量。基于 TensorFlow/Keras 与 scikit-learn 构建，附带两篇 arXiv 论文，README 列出 MNIST、CIFAR-10、IMDB、Web of Science 等基准数据集。GPU 运行需 CUDA 8.0 与 cuDNN v6。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 并行集成 DNN、CNN、RNN 三类随机结构模型并合并结果
- 各模型层数与节点数在设定上下界内随机生成
- 提供文本（GloVe 嵌入）与图像两套分类接口
- 附两篇 arXiv 论文与多个基准数据集说明

## 适用场景

- 我不想手工调网络结构，直接做文本或图像分类
- 在多数据类型（文本/图像/符号）上跑集成深度学习基线
- 复现论文中的 MNIST/CIFAR-10/Web of Science 分类实验

## 场景标签

 · 领域:机器学习/数据挖掘

## 证据(README 行号)

> L10: A new ensemble, deep learning approach for classification. Deep
> L68: learning architectures. In short, RMDL trains multiple models of Deep Neural Network (DNN),

## 星数曲线

```mermaid
xychart-beta
    title "kk7nc/RMDL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 426 --> 428
    line [427, 427]
```

2026-10-18 427 → 2026-10-26 427（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `a11713433449` · [字段定义](../../DATASET.md)*
