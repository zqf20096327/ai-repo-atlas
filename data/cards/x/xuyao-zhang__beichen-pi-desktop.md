# xuyao-zhang/beichen-pi-desktop

⭐ 16 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/xuyao-zhang/beichen-pi-desktop) · 个人维护 · 中文 README

**给本地模型用户的 Windows 桌面 Agent 平台，控制上下文与 Token**

面向本地部署模型的 Windows 桌面 Agent 平台，基于 Electron，通过 Pi RPC 接入 Pi 生态（会话树、工具、技能、扩展、OAuth/API 认证、原生自动压缩）。核心机制：Quantum Collapse 在回合结束后将已完成 thinking 压缩为本地短摘要，Ghost Payload 在后续请求中剔除已完成 thinking；提供五档 Agent 模式与集中式 Token 仪表（上下文占用、缓存、费用、token/s 等）。不下载、启动或量化模型；Agent 继承当前 Windows 用户权限，非安全沙箱。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 回合后思考上下文治理：Quantum Collapse 本地摘要与 Ghost Payload 剔除已完成 thinking
- Token 仪表：上下文占用、缓存读写、命中率、费用、token/s 集中展示
- 每窗口独立 Pi RPC、工作目录、会话、模型与推理等级，支持多开
- Agent 界面可读取项目、编辑代码、运行 PowerShell

## 适用场景

- 用 Ollama/LM Studio/vLLM 本地模型执行编码 Agent 任务
- 长会话中追踪上下文占用与 Token 消耗明细
- 无人值守运行复杂任务后只收取最终结果

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L5:  为本地部署模型而生的极简 Agent 平台
> L27: 北辰 Pi 把 Pi 的模型、会话、工具、技能、扩展、认证与原生自动压缩装进一个 Windows 桌面 Agent：界面尽量少，控制必须明确，数据必须能测，边界必须说清。
> L39: |**本地优先 / Local first**|原生接入 Ollama、LM Studio、vLLM 和 OpenAI-compatible 本地端点，也支持 OpenAI Responses、Anthropic Messages


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `5a1f4d1b1476` · [字段定义](../../DATASET.md)*
