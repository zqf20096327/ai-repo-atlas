# maolonchen/antiForget-dk-sft

⭐ 14 · Python · MIT · 推送 2026-05-12 · [GitHub](https://github.com/maolonchen/antiForget-dk-sft) · 个人维护

**通过块扩展与分布锚定防止 LLM 微调灾难性遗忘的训练代码**

面向 LLM 微调的研究代码库：在预训练模型中插入恒等映射块（Block Expansion）增加容量，并在每个插入点用局部 KL 散度（输出空间）与 MSE 特征蒸馏（隐藏空间）将块的输出分布锚定到输入分布，以任务损失+两项蒸馏损失联合训练，防止冻结层原有能力被级联破坏。支持 Qwen3 系列（0.6B/32B 示例），提供 5 种插入策略、4 种 JSONL 数据格式混用、bfloat16 训练与梯度检查点；仅加载单一模型，Qwen3-0.6B 扩展训练估算约 5GB 显存，更大模型需 DeepSpeed ZeRO 或 FSDP。

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

- 每个恒等块插入点的局部 KL + MSE 双空间分布锚定
- 5 种块插入策略（second_half/every_layer/every_n/first_half/custom）
- 单文件混用 messages/text/instruction-output/thinking 四种 JSONL 格式
- 仅训练恒等块参数，Qwen3-0.6B 约 5GB 显存，支持 DeepSpeed/FSDP 扩展

## 适用场景

- 在保持 Qwen3 原有能力的前提下做领域 SFT
- 研究块扩展插入策略与蒸馏超参对遗忘的影响
- 用扩展后模型直接推理对话（chat.py --think）

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: **Anti-Catastrophic Forgetting via Local Distributional Anchoring at Identity Blocks**
> L176: python scripts/train.py \
> L184: from sft_distill_mil import BlockExpansionWrapper

## 星数曲线

```mermaid
xychart-beta
    title "maolonchen/antiForget-dk-sft 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6360c15dc3e8` · [字段定义](../../DATASET.md)*
