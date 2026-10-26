# Quazmoz/npu-windows

⭐ 29 · Python · 推送 2026-09-18 · [GitHub](https://github.com/Quazmoz/npu-windows) · 个人维护

**在 Intel Core Ultra NPU 上本地运行 LLM 的 OpenAI 兼容服务器**

面向 Intel Core Ultra（Meteor Lake/Arrow Lake/Lunar Lake）NPU 的 Windows 11 本地 LLM 推理服务器：基于 ipex-llm[npu] 后端加载 Qwen、Llama、DeepSeek R1、GLM-Edge、MiniCPM、Baichuan2 等模型，通过 setup.bat 自动完成 Miniconda 环境与依赖安装并执行硬件预检（Windows 版本、NPU 驱动）。提供 http://localhost:8000 内置聊天 UI、/v1/chat/completions 等 OpenAI 兼容端点与 tool calling，可连接 Open WebUI、N8N。README 标注本仓库是较早期的 NPU 方案，指向更新的 OpenVINO 项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI 兼容 API（/v1/chat/completions、/v1/responses）与 tool calling 支持
- 内置聊天 UI，含 NPU 状态、内存与 token 实时监控
- setup.bat 硬件预检 + 自动安装 Miniconda/ipex-llm 环境
- 官方验证 Qwen/Llama/DeepSeek/GLM-Edge/MiniCPM/Baichuan2 等 NPU 模型列表

## 适用场景

- 在 Intel NPU 上低功耗本地运行 LLM 并通过 OpenAI 客户端调用
- 为 Open WebUI 或 N8N 提供局域网内的本地推理后端
- 在 Windows 笔记本上构建带 function calling 的本地 AI agent

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Run Large Language Models on your Intel Core Ultra NPU with an OpenAI-compatible API.
> L183: - `/v1/chat/completions` — OpenAI Chat Completions API (Open WebUI, LangChain, curl)
> L55: > environment (Python 3.11), installs `ipex-llm[npu]` and all server dependencies,

## 星数曲线

```mermaid
xychart-beta
    title "Quazmoz/npu-windows 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `4cef62109c1c` · [字段定义](../../DATASET.md)*
