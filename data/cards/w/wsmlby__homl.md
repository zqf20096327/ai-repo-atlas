# wsmlby/homl

⭐ 90 · Python · Apache-2.0 · 推送 2026-02-23 · [GitHub](https://github.com/wsmlby/homl) · [官网](https://homl.dev/) · 个人维护

**家庭实验室运行 LLM 的工具：Ollama 式 CLI 加 vLLM 推理**

由 CLI 与 Server 两部分组成：Server 在 Docker 容器中运行，基于 vLLM 镜像构建，负责模型生命周期管理与 gRPC 控制接口，并暴露 OpenAI 兼容 API；CLI 为 Python 包，通过一行脚本安装。功能包括从 Hugging Face Hub 拉取模型、交互式聊天、按需自动加载/卸载模型（默认 10 分钟空闲后卸载）。当前官方仅支持 CUDA 平台，ROCm/Apple Silicon 在路线图中；项目已标记弃用，建议改用 Docker Model Runner。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于 vLLM 的推理，暴露 OpenAI 兼容 API
- 模型按请求自动加载，空闲 10 分钟自动卸载
- 从 Hugging Face Hub 拉取模型的一行式 CLI
- Server 以 Docker 容器方式运行

## 适用场景

- 在家庭实验室服务器上用简单 CLI 运行本地 LLM
- 为已有工具提供 OpenAI 兼容的本地 API 端点
- 在单 GPU 上按需切换运行多个模型

## 场景标签

 · 领域:LLM 基础设施

## 证据(README 行号)

> L5: HoML aims to combine the ease of use of Ollama with the high-performance inference capabilities of vLLM. This projec
> L28: * **OpenAI-Compatible API:** A built-in server that exposes an OpenAI-compatible API for seamless integration with 

## 星数曲线

```mermaid
xychart-beta
    title "wsmlby/homl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 89 --> 91
    line [90, 90]
```

2026-10-18 90 → 2026-10-24 90（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `2b72b3d98754` · [字段定义](../../DATASET.md)*
