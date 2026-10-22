# YassWorks/Ally

⭐ 239 · Python · Apache-2.0 · 推送 2026-04-05 · [GitHub](https://github.com/YassWorks/Ally) · [官网](https://hub.docker.com/r/yassw0rks/ally) · 个人维护

**终端里的本地私有 agentic 助手，读写文件、执行命令、RAG 与项目生成**

面向终端用户的 AI CLI 助手：默认基于 Ollama 构建全本地 agentic 系统，也支持 OpenAI、Anthropic、Google GenAI、Groq、Cerebras、OpenRouter、GitHub Models 等推理提供方。默认聊天界面提供文件读写、联网访问、命令执行等工具（执行前需许可），支持文件嵌入知识库的 RAG 会话（Hugging Face/Ollama/NLP Cloud/OpenAI 嵌入），以及由 Brainstormer Agent 与 Codegen Agent 组成的编码项目生成工作流（自述为早期阶段）。提供 Docker 镜像与本地源码安装两种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 默认 Ollama 本地运行，支持 7+ 外部推理提供方切换
- Agent 工具可读写文件、访问互联网、执行命令（许可确认机制）
- RAG：文件嵌入知识库，会话内不使用外部数据作答
- Brainstormer+Codegen 双 Agent 编码项目生成工作流（Preview）

## 适用场景

- 在终端用自然语言完成日常任务与复杂项目
- 把本地文件嵌入知识库做私密问答
- 隐私敏感场景下本地运行 agentic 工作流

## 场景标签

 · 领域:AI 助手/终端工具

## 证据(README 行号)

> L12: **Ally** is an AI-powered CLI tool designed to assist with anything from everyday tasks to complex projects efficie
> L14: Ally was built a fully local agentic system using **Ollama**, but it also works seamlessly with:

## 星数曲线

```mermaid
xychart-beta
    title "YassWorks/Ally 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 238 --> 240
    line [239, 239]
```

2026-10-18 239 → 2026-10-22 239（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ce5cd1c56eb6` · [字段定义](../../DATASET.md)*
