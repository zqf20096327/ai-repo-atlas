# bobazooba/xllm

⭐ 410 · Python · Apache-2.0 · 推送 2026-11-19 · [GitHub](https://github.com/bobazooba/xllm) · [官网](https://t.me/talequestbot) · 个人维护

**面向工程师的大模型微调训练库**

X—LLM 是一个 Python 库，用于 LLM 微调训练，将 QLoRA、DeepSpeed、GPTQ 量化、Flash Attention 2、FSDP 等训练技术封装为单一 Config 配置。流程覆盖数据准备、训练、LoRA 融合、量化四步，可从命令行启动，checkpoint 可推送至 HuggingFace Hub，训练进度可上报 W&B。库内置 SODA 数据集用于演示，其余数据集需用户自行实现；通过 pip 安装，提供快速原型与生产两条使用路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- QLoRA、GPTQ、DeepSpeed、Flash Attention 2、FSDP 等训练技术封装于单一 Config
- prepare/train/fuse/quantize 四步流程可由命令行运行
- checkpoint 保存至 HuggingFace Hub，训练进度上报 W&B
- 支持 Yi-34B、Llama 2、Zephyr、Falcon、Phi、Qwen 等模型

## 适用场景

- 快速原型化一个大模型微调实验
- 多 GPU 环境下运行分布式训练
- 训练后对模型做 GPTQ 量化以减少显存占用

## 场景标签

`微调` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L17: Cutting Edge & Easy LLM Finetuning using the most advanced methods (QLoRA, DeepSpeed, GPTQ, Flash Attention 2, FSDP
> L28: **X—LLM** is your solution. It's a user-friendly library that streamlines training optimization, so you can **focus
> L311: Remember, these tasks in `X—LLM` start from the command line. So, when you're all set to go, launching your full p


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `0066b28a7945` · [字段定义](../../DATASET.md)*
