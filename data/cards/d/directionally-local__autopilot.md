# directionally-local/autopilot

⭐ 177 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/directionally-local/autopilot) · [官网](https://directionallylocal.com/autopilot) · 组织维护

**开源终端编码 agent 与 SDK，自带密钥接入 25+ 供应商**

终端中的编码 agent，以 bring-your-own-key 方式把每次模型调用直接发到用户选择的供应商（OpenRouter、OpenAI、Anthropic、DeepSeek、Ollama/LM Studio 本地模型或任意 OpenAI 兼容端点），不做代理或加价。功能含 plan/edit/auto 三档权限模式、沙箱子代理、LSP+MCP、SQLite 跨会话记忆、网页/GitHub/无头浏览器研究、逐轮计费显示与 headless SDK（createAgentSession / JSONL-over-stdio）。面向在自己硬件上运行编码 agent 的开发者，npm/Homebrew/npx 安装，需 Node.js 22.23.4+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 25+ 供应商接入，支持 OpenRouter、Anthropic、OpenAI、Bedrock、Vertex、Ollama/LM Studio 本地模型及任意 OpenAI 兼容端点
- plan/edit/auto 三档权限模式，含凭据文件读取与内网地址访问的注入防护
- 沙箱子代理与无人值守长任务（检查点恢复、运行时/token/成本/动作预算）
- headless SDK：createAgentSession API 与 JSONL-over-stdio RPC 模式

## 适用场景

- 在终端里用自己供应商的 key 让 agent 读写代码、跑命令、做研究
- 本地 Ollama/LM Studio 模型驱动编码 agent
- 通过 SDK 把 autopilot 的 agent 会话嵌入自己的程序或 CI 长任务

## 场景标签

`编码 Agent` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L13:  A terminal coding agent that runs on your own provider key.
> L20: autopilot sends every model call to **the provider you choose** using **your own key** — bring-your-own-key, nothin
> L52: - **Headless SDK** — Programmatic `createAgentSession` API and JSONL-over-stdio RPC mode for building on top of aut


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7211a6e82dae` · [字段定义](../../DATASET.md)*
