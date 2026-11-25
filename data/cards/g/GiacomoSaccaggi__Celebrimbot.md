# GiacomoSaccaggi/Celebrimbot

⭐ 12 · Kotlin · MIT · 推送 2026-09-21 · [GitHub](https://github.com/GiacomoSaccaggi/Celebrimbot) · 个人维护

**JetBrains IDE 内的多 Agent 自主编码助手插件**

IntelliJ 平台插件，在 IDE 内提供多 Agent 系统：按托尔金角色分工的十一个 Agent 完成路由（CHAT/EASY_TASK/COMPLEX_TASK）、规划、代码执行、审查与总结。默认经 java-llama.cpp 本地运行 Qwen 2.5 Coder 1.5B 实现离线推理，可按角色配置阿里云、Gemini、Amazon Q 回退。提供代码编辑、终端执行、git、网页搜索等 17 种工具，支持影子日志自动撤销、构建验证循环与 BM25 文件检索。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六层多 Agent 架构，带路由、规划、审查与最多 2 轮重规划
- 离线优先：本地嵌入 Qwen 2.5 Coder 1.5B（GGUF），无需 API 调用
- 暴露 Ollama 兼容 API 与 OpenAI 兼容端点，可被 Open WebUI/llama-index 等客户端调用
- MCP 服务器（HTTP 与 Stdio）及独立 CLI（forge/scan/serve/mcp-stdio/undo）

## 适用场景

- 在 JetBrains IDE 中用自然语言让 AI 修改代码、跑命令、查 git
- 无网络环境下本地运行编码助手
- 把 IDE 内模型通过 Ollama 兼容端点接入 Open WebUI 等工具

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L7:  An autonomous AI coding agent embedded directly into your JetBrains IDE.
> L9: Celebrimbot is an IntelliJ Platform plugin that brings a full multi-agent AI system into your IDE. It can read your 
> L66: All four providers — `Local`, `Alibaba Qwen Cloud`, `Google Gemini`, `Amazon Q Developer` — are selectable per-char

## 星数曲线

```mermaid
xychart-beta
    title "GiacomoSaccaggi/Celebrimbot 星数(近 3 点)"
    x-axis ["2026-10-23", "2026-11-08", "2026-11-25"]
    y-axis "stars" 9 --> 13
    line [10, 12, 12]
```

2026-10-23 10 → 2026-11-25 12（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `f647f305ba11` · [字段定义](../../DATASET.md)*
