# gittensor-ai-lab/sparkinfer

⭐ 90 · C++ · MIT · 推送 2026-10-11 · [GitHub](https://github.com/gittensor-ai-lab/sparkinfer) · [官网](https://sparkinfer.com/) · 组织维护

**面向消费级/边缘 Blackwell GPU 的 C++/CUDA MoE/LLM 推理运行时**

原生 C++/CUDA 编写的 LLM 解码运行时，针对 NVIDIA Blackwell 架构（sm_120，从 RTX 到 PRO 6000）优化，提供 2.5 MB 二进制、无 Python 依赖，通过 Docker 一条命令启动 OpenAI 兼容端点，权重首次运行自动下载。支持文本/图像/视频输入、OpenAI/Anthropic/Ollama/LM Studio 多种 API，默认开启投机解码（DFlash2/DSpark drafter，声称无损 token 级一致）。主要优化对象为 Qwen3.8-27B（NVFP4 量化），由 Gittensor SN74 竞赛持续优化。README 给出与 llama.cpp、vLLM 的基准对比数据。硬件限定 Blackwell GPU，服务图像输入需约 1 GB 显存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Docker 单命令启动 OpenAI 兼容端点，权重自动下载
- 默认投机解码（DFlash2 drafter），至多 8 个并发请求共享 draft/verify
- 支持 OpenAI/Anthropic/Ollama/LM Studio API 与文本/图像/视频输入
- 针对 Qwen3.8-27B 的 NVFP4 量化与 262,144 token 上下文

## 适用场景

- 在 RTX 5090 等 Blackwell 显卡上本地部署 Qwen3.8-27B 服务
- 需要低占用二进制、无 Python 栈的边缘推理端点
- 对比 llama.cpp/vLLM 之外的高吞吐投机解码方案

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: A native C++/CUDA runtime for MoE/LLM decoding on Blackwell — from desk-side RTX to workstation
> L64: - **APIs** OpenAI (`/v1/chat/completions`, `/v1/completions`, `/v1/responses`), Anthropic

## 星数曲线

```mermaid
xychart-beta
    title "gittensor-ai-lab/sparkinfer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 87 --> 90
    line [89, 88, 88]
```

2026-10-18 89 → 2026-10-25 88（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `c3b48028f22b` · [字段定义](../../DATASET.md)*
