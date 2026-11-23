# abdallah-swe/layerpool

⭐ 3 · Python · MIT · 推送 2026-11-22 · [GitHub](https://github.com/abdallah-swe/layerpool) · [官网](https://pypi.org/project/layerpool/) · 个人维护

**把多台设备的显存合并，分层拆分训练大模型**

layerpool 将一个模型按层拆分到多台设备（笔记本、台式机、云 GPU、Colab/Kaggle 笔记本）上合并训练：本机保留 embeddings 与输出头并运行训练代码，各设备按内存与实测速度分配连续层，激活前向传递、梯度反向回传。设备掉线时其余设备从检查点接管其层，训练不丢失。兼容 transformers Trainer 与 TRL，支持 LoRA/QLoRA/全参/DPO 等，提供仪表盘、cloudflared 隧道联网与自动再平衡。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按层将模型拆分到任意数量、异构混合的设备（NVIDIA/AMD GPU、Apple Silicon、CPU）
- 设备掉线后其余设备从检查点接管层并重做丢失步骤
- 支持 LoRA、QLoRA、全参微调、DPO/KTO/IPO/SimPO/ORPO、策略梯度
- 接入 Colab/Kaggle 免费 GPU 作为池中设备

## 适用场景

- 用家里多台电脑的闲置显存微调 14B 级别模型
- 把 Colab/Kaggle 免费 GPU 加入训练池
- 不改训练脚本代码地扩大可训练模型规模

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L7: One model, split by layers across all your machines. Their memory is pooled, and they train it as one.
> L38: - **Any hardware, mixed.** NVIDIA GPUs, Apple Silicon (with MLX or PyTorch) and plain CPUs, on Linux, Windows and m
> L50: - **Every kind of training.** LoRA, QLoRA, full fine-tuning, training from scratch, DPO, KTO and other preference m


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `62a270596f20` · [字段定义](../../DATASET.md)*
