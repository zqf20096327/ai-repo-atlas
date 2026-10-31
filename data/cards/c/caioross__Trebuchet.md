# caioross/Trebuchet

⭐ 14 · Python · AGPL-3.0 · 推送 2026-06-07 · [GitHub](https://github.com/caioross/Trebuchet) · 个人维护

**本地优先的自主 AI Agent 编排框架（LangGraph+llama.cpp）**

用于构建、运行与编排自主 AI Agent 的 Python 框架，面向本地硬件：LLM 推理用 llama-cpp-python 运行 GGUF 模型（Llama/Mistral/Gemma，CPU 或 CUDA），持久记忆与 RAG 用 ChromaDB。v4.0 采用 LangGraph 状态图架构，支持 Chat/Agent 模式动态切换、推理循环与错误恢复；集成视觉（OpenCV）、语音（Faster-Whisper）、TTS、Shell 与 PyAutoGUI 桌面控制工具，并提供 ToolRegistry 插件机制，放入继承 BaseTool 的 .py 文件即自动注入 LLM 上下文。前端为 NiceGUI，API 基于 FastAPI。安装需 C++ 编译器，CUDA 为可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph 状态图工作流，Chat/Agent 模式动态切换
- llama-cpp-python 本地推理 GGUF 模型（CPU/CUDA）
- ChromaDB 持久记忆与 RAG
- BaseTool 插件机制：.py 文件自动发现并注入 LLM 上下文
- 多模态工具：OpenCV 视觉、Faster-Whisper 听觉、TTS、Shell/PyAutoGUI 桌面控制

## 适用场景

- 在本地硬件上运行带工具调用的自主 Agent，数据不出本地
- 为 Agent 添加自定义工具插件而不改动核心
- 构建带视觉、语音输入和桌面自动化能力的多模态 Agent

## 场景标签

`Agent 框架` `Agent 记忆` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L18: O **Trebuchet Framework** é uma infraestrutura robusta para a criação, execução e orquestração de Agentes de IA aut
> L20: A versão **v4.0** introduz uma arquitetura baseada em grafos (**LangGraph**), permitindo fluxos de trabalho complex
> L149: **Trebuchet Framework v4.0** is a robust infrastructure for building, running and orchestrating **autonomous AI ag

## 星数曲线

```mermaid
xychart-beta
    title "caioross/Trebuchet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `640998a5e890` · [字段定义](../../DATASET.md)*
