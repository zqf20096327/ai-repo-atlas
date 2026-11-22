# RegaLabs/lorasmith

⭐ 3 · Rust · Apache-2.0 · 推送 2026-11-12 · [GitHub](https://github.com/RegaLabs/lorasmith) · 个人维护

**一条命令在自有数据上微调开源 LLM 的 Rust 工具**

基于 Burn 构建的单二进制 LoRA/QLoRA 微调工具，用 Rust 实现训练，不依赖 Python 与 CUDA 配置。从 Hugging Face 下载模型，读取 JSONL 格式数据（messages/prompt-completion/text 三种形态），训练后输出 PEFT 适配器、合并模型与 Q8_0 GGUF 文件及 Ollama Modelfile。运行时通过 wgpu 支持 Vulkan、Metal、DirectX 12 或纯 CPU，可选 cuda/rocm cargo 特性。软件处于早期状态，训练仅在 Linux 上实测，不支持恢复训练与多 GPU 训练。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 单二进制、无 Python，支持 Vulkan/Metal/DirectX 12/CPU 后端
- 训练输出 PEFT 适配器、合并模型与 Q8_0 GGUF 导出
- --qlora 4-bit 训练降低显存占用（0.5B 模型峰值 1.8 GB 实测）
- 支持 Llama、Mistral、Qwen2/3、SmolLM 等模型家族与本地模型目录

## 适用场景

- 在没有 NVIDIA 卡或 CUDA 环境的机器上做 LoRA 微调
- 把自有对话数据训练成可在 Ollama 运行的模型
- 导出适配器或 GGUF 供 vLLM、llama.cpp 等推理工具使用

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L19: Training a LoRA adapter today means PyTorch, CUDA versions that have to line up, half a dozen Hugging Face librarie
> L53: lorasmith train qwen2.5:0.5b pirate.jsonl
> L137: When memory runs out, lorasmith says so and suggests, in this order: `--qlora`, `--batch-size 1`, a lower `--max-l


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `e7bdeffe6c39` · [字段定义](../../DATASET.md)*
