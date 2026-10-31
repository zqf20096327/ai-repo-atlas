# RamboRogers/cyber-inference

⭐ 15 · Python · GPL-3.0 · 推送 2026-09-25 · [GitHub](https://github.com/RamboRogers/cyber-inference) · [官网](https://matthewrogers.org) · 个人维护

**本地推理服务器的 Web GUI 管理工具，提供 OpenAI 兼容 API**

面向边缘部署的推理服务管理器：以 Web 仪表盘和 API 服务器管理 llama.cpp（GGUF）、transformers（HuggingFace 目录）、whisper.cpp（转录/翻译）三种后端，统一暴露 OpenAI 兼容的 /v1 端点（chat/completions/embeddings/audio/rerank）。机制上支持模型下载注册（含 GGUF 分片集）、MTP 投机解码自动配置、懒加载与闲置卸载、JWT 可选鉴权。限制：容器镜像仅支持 NVIDIA（Linux AMD64 与 Thor ARM64），macOS Apple Silicon 需走原生启动；rerank 仅支持 GGUF/llama.cpp，transformers 不支持。原生启动需 Python 3.12+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容 /v1 端点覆盖 chat/completions/embeddings/audio/rerank
- llama.cpp、transformers、whisper.cpp 三引擎统一管理与懒加载/闲置卸载
- HuggingFace 模型下载注册，含 GGUF 分片集合并与 MTP 投机解码自动配置
- NVIDIA 容器镜像（Linux AMD64 / Thor ARM64）+ macOS Apple Silicon 原生启动

## 适用场景

- 在边缘设备或本地服务器上用图形界面管理推理模型并提供 OpenAI 兼容 API
- 用现有 OpenAI SDK 代码直接访问本地部署的 GGUF/HF 模型
- 统一部署文本生成、嵌入、重排与语音转录服务

## 场景标签

`推理引擎` `语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L13: Cyber-Inference is a web GUI and API server for running local inference engines behind OpenAI-compatible `/v1` endp
> L26: - Web dashboard for model and resource management

## 星数曲线

```mermaid
xychart-beta
    title "RamboRogers/cyber-inference 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b33a9ac6226f` · [字段定义](../../DATASET.md)*
