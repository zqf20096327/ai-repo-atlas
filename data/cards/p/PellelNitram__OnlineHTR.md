# PellelNitram/OnlineHTR

⭐ 30 · Jupyter Notebook · MIT · 推送 2026-06-11 · [GitHub](https://github.com/PellelNitram/OnlineHTR) · [官网](http://lellep.xyz/blog/online-htr.html?utm_campaign=github) · 个人维护

**PyTorch 实现的在线手写文本识别模型，预测手写内容**

基于 Carbune 等（2020）论文 'Fast multi-language LSTM-based online handwriting recognition' 的 PyTorch 复现，输入在线手写笔迹（stroke 序列），输出文本预测。使用 PyTorch Lightning 与 Hydra 框架构建，提供预训练模型权重（IAM-OnDB 训练，特征为 dx/dy/dt/n 通道）与训练脚本。用户可通过脚本在画板上书写并实时预测，或下载 IAM On-Line Handwriting Database 从零训练。属作者为 Xournal++ 构建手写识别系统的一部分。安装走 conda + pip 路线。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 LSTM 的在线手写文本识别模型 PyTorch 实现
- 提供 IAM-OnDB 训练的预训练权重与从零训练脚本
- draw_and_predict_sample 脚本支持对自己手写内容做推理
- 基于 PyTorch Lightning 与 Hydra 模板构建

## 适用场景

- 在手写笔记场景中将自己的笔迹识别为文本
- 复现论文并使用 IAM-OnDB 数据集从零训练模型
- 为 Xournal++ 等手写软件集成手写识别能力

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L18: In this repository I provide a clean PyTorch model implementation of the paper "Fast multi-language LSTM-based onli
> L20: This model lets you predict handwritten text as shown in the project demo below.

## 星数曲线

```mermaid
xychart-beta
    title "PellelNitram/OnlineHTR 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-31 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b175967805c9` · [字段定义](../../DATASET.md)*
