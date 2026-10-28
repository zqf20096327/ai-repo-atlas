# OML-Team/open-metric-learning

⭐ 998 · Python · Apache-2.0 · 推送 2025-11-26 · [GitHub](https://github.com/OML-Team/open-metric-learning) · [官网](https://open-metric-learning.readthedocs.io/en/latest/index.html) · 组织维护 · 中文 README

**PyTorch 度量学习框架：训练嵌入模型并构建检索流水线**

基于 PyTorch 的度量学习与检索框架，面向需要图像/NLP/音频嵌入的训练与检索场景。提供配置驱动的 Pipelines、损失函数、Miner、Sampler、检索指标计算与后处理（重排序、自适应阈值），并内置可如 torchvision 方式调用的预训练模型 Zoo。集成 PyTorch Lightning 支持多卡 DDP，同时保留纯 PyTorch 用法；不直接支持导出 ONNX。以 pip 包分发，含最小依赖与 nlp/audio 等可选安装项。

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

- 配置驱动的训练与验证 Pipelines，仅需准备 .csv 格式数据
- 预训练模型 Zoo（多模态），代码内直接加载
- Category Balance Sampler、Hard Triplets Miner 等采样与挖掘组件
- 检索后处理：PairwiseReranker、AdaptiveThresholding，及多种检索指标

## 适用场景

- 训练用于图像检索/行人重识别/人脸识别的嵌入模型
- 在数千类别、每类少量样本的数据上做检索验证
- 用预训练模型直接构建相似度搜索系统

## 场景标签

`模型训练` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L8: OML is a PyTorch-based framework to train and validate the models producing high-quality embeddings.
> L100: Here are a few examples of such tasks from the computer vision sphere:

## 星数曲线

```mermaid
xychart-beta
    title "OML-Team/open-metric-learning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 997 --> 999
    line [998, 998]
```

2026-10-18 998 → 2026-10-28 998（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `642853ec3b11` · [字段定义](../../DATASET.md)*
