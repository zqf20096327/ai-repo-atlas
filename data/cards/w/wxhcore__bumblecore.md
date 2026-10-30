# wxhcore/bumblecore

⭐ 72 · Python · Apache-2.0 · 推送 2026-08-24 · [GitHub](https://github.com/wxhcore/bumblecore) · 个人维护 · 中文 README

**从零实现的 LLM 训练框架，覆盖预训练到 SFT/DPO 全流程**

面向研究者、算法工程师与学习者的 LLM 训练框架，不依赖高层 Trainer 库，手动实现数据加载、分布式配置（DeepSpeed/ZeRO/混合精度）、前后向传播与推理生成（Top-p/Top-k、KV Cache）。内置受 Qwen2.5 启发的 Bumblebee 架构，提供 0.5B–72B 多档配置，兼容 Qwen、LLaMA 系列模型，支持预训练、持续预训练、指令微调、RLHF/DPO，含梯度累积/检查点等显存优化、LoRA 权重合并与 OpenAI 兼容的 Web 推理界面。要求 Linux 与 Python>=3.10。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无高层 Trainer 库的全手动训练循环（数据、分布式、loss、推理均自行实现）
- Bumblebee 自定义架构，0.5B–72B 多档参数配置
- Pretraining→SFT→DPO 三阶段完整流程与实验教程
- DeepSpeed 集成（ZeRO、混合精度）与 BumbleChat OpenAI 兼容推理界面

## 适用场景

- 验证新的模型架构设计或训练策略
- 对 Qwen/LLaMA 类模型做预训练、微调与偏好对齐
- 学习 LLM 训练底层实现细节

## 场景标签

`模型训练` `微调` `强化学习` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: A hands-on large language model training framework built from scratch, giving you complete control over every traini
> L47: - Supports full training pipeline: pretraining, continual pretraining, instruction fine-tuning, reinforcement learn

## 星数曲线

```mermaid
xychart-beta
    title "wxhcore/bumblecore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 71 --> 73
    line [72, 72]
```

2026-10-18 72 → 2026-10-30 72（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8053b6af6f9c` · [字段定义](../../DATASET.md)*
