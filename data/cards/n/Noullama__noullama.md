# Noullama/noullama

⭐ 4 · Rust · AGPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/Noullama/noullama) · [官网](https://noullama.dev) · 个人维护

**在本地运行决策模型的工作台与 API**

基于 llama.cpp 的桌面应用与本地运行时，面向在本机运行"决策模型"的用户：对给定内容回答类型化问题（choice/noul/score 三类），而非对话。提供模型下载（Hugging Face GGUF）、llama.cpp 构建管理与自动更新、GPU/CPU 加载配置、Playground 试问、本地 HTTP API（127.0.0.1:11435）与无依赖 Python 客户端。带内存保护检查、models.yml 库管理与备份。限制：仅 Linux x86-64，处于早期 beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 本地 API 支持 /v1/systemone 决策端点与 OpenAI 格式 /v1/chat/completions
- 自动下载并管理 llama.cpp 构建（CPU/Vulkan/CUDA 12/13），含 SHA-256 校验
- Playground 支持 choice/noul/score 三类类型化问题与预设
- 内存保护：拒绝明显超内存的加载并在内存不足时弹出模型

## 适用场景

- 在本地对内容做类型化判定（如工单分派、退款识别）
- 通过本地 API 把决策模型接入自己的代码
- 管理多个 GGUF 模型与 llama.cpp 构建的加载与更新

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L6:  A local workbench and API for decision models using llama.cpp
> L13: - serves them to your own code through a **local API** and a **Python client**
> L16: Linux x86-64 only, in early beta.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `9d941c3f23d3` · [字段定义](../../DATASET.md)*
