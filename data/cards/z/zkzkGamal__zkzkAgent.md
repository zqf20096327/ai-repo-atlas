# zkzkGamal/zkzkAgent

⭐ 14 · Python · 推送 2026-10-26 · [GitHub](https://github.com/zkzkGamal/zkzkAgent) · 个人维护

**给 Linux 用户的本地 AI 系统管理 agent，多节点路由架构**

基于 LangGraph StateGraph 的本地 AI agent，面向 Linux（Ubuntu/Debian）用户管理系统：先经专用 classify 节点做意图分类，再按对话/直接执行/规划三条路径分流执行。内置 25 个工具（文件操作、进程管理、网络、部署等），危险操作有 yes/no 确认门。默认用 Ollama 完全本地推理（默认模型 qwen3:1.7b），也可设 MODEL_TYPE=NOSANA 将 LLM 调用发往 Nosana 去中心化 GPU（工具仍本地运行）；Nosana 模式会把提示、对话历史与工具输出发至远端。可选 Whisper 语音输入与 Coqui/Kokoro TTS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 专用 classify 节点做意图分类，条件边路由到对话/直接执行/规划三条路径
- 25 个本地工具，危险操作（删除/装包等）需显式确认
- 默认 Ollama 完全本地推理，可选 Nosana 去中心化 GPU 后端（27B 模型）
- 可选 Whisper 语音输入与 Coqui/Kokoro TTS 语音回复

## 适用场景

- 在 Linux 上通过对话执行文件、进程、网络等系统操作
- 让 agent 规划并生成完整项目代码（含 FastAPI 前后端示例）
- 本地无 API key 运行，或用 Nosana GPU 跑更大模型

## 场景标签

`AI 助手` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: **A privacy-first AI agent for Linux that thinks before it acts — built with LangGraph's multi-node router architec
> L199: > This is where zkzkAgent differs from a simple ReAct loop. Instead of feeding every request to a single LLM call,

## 星数曲线

```mermaid
xychart-beta
    title "zkzkGamal/zkzkAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `012cdb61d058` · [字段定义](../../DATASET.md)*
