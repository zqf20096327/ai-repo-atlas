# Shaivpidadi/FreeRideV3

⭐ 54 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/Shaivpidadi/FreeRideV3) · [官网](https://free-ride.xyz) · 个人维护

**开发者：本地 OpenAI 兼容网关，聚合免费层推理并自动故障转移**

FreeRide 是运行在 localhost:11343 的本地推理网关，把请求路由到 OpenRouter、Gemini、Groq、NVIDIA NIM、Cloudflare Workers AI、Ollama（含 Ollama Cloud）等免费层提供方，按 (provider, key) 健康度排序做自动故障转移与多 key 轮换，支持密钥冷却与模型级降级。对外提供 OpenAI、Anthropic /v1/messages、Responses、Gemini 等多种协议，可包装 Claude Code/Codex/Gemini CLI；另一形态 ridex 是基于 fx 分支的编码 agent。密钥仅存本机 ~/.freeride/.env。安装为 curl 脚本，macOS/Linux/Windows 可用（agent 仅 macOS+Linux）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨十余家免费层提供方的自动故障转移链（密钥级/模型级/配额级分级处理）
- 本地 OpenAI 兼容端点，另原生支持 Anthropic、Responses、Gemini 线协议
- 每提供方多 key 轮换，429 后冷却 60 秒切换
- freeride run 命令包装 Claude Code/Codex/Gemini CLI，无需厂商登录

## 适用场景

- 让 Aider、Continue.dev、LangChain 等工具走一个本地免费推理端点
- 不付订阅费获得多提供方冗余的编码 agent 推理
- 免费层被限流时自动切换提供方继续会话

## 场景标签

`模型网关` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: FreeRide routes requests across free-tier providers — **OpenRouter, Google Gemini, Ollama Cloud, Z.ai, Groq, NVIDIA 
> L29: A local, OpenAI-compatible endpoint on `localhost:11343` that any agent, SDK, or script can point at — Aider, Conti
> L41: It also natively serves the **Anthropic** (`/v1/messages`), **OpenAI Responses** (`/v1/responses`), **Gemini** (`:g

## 星数曲线

```mermaid
xychart-beta
    title "Shaivpidadi/FreeRideV3 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-26 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fa2bba2dbf2b` · [字段定义](../../DATASET.md)*
