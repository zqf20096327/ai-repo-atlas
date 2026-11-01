# Karunya-Muddana/Native

⭐ 13 · Python · Apache-2.0 · 推送 2026-09-08 · [GitHub](https://github.com/Karunya-Muddana/Native) · 个人维护

**本地优先的开源 AI Agent 运行环境，供开发者自行运行**

单文件 Web UI 加 FastAPI 后端的 agent 应用：读取文档（PDF/OCR/表格/图片）、在禁网的 Docker 容器中执行 Python、以本地嵌入模型检索自有知识库、通过 Steel 驱动真实 Chrome 浏览器，并生成 docx/xlsx/pptx 文件后复检其真实内容。模型按角色组成链式路由，免费额度（Groq/Gemini/OpenRouter/NVIDIA）在前、本机 Ollama 在后，限流时自动降级到下一环节。含 Standard 与 Research 两种运行模式，后者逐源记笔记并带 [S1] 式可核查引用。记忆分工作集、会话摘要、本地嵌入长期记忆三层。面向开发者，Python 3.10+，Apache 2.0，通过 install.py 安装；Docker、Ollama、Steel 均为可选组件，浏览器工具需 Steel 在本机运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型链式路由：免费额度限流时自动降级，链尾为本机 Ollama
- 代码在内核级禁网的 Docker 沙箱中执行，含内存与超时限制
- 本地嵌入的知识库检索，文档不出本机
- Research 模式逐源笔记，回答带可对照磁盘文件的 [S1] 式引用

## 适用场景

- 在本地跑一个能读文档、写 Office 文件、开浏览器的 agent
- 不付费、不限流地全天运行 AI 代理任务
- 对回答过程做逐步核查：每次工具调用的参数与原始结果全程可见
- 在自己机器上检索私有知识库并生成带引用的研究报告

## 场景标签

`Agent 框架` `Agent 记忆` `浏览器自动化` `文档解析` · 领域:Agent 开发

## 证据(README 行号)

> L13: An agent you run yourself. It reads your documents, executes code in a sealed
> L39: two in the afternoon. So each role is a chain of providers tried in order, and


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `3c72546ab9cc` · [字段定义](../../DATASET.md)*
