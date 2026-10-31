# hexagon-codes/hexclaw-desktop

⭐ 30 · TypeScript · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/hexagon-codes/hexclaw-desktop) · [官网](https://hexclaw.net) · 组织维护 · 中文 README

**连接本机或云端 HexClaw 服务的 AI Agent 桌面工作台**

基于 Tauri 2 + Vue 3 + TypeScript 的桌面应用，连接应用管理的本机 HexClaw Agent 服务（Go Sidecar）或自部署的云端服务，由智能体调用模型、知识与工具完成工作。功能覆盖多轮对话与流式回答、智能体与场景模板、知识库（全文与向量检索）、Skill/MCP 工具集成、定时任务/Webhook/工作流自动化、IM 通道接入，以及面向小学的 K12 作业辅导（图片批改、错题积累、周练）。本地模型可使用 Ollama，在线模型通过 OpenAI、Anthropic、Gemini、DeepSeek、Qwen 等接入。限制：README 描述 v0.5.0 源码能力，文档更新不代表已发布；本机与云端服务数据不互通。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 桌面对话、已绑定 IM 通道与自动化任务均可发起 Agent 工作
- 知识库支持文档上传、处理状态管理与全文/向量检索
- K12 作业辅导：图片解题批改、错题学习档案、周练与学情报告
- 支持 Ollama 本地模型与 OpenAI/Anthropic/Gemini/DeepSeek/Qwen 等在线 Provider

## 适用场景

- 在桌面上一站式使用 AI 对话、知识库与工具自动化
- 为小学孩子建立作业辅导档案并获取带批注的批改图与周练
- 不依赖云端 API Key，用 Ollama 本地模型完成任务
- 通过 IM 通道或定时任务触发智能体工作

## 场景标签

`聊天机器人` `工作流自动化` `知识库管理` · 领域:效率与自动化

## 证据(README 行号)

> L13: HexClaw Desktop 用一个桌面应用连接 HexClaw Agent 服务。你可以直接使用应用管理的本机服务，也可以连接自己部署的云端服务；从桌面对话、已绑定的 IM 通道或自动化任务发起工作，由智能体调用模型、知识与工
> L261: |HexClaw Desktop（本仓库）|AI Agent 桌面工作台：连接本机或云端 HexClaw 服务，集成对话、知识库、工具、任务自动化与 K12 作业辅导|Tauri 2、Vue 3、TypeScript、Rust|

## 星数曲线

```mermaid
xychart-beta
    title "hexagon-codes/hexclaw-desktop 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30", "2026-10-31"]
    y-axis "stars" 27 --> 31
    line [28, 29, 30, 30]
```

2026-10-18 28 → 2026-10-31 30（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `06a9fb7074b2` · [字段定义](../../DATASET.md)*
