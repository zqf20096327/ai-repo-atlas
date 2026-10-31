# yc-software/minecraft-agent-harness

⭐ 63 · JavaScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/yc-software/minecraft-agent-harness) · 组织维护

**在 Minecraft 中运行 LLM agent 的 harness，含持久会话与沙箱**

面向开发者的 Node.js 框架：将 LLM agent 接入 Minecraft Java 服务器，通过 Mineflayer 让 agent 走路、挖掘、合成、建造、战斗与聊天。支持 Claude、GPT、Gemini、OpenRouter 及 OpenAI Responses API 兼容端点；会话状态存于 .agent-state/，重启后同名 agent 可续接。每个 agent 配备 shell 沙箱（E2B/Docker/本地文件夹），支持多 agent 团队与 DM 通信，曾以 50 个 agent 同时运行生存服务器。附带 Paper 开发服务器（需 Java 21）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 Mineflayer 让 LLM agent 在 Minecraft 中执行完整玩家行为
- 会话状态持久化，重启后同名 agent 续接会话
- 每个 agent 有 shell 沙箱（E2B/Docker/本地文件夹）
- 单 JSON 文件配置多 agent 团队，支持 agent 间 DM

## 适用场景

- 让 LLM agent 在自己的 Minecraft 服务器上完成指定目标
- 搭建多 agent 团队并观察其协作与通信
- 研究 agent 长期会话与沙箱内脚本编写行为

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L18: Point an LLM at a Minecraft server and give it something to do. It plays through
> L25: - Claude, GPT, Gemini, OpenRouter, or your own endpoint if it speaks the OpenAI Responses API
> L27: - A shell for every agent (Docker, E2B or a plain local folder). Agents keep notes there and write little scripts t


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f8386daf66c3` · [字段定义](../../DATASET.md)*
