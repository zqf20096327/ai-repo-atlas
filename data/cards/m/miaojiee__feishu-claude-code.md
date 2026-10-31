# miaojiee/feishu-claude-code

⭐ 25 · Shell · MIT · 推送 2026-05-24 · [GitHub](https://github.com/miaojiee/feishu-claude-code) · 个人维护 · 中文 README

**把 Claude Code 接入飞书聊天的部署方案：手机指挥云服务器写代码**

一套教程型仓库：用 cc-connect 做消息桥接，把 Claude Code 终端助手接入飞书机器人，用户在聊天框以自然语言指挥云服务器执行代码、处理文件、生成报告；模型侧通过 Anthropic 兼容端点接入 DeepSeek API 降低成本。提供一键安装脚本与手动安装文档，覆盖飞书机器人配置、npm 淘宝镜像、systemd 守护、Cron 定时任务、多项目隔离与 MCP 扩展。面向有云服务器与飞书管理员权限的开发者/个人用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- cc-connect 桥接飞书与 Claude Code，手机端即可操控云服务器
- DeepSeek 经 Anthropic 兼容端点替代官方 API，全链路国内直连
- 一键安装脚本（git clone + install.sh）自动处理 npm 淘宝镜像
- 支持多项目隔离（多飞书群映射多工作目录）、Cron 定时任务与 MCP 工具链扩展

## 适用场景

- 在手机飞书里随时指挥 AI 在服务器上写代码、跑脚本
- 国内网络环境下低成本部署 Claude Code 工作流
- 把数据处理规范沉淀为 AI 记忆，上传文件自动跑全流程

## 场景标签

`编码 Agent` `教程课程` · 领域:编码与开发

## 证据(README 行号)

> L29: **核心思路**：飞书 = 交互入口 → cc-connect = 消息桥接 → Claude Code = 执行引擎 → DeepSeek API = AI 大脑。
> L178: - cc-connect — 消息平台桥接框架
> L179: - Claude Code — Anthropic 的 AI 编程 CLI

## 星数曲线

```mermaid
xychart-beta
    title "miaojiee/feishu-claude-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `10fd02af6159` · [字段定义](../../DATASET.md)*
