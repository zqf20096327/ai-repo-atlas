# Cre4T3Tiv3/unsloth-llama3-alpaca-lora

⭐ 39 · Jupyter Notebook · Apache-2.0 · 推送 2026-04-02 · [GitHub](https://github.com/Cre4T3Tiv3/unsloth-llama3-alpaca-lora) · [官网](https://huggingface.co/spaces/Cre4T3Tiv3/unsloth-llama3-alpaca-demo) · 个人维护

**LLaMA 3 8B 的 4-bit QLoRA 微调流水线：训练到发布适配器**

基于 Unsloth 与 HuggingFace PEFT 的端到端模型训练流水线：数据准备、QLoRA 微调、幻觉模式评估与部署。基座为 unsloth/llama-3-8b-bnb-4bit，在约 2K 条 Alpaca-cleaned 及补充的 grounded 样本上以 LoRA(r=16) 训练两个 epoch，训练硬件为 A100 40GB。通过 Makefile 提供安装/训练/评估/推理命令，训练后适配器合并并发布至 HuggingFace，附 HF Spaces 在线演示。自述限制：未针对 2K token 以上上下文优化，4-bit 量化可能降低保真度，不适用于事实问答或关键领域生产环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4-bit QLoRA 微调 LLaMA 3 8B，基于 Unsloth + HuggingFace PEFT
- eval_adapter.py 检查幻觉模式并输出 JSON 评估摘要
- Makefile 一键安装/训练/评估/推理（uv 管理虚拟环境）
- 适配器发布于 HuggingFace，附 HF Spaces 演示

## 适用场景

- 在消费级显存预算内对 LLaMA 3 8B 做指令微调
- 参考完整的 QLoRA 训练到发布流水线
- 评估微调适配器的幻觉模式与关键词覆盖

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L1: 4-bit QLoRA fine-tuning pipeline for LLaMA 3 8B. From training configuration to published adapter on HuggingFace. Me
> L22: An end-to-end pipeline for custom model training: dataset preparation, QLoRA fine-tuning, evaluation, and deploymen
> L35: |Framework|Unsloth + HuggingFace PEFT|

## 星数曲线

```mermaid
xychart-beta
    title "Cre4T3Tiv3/unsloth-llama3-alpaca-lora 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-26 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c3da68742984` · [字段定义](../../DATASET.md)*
