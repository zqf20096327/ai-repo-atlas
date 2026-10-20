# openai/openai-agents-python

⭐ 30,116 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/openai/openai-agents-python) · [官网](https://openai.github.io/openai-agents-python/) · 组织维护

**给开发者的多 Agent 工作流 Python 框架**

OpenAI 官方发布的 Python SDK，用于构建多 Agent 工作流。核心概念包括 Agent（配置指令/工具/护栏/交接）、沙箱 Agent（容器内长时任务）、实时 Agent（WebSocket 语音）、语音管线、Agent 即工具与交接、MCP 等工具接入、输入输出护栏、人工介入机制、会话历史管理与内置 tracing。Provider 无关：支持 OpenAI Responses 与 Chat Completions API 及 100+ 其他 LLM。需 Python 3.10+，通过 pip/uv 安装，运行示例需设置 OPENAI_API_KEY。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 1.3 天,年发版 88,401 位贡献者
- 涨星:近 1 天 **+23**(自 20261016 起算)
- 安装:pypi 包 `openai-agents` 月下载 12,449,784
- 平台:WINDOWS / MACOS / LINUX · 协议:MCP

## 能力要点

- 多 Agent 工作流核心原语：handoffs、guardrails、sessions、tracing
- 支持文本、沙箱、实时语音、语音管线四种 Agent 运行方式
- provider-agnostic：支持 OpenAI API 及 100+ 其他 LLM
- 沙箱客户端：macOS/Linux 用本地沙箱，Windows 支持 Docker 沙箱

## 适用场景

- 用 Python 编排多 Agent 协作与任务交接的工作流
- 构建带语音输入输出的实时对话 Agent
- 在容器沙箱中运行需要操作文件与命令的长时任务

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: The OpenAI Agents SDK is a lightweight yet powerful framework for building multi-agent workflows. It is provider-agn
> L27: To get started, set up your Python environment (Python 3.10 or newer required), and then install OpenAI Agents SDK 

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `ce34fe593ba4` · [字段定义](../../DATASET.md)*
