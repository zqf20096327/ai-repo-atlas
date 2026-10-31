# shakfu/chimera

⭐ 14 · C++ · MIT · 推送 2026-10-17 · [GitHub](https://github.com/shakfu/chimera) · 个人维护

**单二进制本地推理多工具：集成 llama/whisper/sd.cpp 三引擎**

静态链接的 C++ 本地推理多工具，将 llama.cpp、whisper.cpp、stable-diffusion.cpp、SQLite 与 sqlite-vec 打包为一个原生二进制：同一进程可运行文本生成、持久化对话、语音转文字、文生图、嵌入与个人 RAG 向量库，并通过 OpenAI 兼容 HTTP 服务器跨模态提供服务，共享一套 ggml 后端与单一 SQLite 数据库。面向 CLI 用户与 C++ 嵌入方（提供 libchimera.a 静态库）。从源码构建，需 OpenSSL 等系统依赖；支持 CPU/CUDA/ROCm/SYCL/Vulkan/Metal 后端，无 GUI（可选嵌入 web UI）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三引擎共享单一 ggml 后端与单一 SQLite 数据库
- OpenAI 兼容 HTTP 服务器覆盖文本/音频/图像/嵌入/RAG 路由
- 同一构建产出 libchimera.a 可再分发静态库供 C++ 嵌入
- CPU/CUDA/ROCm/SYCL/Vulkan/Metal 一等构建目标

## 适用场景

- 本地同时跑 LLM、语音转写与文生图，不装三套服务器
- 以单一静态二进制分发到无 Python/Node 运行时的目标机
- 在自己的 C++ 进程中嵌入推理引擎与 HTTP 服务

## 场景标签

`推理引擎` `图像生成` `语音识别` `RAG` · 领域:内容生成

## 证据(README 行号)

> L5: It bundles llama.cpp, whisper.cpp, stable-diffusion.cpp, SQLite, and sqlite-vec into one native binary. The same pro
> L34: chimera targets CLI-first users who run more than one ggml-backed modality (text + audio + image) and want them sha

## 星数曲线

```mermaid
xychart-beta
    title "shakfu/chimera 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `90ad5c53cd4f` · [字段定义](../../DATASET.md)*
