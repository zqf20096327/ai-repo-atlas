# researchim-ai/models-at-home

⭐ 42 · Python · Apache-2.0 · 推送 2026-08-20 · [GitHub](https://github.com/researchim-ai/models-at-home) · 组织维护

**在家训练与微调 LLM 的浏览器图形化训练工作室**

开源的 LLM 训练/微调工作室，通过浏览器 GUI 配置、启动并监控训练，无需写代码。支持从头预训练、继续预训练、SFT 与 GRPO 强化学习四种模式，模型采用 Llama 风格架构（RoPE/SwiGLU/RMSNorm、Flash Attention、KV-Cache）。可从 HuggingFace 一键下载 SmolLM2、Pythia、Qwen、TinyLlama 等模型作基座，流式加载 Hub 数据集并配置过滤。支持多 GPU（DDP/FSDP/DeepSpeed ZeRO 系列），内置对话测试（vLLM 后端）。推荐 Docker Compose 运行，本地运行需 Python 3.10+ 与 CUDA 11.8+。模型权重兼容 HuggingFace 生态，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种训练模式：预训练/继续预训练/SFT/GRPO 强化学习
- 浏览器 GUI 配置训练并实时监控 loss、GPU 利用率
- DDP/FSDP/DeepSpeed ZeRO-2/ZeRO-3/CPU Offload 分布式策略
- HuggingFace 模型与数据集一键下载，模型兼容 HF 生态

## 适用场景

- 在家中 GPU 上从头预训练或微调自己的小模型
- 用图形界面完成 SFT 并直接对话测试效果
- 用 GRPO 奖励函数训练推理能力
- 以 Docker 规避 CUDA/PyTorch 环境配置

## 场景标签

`微调` `模型训练` `强化学习` · 领域:训练与推理

## 证据(README 行号)

> L10: **Models at Home** is an open-source studio for training and fine-tuning Large Language Models (LLMs) at home. The 
> L23: - **Browser-based GUI** — Configure, launch, and monitor training without writing code

## 星数曲线

```mermaid
xychart-beta
    title "researchim-ai/models-at-home 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-31 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d769647f4445` · [字段定义](../../DATASET.md)*
