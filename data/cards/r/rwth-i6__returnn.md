# rwth-i6/returnn

⭐ 377 · Python · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/rwth-i6/returnn) · [官网](http://returnn.readthedocs.io/) · 组织维护

**RWTH 大学的循环神经网络训练框架，面向 ASR/MT 研究**

基于 PyTorch/TensorFlow 的循环神经网络训练框架，针对多 GPU 环境下快速可靠的 RNN 训练优化。特性包括序列分块批训练、LSTM（含自研 CUDA kernel）、多维 LSTM（仅 GPU）、大数据集内存管理、多设备任务分布，以及各类 encoder-attention-decoder 模型。面向科研与生产场景（解码速度面向生产），提供 ASR/MT 实验示例与文档。要求 Python>=3.8，TensorFlow 方案需 TF>=2.2，PyTorch 方案需 Torch>=1.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 PyTorch/TensorFlow 双后端的 RNN 训练框架
- LSTM 自研 CUDA kernel，多维 LSTM 仅支持 GPU
- 序列分块批训练与多设备任务分布
- 支持各类 encoder-attention-decoder 模型

## 适用场景

- 在多 GPU 环境下训练语音识别/机器翻译模型
- 搭建和复现 ASR 实验（如 Switchboard、LibriSpeech）
- 研究自定义循环神经网络架构

## 场景标签

`科研工具` `语音识别` `模型训练` · 领域:学习与行业

## 证据(README 行号)

> L7: RETURNN - RWTH extensible training framework for universal recurrent neural networks,
> L9: It is optimized for fast and reliable training of recurrent neural networks in a multi-GPU environment.

## 星数曲线

```mermaid
xychart-beta
    title "rwth-i6/returnn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 376 --> 378
    line [377, 377]
```

2026-10-18 377 → 2026-10-28 377（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `6fc35058214c` · [字段定义](../../DATASET.md)*
