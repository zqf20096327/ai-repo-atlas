# Colton-z/AstraBox

⭐ 15 · Python · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/Colton-z/AstraBox) · [官网](https://www.astrabox.ai) · 个人维护 · 中文 README

**自托管平台：将 Claude Code、Codex 等 Agent 程序作为云端 Agent 运行**

AstraBox 是开源（Apache-2.0）自托管的 Agent 运行平台：在自有基础设施的沙箱中运行 Claude Code、Codex、DeepSeek Harness、pi 与 Hermes 等真实 Agent 程序，统一处理沙箱、流式输出、会话状态与凭据；内置 LiteLLM 模型网关（支持 Anthropic、OpenAI 兼容及本地提供方）、Casdoor 团队登录、OpenSandbox（Docker/K8s）、Vault 凭据保护。提供 Web 控制台、HTTP API、CLI、MCP 工具及 Slack/Discord/Telegram 等消息渠道触发。一条 curl 命令在 Linux/WSL 2（需 Docker Engine 26+）上安装部署，各组件以 Python 插件扩展点替换。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在隔离沙箱中运行真实 Agent 程序（Claude Code/Codex/DeepSeek Harness/pi/Hermes）
- 内置 LiteLLM 模型网关，支持 Anthropic、OpenAI 兼容与本地提供方
- 沙箱丢失后从平台数据库恢复原生会话
- 提供 Web 控制台、CLI（含 MCP 工具、配置即代码）、Webhook 与消息平台触发

## 适用场景

- 团队在自有服务器上把 Claude Code 等 Agent 程序跑成可复用的云端 Agent
- 通过 Slack/Discord/Telegram 或定时任务触发 Agent 执行任务
- 为 Agent 任务提供隔离沙箱与凭据保护的企业化部署

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L23: AstraBox runs the Agent programs you already use (Claude Code, Codex,
> L24: DeepSeek Harness, Pi and Hermes) as cloud Agents on your own infrastructure,
> L26: sandboxes, streaming, state and credentials, so you do not have to turn an

## 星数曲线

```mermaid
xychart-beta
    title "Colton-z/AstraBox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0c778d078fb8` · [字段定义](../../DATASET.md)*
