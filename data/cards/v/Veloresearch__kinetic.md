# Veloresearch/kinetic

⭐ 275 · Rust · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/Veloresearch/kinetic) · [官网](https://veloresearch.com/research/kinetic) · 组织维护

**在个人电脑上本地运行 GGUF 大模型的 Rust 推理引擎**

用 Rust 编写的本地推理引擎，读取 llama.cpp 格式的 GGUF 文件，单个二进制支持 CPU 与 NVIDIA/AMD/Intel GPU（CUDA/Vulkan/Metal），平台为 Windows 与 Linux。内置 RAD-1 精确投机解码、Warm Start 提示缓存、Zero Wait 输入预处理、Torque CUDA graph、Convoy 并发与 Shortlist 等默认开启的加速技术，声明输出与普通解码逐 token 一致。可作为 llama-server/llama-cli 等工具的替身运行，同时提供 OpenAI、llama-server 与 Ollama 兼容 API，当前为 beta 状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单二进制运行 CPU 与 NVIDIA/AMD/Intel GPU，读取 GGUF 文件
- RAD-1 精确投机解码与 Warm Start 提示缓存，声明输出逐 token 与普通解码一致
- 提供 OpenAI /v1、llama-server 与 Ollama /api 兼容接口，支持 llama.cpp 命令行标志
- 自动检测机器并推荐可运行模型，`kinetic pull` 下载模型

## 适用场景

- 在自己的电脑上用一条命令下载并聊天运行 GGUF 模型
- 已有 llama.cpp 工作流时替换 server/cli/bench/quantize 等工具
- 多用户同时向本地模型服务发请求（--parallel 共享推理）
- 长文档粘贴场景下加速首 token 返回（Zero Wait）

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: ### The open engine for running AI on your own computer.
> L11: API
> L287: works as written. One port answers the OpenAI API under `/v1`,

## 星数曲线

```mermaid
xychart-beta
    title "Veloresearch/kinetic 星数(近 12 点)"
    x-axis ["2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-27"]
    y-axis "stars" 40 --> 296
    line [61, 84, 87, 89, 90, 91, 152, 246, 263, 270, 275, 275]
```

2026-11-11 61 → 2026-11-27 275（+214）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `1fa058867e38` · [字段定义](../../DATASET.md)*
