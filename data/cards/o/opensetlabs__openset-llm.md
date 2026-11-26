# opensetlabs/openset-llm

⭐ 767 · C++ · MIT · 推送 2026-11-25 · [GitHub](https://github.com/opensetlabs/openset-llm) · 组织维护

**无 GPU、8 GB 内存即可本地运行 LLM 的 CPU 推理引擎**

面向普通 CPU（x86-64，AVX-512）的 LLM 推理引擎，当前运行 PrismML 的三元模型 Bonsai-2-27B（5.95 GB 文件），提供 OpenAI 兼容 API 与内置聊天页面，支持 `./serve --multi` 并发与推测解码。从源码构建，依赖 git、cmake、C++ 编译器，首次运行下载约 7.3 GB 模型。要求 Linux 或 WSL2；不带 AVX-512 的 CPU 走慢速回退路径。同类项目 openset-tts 处理语音。

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

- x86-64 AVX-512 CPU 上运行 27B 模型，文件 5.95 GB，8 GB 内存运行
- OpenAI 兼容 API（/v1），现有客户端与 agent 无需改动接入
- 默认推测解码，`--multi 4` 支持 4 路并发
- 基于 PrismML 的 llama.cpp fork 加新 kernel 与运行时补丁

## 适用场景

- 在没有 GPU 的 8 GB 内存机器上本地运行大模型
- 为已有 OpenAI 客户端或 agent 流程提供本地推理后端
- 本地离线运行搜索、抽取、agent 等场景

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L13:  Platform: Linux x86-64, AVX-512
> L49: openset-llm is an inference engine for ordinary CPUs; more models and more hardware will follow. Today it runs
> L52: serves an OpenAI-compatible API, so the clients and agents you already use work unchanged.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `acfbafcf8831` · [字段定义](../../DATASET.md)*
