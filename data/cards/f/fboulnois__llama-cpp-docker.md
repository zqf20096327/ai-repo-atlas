# fboulnois/llama-cpp-docker

⭐ 68 · Shell · MIT · 推送 2026-04-03 · [GitHub](https://github.com/fboulnois/llama-cpp-docker) · 个人维护

**在 GPU 加速 Docker 容器中运行 llama.cpp 聊天服务器**

提供 Docker 封装，用于构建并运行 llama.cpp 的聊天服务器，默认在 localhost:8080 提供服务。默认要求带 CUDA 的 NVIDIA GPU（8GB+ 显存），无 GPU 时回退为 CPU 版本。通过 docker-compose 环境变量配置上下文长度、GPU 层数等参数，并以 LLAMA_ARG_HF_REPO 变量从 HuggingFace 自动下载 GGUF 格式模型（默认 bartowski/Meta-Llama-3.1-8B-Instruct-GGUF:q5_k_m），README 附带按 ELO 排序的流行模型列表。面向希望以容器方式部署本地 LLM 推理的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GPU 加速 Docker 容器运行 llama.cpp 聊天服务器
- 无 CUDA GPU 时自动回退 CPU 版本
- 通过环境变量从 HuggingFace 自动下载 GGUF 模型
- 提供按 ELO 排序的推荐模型列表与量化说明

## 适用场景

- 用 Docker Compose 快速部署本地 LLM 聊天服务
- 在有 NVIDIA GPU 的机器上跑量化 GGUF 模型推理
- 通过切换 HuggingFace 仓库变量更换运行模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Run llama.cpp in a GPU accelerated Docker container.
> L16: After starting up the chat server will be available at `http://localhost:8080`.

## 星数曲线

```mermaid
xychart-beta
    title "fboulnois/llama-cpp-docker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-25 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e908c6b2bad8` · [字段定义](../../DATASET.md)*
