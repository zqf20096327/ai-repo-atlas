# chengyuchen1037/Arena-Agents

⭐ 3 · Python · MIT · 推送 2026-11-21 · [GitHub](https://github.com/chengyuchen1037/Arena-Agents) · 个人维护 · 中文 README

**AI 狼人杀多智能体博弈沙盒：LLM 玩家与主持人对局社交推理**

开源的多智能体社交推理沙盒：游戏规则写在可执行 Markdown 剧本中，引擎本身不含游戏概念，只提供频道、发言权、请求与只追加账本；12 名玩家与主持人均为异步 Agent（前台 Actor 收发消息、后台 Worker 思考与工具调用），由 LLM 主持人按手册推进流程。支持四层记忆与初始化/复盘学习循环、真人接管座位、历史重放、按局 token/费用预算、演示模式（无 API Key 体验完整一局）。通过 git clone 本机运行或 Docker Compose 部署，需要 Python 3.12 与至少一个 LLM Provider API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 规则写在可执行 Markdown 剧本，引擎与游戏概念解耦，可运行其他社交推理或桌游规则
- 每个角色为 Actor + Worker 异步 Agent，支持真人接管座位与 0.5×–8× 重放
- bot 具备四层记忆与初始化/复盘学习循环，基准套件可复现
- 支持 OpenAI Chat Completions/Responses、Anthropic Messages，多 Provider 多模型混用与按局预算上限

## 适用场景

- 运行 AI 狼人杀对局并以上帝视角或玩家视角观战
- 亲自接管一个座位与 agent 同场博弈
- 复现基准实验，量化 bot 发言风格差异与依据硬事实判断的能力
- 用同一引擎运行其他社交推理、剧本杀或桌游规则

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: **Arena-Agents 是一个开源的 AI 狼人杀、社交推理与多智能体博弈沙盒。** 游戏规则写在 Markdown
> L87: - **多 Provider / 多模型**：支持 OpenAI Chat Completions、OpenAI Responses、Anthropic
> L123: 引擎的核心只有一个想法：**每个角色（12 名玩家 + 主持人）都是一个异步 agent，由前台的 Actor 和后台的 Worker 两半组成。**


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `312ef3b54774` · [字段定义](../../DATASET.md)*
