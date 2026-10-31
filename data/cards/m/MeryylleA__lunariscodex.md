# MeryylleA/lunariscodex

⭐ 14 · Python · MIT · 推送 2026-01-30 · [GitHub](https://github.com/MeryylleA/lunariscodex) · [官网](https://huggingface.co/meryyllebr543) · 个人维护

**给研究/开发者的 Llama 风格语言模型预训练 PyTorch 工具包**

基于 nanoGPT 改造的从零预训练工具包，实现 Llama 风格架构：RMSNorm、NTK-aware RoPE、GQA、可选 QK-Norm、SwiGLU、绑定词嵌入等。训练脚本 train.py 通过 torchrun 启动，支持 DDP 多卡多节点、bfloat16/fp16 混合精度、torch.compile、SDPA/Flash Attention、梯度累积与裁剪、断点自动恢复及 W&B 监控。数据准备由用户自行完成：训练 BPE 分词器并将语料切分为 uint16 的 .npy 分片。以 git clone 源码方式使用，配置经 train_config.yaml 定义。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Llama 风格架构：RMSNorm、NTK-aware RoPE、GQA、SwiGLU、QK-Norm（可选）
- DDP 多 GPU/多节点训练、bfloat16/fp16、torch.compile、SDPA 自动调用 Flash Attention
- 内存映射 ShardDataset 流式读取大规模 .npy 数据分片
- 断点自动恢复与完整训练状态保存，集成 W&B 监控

## 适用场景

- 用自己的数据集从零预训练一个基础语言模型
- 研究现代 transformer 架构组件（RoPE 缩放、QK-Norm、GQA）的训练效果
- 需要可长期运行、可断点续训的大规模训练流水线

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L11: **Lunaris Codex** is a streamlined, high-performance toolkit for pre-training powerful language models from scratch
> L83: ### Phase 2: Model Training (Our Speciality)

## 星数曲线

```mermaid
xychart-beta
    title "MeryylleA/lunariscodex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6f4511cc14e5` · [字段定义](../../DATASET.md)*
