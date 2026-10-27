# 2001Haru/CloseClaw

⭐ 33 · Python · MIT · 推送 2026-03-31 · [GitHub](https://github.com/2001Haru/CloseClaw) · 个人维护 · 中文 README

**安全优先的 OpenClaw 式个人 Agent 框架，支持多渠道自动化**

基于 Python 的轻量级 Agent 编排框架，提供 CLI、Telegram、飞书/Lark、Discord、WhatsApp、QQ 等渠道接入，内置守护者审查机制、工作区路径沙箱、Windows 受限令牌 OS 级沙箱、心跳与 Cron 定时任务及结构化长期记忆。LLM 侧支持 openai/openai-compatible 原生路径，Gemini 与 Anthropic 经 LiteLLM 运行（需安装 .[providers] 扩展）。兼容 OpenClaw 技能与 MCP 工具扩展，提供 git clone + pip 可编辑安装与可选 Docker Compose 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Guardian Agent 审查高风险连接操作（邮箱/云仓库/第三方 API/MCP 内容）
- PathSandbox 工作区边界 + Windows 受限令牌/低完整性 OS 级沙箱
- 心跳与 Cron 服务支持定时任务与周期性唤醒
- MCP 原生扩展，兼容 OpenClaw 技能与工具

## 适用场景

- 通过 Telegram 等聊天渠道运行个人自动化 Agent
- 定时执行新闻采集等 24/7 周期任务
- 在沙箱约束下让 Agent 执行文件与 Shell 操作
- 通过 MCP 接入自定义工具服务器扩展 Agent 能力

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L15: > 🔥 **CloseClaw** is a lightweight, security-focused and practical OpenClaw-style Python framework. It is an person
> L42: - Supporst MCP-Native Extensibility, Being compatible with any OpenClaw skills and tools. Massive ecosystem. Easy t

## 星数曲线

```mermaid
xychart-beta
    title "2001Haru/CloseClaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-27 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `570a5c18d8b1` · [字段定义](../../DATASET.md)*
