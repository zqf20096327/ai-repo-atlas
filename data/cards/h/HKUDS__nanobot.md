# HKUDS/nanobot

⭐ 49,146 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/HKUDS/nanobot) · [官网](https://nanobot.wiki) · 组织维护 · 中文 README

**给个人用户的自托管轻量 AI agent 框架**

以 Python 编写的自托管个人 AI agent 框架：提供浏览器 WebUI、终端 TUI 及 Telegram/Discord/Slack/微信/邮件等聊天渠道接入，内置文件读写、shell、网页搜索/抓取、MCP、定时任务、图像生成与多 agent 委派，通过 Dream 保存会话历史与长期记忆，并暴露 Python SDK 与 OpenAI 兼容 API。需自备模型供应商账号或本地模型服务，框架本身不提供模型。通过安装脚本、uv/pip 安装 PyPI 包或源码检出运行。

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

## 动量与使用信号

- 维护:`active` — 距上次 push 0.6 天,年发版 20,389 位贡献者
- 涨星:近 1 天 **+47**(自 20261016 起算)
- 安装:pypi 包 `nanobot-ai` 月下载 47,015
- 平台:WEB · 协议:OPENAI-API / MCP / OLLAMA

## 能力要点

- WebUI、终端 TUI 与多聊天渠道接入
- 内置文件工具支持读取 PDF/Word/Excel/PowerPoint
- 通过 Dream 保存长期记忆，支持长时目标与定时自动化
- 暴露 Python SDK 与 OpenAI 兼容 API

## 适用场景

- 自托管一个能操作文件、执行定时任务的私人 AI 助手
- 通过 Telegram/Discord/微信等聊天软件与个人 agent 交互
- 在服务器上部署长期运行的 agent 网关并通过 SSH 访问 WebUI

## 场景标签

`Agent 框架` `Agent 记忆` `多智能体` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L28: 🐈 **nanobot** is an ultra-lightweight, open-source, self-hosted personal AI agent framework written in Python. Use 
> L49: - connect to Telegram, Discord, Slack, WeChat, Email, Mattermost, Linear, and other channels
> L61: - **Model freedom**: OpenAI-compatible APIs, local LLMs, image generation, search, and fallbacks.

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 mid · 依据 README sha `c95912f4fb26` · [字段定义](../../DATASET.md)*
