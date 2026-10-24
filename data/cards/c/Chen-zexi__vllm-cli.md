# Chen-zexi/vllm-cli

⭐ 505 · Python · MIT · 推送 2026-01-25 · [GitHub](https://github.com/Chen-zexi/vllm-cli) · 个人维护

**用 vLLM 部署 LLM 服务的命令行工具**

围绕 vLLM 的服务启动与管理 CLI：提供交互式终端与命令行两种模式，自动发现本地 HuggingFace 与 Ollama 模型，内置 7 种配置 profile（含针对 NVIDIA A100/H100/Blackwell 的 GPT-OSS 优化档），支持快捷方式、GPU 选择、环境变量管理与实时服务器监控。实验性多模型代理可将多个模型经单一 API 端点提供服务。默认不安装 vLLM/PyTorch，需自行准备 CUDA 兼容环境，Python 3.9+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 交互式终端与 CLI 双模式，含 GPU 状态概览
- 自动发现 HuggingFace 与 Ollama 本地模型（GGUF 实验性支持）
- 7 个内置配置 profile 与快捷方式系统
- 实验性多模型代理：单端点动态加载/卸载模型

## 适用场景

- 用命令行快速启动和管理 vLLM 推理服务
- 为不同 GPU 架构选择预置的 GPT-OSS 服务配置
- 监控运行中的 vLLM 服务器状态

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L10: A command-line interface tool for serving Large Language Models using vLLM. Provides both interactive and command-l
> L22: - **📊 Server Monitoring** - Real-time monitoring of active vLLM servers

## 星数曲线

```mermaid
xychart-beta
    title "Chen-zexi/vllm-cli 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 504 --> 507
    line [506, 505, 505]
```

2026-10-18 506 → 2026-10-24 505（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3d7b7884faf2` · [字段定义](../../DATASET.md)*
