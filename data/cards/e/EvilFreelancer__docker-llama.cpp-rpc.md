# EvilFreelancer/docker-llama.cpp-rpc

⭐ 26 · Dockerfile · MIT · 推送 2026-08-17 · [GitHub](https://github.com/EvilFreelancer/docker-llama.cpp-rpc) · 个人维护 · 中文 README

**将 llama.cpp RPC 服务器打包为 Docker 镜像，实现分布式推理**

基于 llama.cpp 构建的 Docker 化项目：仅编译 RPC 服务器及作为 RPC 客户端运行的辅助工具（llama-server、llama-cli、llama-embedding），用于 GGUF 格式大语言模型与嵌入模型的分布式推理。镜像发布于 Docker Hub，提供 CPU-only（amd64/arm64）与 CUDA（amd64，Ampere 及以上）两种构建，通过环境变量配置端口、内存、GPU 层数与后端地址，附 docker-compose 示例与 HTTP 调用示例，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 仅编译 llama.cpp RPC 服务器与 RPC 客户端工具，实现跨机分布式推理
- 镜像覆盖 CPU-only（amd64/arm64）与 CUDA（compute capability 8.0+）架构
- 环境变量配置运行模式（server/backend/none）、端口、显存与 GPU 层数
- 支持通过 LLAMACPP_VERSION 构建参数指定任意 llama.cpp 版本

## 适用场景

- 用多台机器分担 GGUF 模型的推理负载
- 在 Docker/Docker Compose 环境中部署 llama.cpp RPC 后端
- 自行构建指定版本或指定 CUDA 架构的 RPC 镜像

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: Данный проект основан на llama.cpp и компилирует
> L7: вспомогательные утилиты, работающие в режиме RPC-клиента, необходимые для реализации распределённого инференса

## 星数曲线

```mermaid
xychart-beta
    title "EvilFreelancer/docker-llama.cpp-rpc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-26 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `91beafe9d1db` · [字段定义](../../DATASET.md)*
