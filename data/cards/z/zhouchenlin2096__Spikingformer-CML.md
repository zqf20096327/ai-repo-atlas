# zhouchenlin2096/Spikingformer-CML

⭐ 49 · Python · Apache-2.0 · 推送 2026-04-16 · [GitHub](https://github.com/zhouchenlin2096/Spikingformer-CML) · 组织维护

**脉冲 Transformer 的 CML 下采样研究代码：SNN 图像识别训练与测试**

论文《Enhancing the Performance of Transformer-based Spiking Neural Networks by SNN-optimized Downsampling with Precise Gradient Backpropagation》（Arxiv 2023，后续发表于 Frontiers in Neuroscience 2024）的官方实现：在 Spikformer/Spikingformer 基础上引入 CML 下采样模块进行直接训练的脉冲神经网络图像与事件数据分类。提供 ImageNet-1K、CIFAR10/100、CIFAR10-DVS、DVS128 Gesture 上的训练/测试脚本与已训练模型下载（含 Google Drive 链接）。依赖 timm、cupy、torch、spikingjelly，通过 YAML 配置超参数，ImageNet 训练使用 torch.distributed.launch 多卡启动。

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

- CML 模块结合 Spikformer/Spikingformer 的直接训练 SNN 实现
- 覆盖 ImageNet-1K、CIFAR10/100、CIFAR10-DVS、DVS128 五类数据集的训练与测试脚本
- 提供已训练模型下载（Google Drive，提取码 abcd）
- ImageNet 训练支持 torch.distributed.launch 分布式启动

## 适用场景

- 复现论文中各数据集上的 SNN 分类结果
- 在自有数据集上训练基于 CML 的脉冲 Transformer
- 下载已训练模型进行推理或下游分析

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L1: # Enhancing the Performance of Transformer-based Spiking Neural Networks by SNN-optimized Downsampling with Precise 
> L3: Our CML models achieve the state-of-the-art performance on several datasets (eg. **77.64 %** on ImageNet, **96.04 %*
> L61: ## Requirements

## 星数曲线

```mermaid
xychart-beta
    title "zhouchenlin2096/Spikingformer-CML 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-29 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b5a919994bba` · [字段定义](../../DATASET.md)*
