# johnbean393/Sidekick

⭐ 3,320 · Swift · MIT · 推送 2026-09-30 · [GitHub](https://github.com/johnbean393/Sidekick) · [官网](https://johnbean393.github.io/Sidekick/) · 个人维护

**macOS 本地 LLM 聊天应用：离线对话并引用本机文件与网页**

原生 macOS 应用，内置 llama.cpp 推理引擎，可离线运行 GGUF 本地模型（如 Qwen），无需额外安装软件。通过 RAG 读取用户配置的'专家'资源（文件/文件夹/网站）并给出带引用来源的回答；支持网络搜索、函数调用、长程 Deep Research、跨会话记忆、Canvas 编辑、基于 CoreML 的文本生图。同时允许接入 OpenAI 兼容 API（OpenAI/Anthropic/DeepSeek/Groq 等预设）。要求 Apple Silicon 与 8GB 以上内存，生图功能需 macOS 15.2+ 与 Apple Intelligence。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 llama.cpp 推理引擎，离线运行 GGUF 本地模型
- RAG 读取本机文件/文件夹/网页，回答附带可点击的引用来源
- 函数调用与本地运行的 agent、Deep Research 多步研究、跨会话记忆
- CoreML 自动识别生图提示词（需 macOS 15.2+ 与 Apple Intelligence）

## 适用场景

- 写论文时让 AI 从本地文献中找答案并核验引用
- 把不同学科的资料配成'专家'，按需激活提问
- 完全离线、数据不出本机地使用 LLM 聊天与研究功能

## 场景标签

`聊天机器人` `RAG` `科研工具` · 领域:对话与助手

## 证据(README 行号)

> L8: Chat with a local LLM that can respond with information from your files, folders and websites on your Mac without in
> L10: Sidekick supports modern GGUF local models such as Qwen3.5 out of the box through its built-in `llama.cpp` backend.
> L34: Because Sidekick uses RAG (Retrieval Augmented Generation), you can theoretically put unlimited resources into each

## 星数曲线

```mermaid
xychart-beta
    title "johnbean393/Sidekick 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 3319 --> 3321
    line [3320, 3320]
```

2026-10-18 3,320 → 2026-10-21 3,320（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-20 · 置信度 high · 依据 README sha `760d19f993fa` · [字段定义](../../DATASET.md)*
