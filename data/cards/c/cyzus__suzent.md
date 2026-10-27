# cyzus/suzent

⭐ 67 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/cyzus/suzent) · [官网](https://suzent.com/) · 个人维护 · 中文 README

**本地优先的个人 AI agent：自持记忆、权限与模型选择**

开源的本地优先个人 AI agent 桌面/移动应用：以磁盘上的追加式 Markdown 文件作为记忆载体，可切换 GPT、Claude、Gemini、DeepSeek 或 Ollama 本地模型而不丢失记忆。工具调用经过权限模式、路径限制与人工审批，代码可在可选 Docker 沙箱中运行。支持目标、定时任务、子代理、SKILL.md 技能包、MCP 扩展、GitHub Sync 同步，并接入 Telegram/Slack/Discord/飞书/微信等聊天渠道。安装脚本自动检测网络并切换大陆镜像。后端 Python 3.12 + FastAPI + litellm，前端 React + Tauri。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 记忆为用户可读写的追加式 Markdown，LanceDB 索引可随时重建
- 工具调用经权限模式、路径限制与人工审批，可选 Docker 沙箱隔离
- 支持目标/定时任务/子代理等跨回合自动化与会话检查点回滚
- 接入 Telegram、Slack、Discord、飞书、微信等聊天渠道，移动端为预览版

## 适用场景

- 拥有一个记忆和配置由自己掌控、可换模型不被平台绑定的个人 AI 助手
- 让 agent 在权限边界内执行研究、写作、编码与定时任务
- 通过已用的聊天软件与同一个 agent 对话，多端共享记忆

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L9: An open-source, local-first personal AI agent whose memory, authority, runtime, and continuity stay yours.
> L21: **SUZENT** [soo-zuh-nt] keeps an agent's identity, memory, skills, workspace, and runtime under your control. Use G

## 星数曲线

```mermaid
xychart-beta
    title "cyzus/suzent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-27 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `156aaf2a6194` · [字段定义](../../DATASET.md)*
