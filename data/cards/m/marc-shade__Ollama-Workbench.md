# marc-shade/Ollama-Workbench

⭐ 49 · Python · MIT · 推送 2026-07-18 · [GitHub](https://github.com/marc-shade/Ollama-Workbench) · 个人维护

**本地管理、测试与使用 Ollama 模型的一体化工作台**

基于 Streamlit UI 与 Flask API 的本地平台，面向使用自有 Ollama 服务器的用户：聚合 Ollama 本地模型与 OpenAI、Groq、Mistral 等外部提供商，提供文本/语音/视觉聊天、RAG（ChromaDB 向量库）、多 Agent 与可视化工作流、模型管理（下载/更新/对比/基准测试）、观测与 Opik 追踪，并随应用启动一个 OpenAI 兼容 API 服务器（端口 8000）。通过 git clone 加 setup 脚本安装，Python 3.10+，默认无认证，文档明确安全模块现状（JWT/RBAC 已含但未接入 UI，MFA 未实现）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一界面接入 Ollama 本地模型与 OpenAI/Groq/Mistral 外部提供商
- 随应用启动的 OpenAI 兼容 API 服务器（端口 8000）
- 多 Agent 编排与拖拽式可视化工作流构建器
- RAG（ChromaDB）、TTS、语音识别与视觉模型支持
- 1,076 项测试套件；AES-256-GCM 加密 API key 存储

## 适用场景

- 本地集中管理和测试自己的 Ollama 模型
- 让任意 OpenAI 客户端通过兼容 API 调用本地模型
- 搭建多 Agent 工作流与 RAG 问答
- 对比不同提供商模型的性能与成本

## 场景标签

`多智能体` `RAG` `工作流自动化` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L15: **Ollama Workbench** is a comprehensive platform for managing, testing, and using AI models from the Ollama library
> L62: - **Ollama Models** - Local LLM execution with full privacy
> L212: - **Local Model Management**: List, download, update, remove Ollama models

## 星数曲线

```mermaid
xychart-beta
    title "marc-shade/Ollama-Workbench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-31 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `080ad8a214c4` · [字段定义](../../DATASET.md)*
