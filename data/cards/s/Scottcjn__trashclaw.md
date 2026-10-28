# Scottcjn/trashclaw

⭐ 75 · Python · MIT · 推送 2026-09-26 · [GitHub](https://github.com/Scottcjn/trashclaw) · [官网](https://rustchain.org) · 组织维护

**零依赖单文件本地 LLM 工具调用 agent，面向老旧硬件**

单文件 Python 工具调用 agent（trashclaw.py），仅依赖 Python 3.7+ 标准库，接入任意本地 LLM 服务器（自动探测 llama.cpp、Ollama、LM Studio 或 OpenAI 兼容端点），无需云端与 API key。内置 14 个工具（文件读写/编辑/补丁、shell 命令、grep、git、剪贴板、URL 抓取等）、21 个斜杠命令与插件系统，支持会话保存、undo、只读审计模式与老旧硬件检测（PowerPC G4/G5、IBM POWER8、2013 Mac Pro）。作者在 2013 Mac Pro 上以 Qwen 3B Q4 达到 15.6 tokens/sec。限制：3B 模型在复杂多步任务上易出错；离散 GPU 上 Metal 生成可能慢于 CPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件零依赖，仅 Python 3.7+ 标准库，无 pip install
- 自动探测 llama.cpp/Ollama/LM Studio/OpenAI 兼容后端
- 14 个内置工具 + 21 个命令 + 插件系统（放入 ~/.trashclaw/plugins/ 即成工具）
- 只读审计模式（--read-only）屏蔽写/shell/提交/剪贴板复制工具

## 适用场景

- 在老旧或非主流硬件（PowerPC G4、POWER8、2013 Mac Pro）上跑本地 AI agent 干活
- 让本地 LLM 自动改代码、跑 shell、管理 git 提交
- 无云端无 API key 的离线终端自动化任务

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L15: TrashClaw is a tool-use agent. You describe a task, the LLM decides what tools to call, sees the results, and itera
> L97: - **Auto-detects backend**: llama.cpp, Ollama, LM Studio, any OpenAI-compatible


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `d072260e460e` · [字段定义](../../DATASET.md)*
