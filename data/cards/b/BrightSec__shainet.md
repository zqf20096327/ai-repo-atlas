# BrightSec/shainet

⭐ 198 · Crystal · MIT · 推送 2026-10-21 · [GitHub](https://github.com/BrightSec/shainet) · 组织维护

**纯 Crystal 神经网络库：训练网络并本地推理 LLM**

用 Crystal 语言编写的神经网络库，源自生物启发神经网络研究，现提供通用网络训练与运行能力：多种层类型与训练算法（SGD、Adam、iRprop+）、流式数据处理、Autograd、SafeTensors 读取。可直接加载 HuggingFace SafeTensors 模型（无需 Python）与 GGUF 文件（含 Ollama blob），支持 GPT-2、LLaMA、Mistral、Qwen2/3/3-MoE/3.5 架构的 LLM 推理，带 KV-cache、Q8/Q4 量化与 MoE 专家卸载。CPU 可用，CUDA GPU 支持为可选，需编译时启用 -Denable_cuda。另附 OpenAI 兼容 API 服务器与编码 agent 示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Crystal 实现，可训练神经网络并支持流式大数据集
- 直接加载 HuggingFace SafeTensors（无需 Python）与 GGUF 文件（含 Ollama blob）
- LLM 推理支持 GPT-2/LLaMA/Mistral/Qwen2/3/3-MoE/3.5，含 KV-cache 与 Q8/Q4 量化
- MoE 专家卸载与自动层放置，使大模型可在小显存 GPU 上运行

## 适用场景

- 在 Crystal 项目中训练和部署神经网络
- 本地加载并运行 GGUF 或 SafeTensors 格式的 LLM
- 通过 OpenAI 兼容端点为现有客户端提供本地模型服务

## 场景标签

`推理引擎` `模型量化` `模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: SHAInet (Super Human Artificial Intelligence Network) is a neural network library written in pure Crystal. Originall
> L12: - LLM inference: GPT-2, LLaMA, Mistral, Qwen2, Qwen3, Qwen3-MoE, and Qwen3.5


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `82b8551192b6` · [字段定义](../../DATASET.md)*
