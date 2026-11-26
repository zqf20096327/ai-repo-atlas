# dotcoreai/dotcore

⭐ 7 · Rust · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/dotcoreai/dotcore) · [官网](https://dotcore.ai) · 组织维护

**本地 AI 部署运行时：加载模型并提供统一端点**

Dotcore 在自有硬件上运行 AI 模型：加载模型并适配到本机硬件，通过统一的 OpenAI 兼容 API 暴露所有模型，部署不可用时请求可转移到其他部署。底层支持 llama.cpp、vLLM 等引擎，显示模型内存需求与机器可容纳的最大上下文，支持多机协同，并可在同一机器上运行 Open WebUI、ComfyUI 等应用。管理通过 Web 控制台进行。当前处于 alpha 阶段，模型暂不能拆分到多 GPU，仅支持 Linux（NVIDIA GPU）与 Apple Silicon macOS。安装依赖 Nix 与 Docker。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 通过一个 OpenAI 兼容 API 调用所有模型，部署故障时自动转移请求
- 显示模型内存需求及每台机器可容纳的最大上下文
- 支持 llama.cpp、vLLM 等多种推理引擎
- 支持多机协同，同一机器可运行 Open WebUI、ComfyUI 等应用

## 适用场景

- 在自有硬件上本地运行 LLM 而无需手动配置环境
- 用统一端点管理多台机器上的多个模型部署
- 在本地机器上搭建对话或图像生成应用并接入模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: Dotcore runs AI on hardware you own. It loads models, fits them to your machines, and puts a single endpoint in fron
> L7: - **Pick a model, get a running endpoint.** Dotcore starts it for you, on llama.cpp, vLLM, etc.
> L9: - **One endpoint in front of everything.** Call every model through one OpenAI-compatible API. If a deployment is do


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `36b5fd6f06c6` · [字段定义](../../DATASET.md)*
