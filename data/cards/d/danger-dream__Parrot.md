# danger-dream/Parrot

⭐ 22 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/danger-dream/Parrot) · 个人维护 · 中文 README

**多渠道 AI 协议代理网关，TG Bot 图形化管理上游账号**

把 Claude OAuth、ChatGPT Plus/Codex OAuth、Cursor/Qoder 订阅及第三方 API 统一抽象成渠道的代理服务：对外提供 Anthropic Messages、OpenAI Chat Completions/Responses、图片、视频与 MCP 入口，家族内协议互转；带评分调度、故障转移、错误冷却、会话亲和、OAuth 自动刷新与并发排队。管理面通过 Telegram Bot 图形面板完成，支持模型映射、统一模型名与配额监控。部署提供一键脚本、Docker Compose、Docker 直跑与源码四种方式。面向持有多个 AI 订阅账号并希望统一复用与管理的开发者。

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

- 三类上游渠道：Anthropic/OpenAI OAuth、Cursor/Qoder 订阅、第三方兼容 API
- 评分调度 + 故障转移 + 错误阶梯冷却 + 会话亲和 + 渠道并发限制
- Telegram Bot 全图形化配置：渠道、API Key、模型映射、网络设置
- Anthropic 与 OpenAI 家族内互转（SSE 双向状态机）

## 适用场景

- 把多个 Claude/ChatGPT/Cursor 订阅账号聚合成一个 API 端点供客户端调用
- 通过 Telegram Bot 在手机上管理渠道、模型映射与配额
- 为下游 SDK/CLI（Claude Code、Codex CLI）提供带故障转移的统一入口

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: **多家族、多渠道、故障转移的 AI 协议代理**
> L12: Parrot 的核心价值：**一个进程管住所有 AI 家族的上游复用**。你手上有一堆 Claude OAuth 账号、ChatGPT Plus OAuth 账号、Cursor 订阅账号、第三方 GLM / Codex Codin
> L20: |`POST /v1/messages`|Anthropic Messages API|Claude Code CLI、OpenClaw、任何 Anthropic SDK|

## 星数曲线

```mermaid
xychart-beta
    title "danger-dream/Parrot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6e4459adc1f1` · [字段定义](../../DATASET.md)*
