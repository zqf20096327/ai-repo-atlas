# Amin-Moniry/n8n_ExecutiveBot_Platform

⭐ 14 · MIT · 推送 2026-05-31 · [GitHub](https://github.com/Amin-Moniry/n8n_ExecutiveBot_Platform) · 个人维护

**Telegram AI 自动化助手：经 n8n 接管 Gmail/Sheets/Drive 与本地模型**

构建于 n8n + Docker + WSL2 之上的 Telegram 机器人：将收到的消息经智能路由分派给邮件与数据双 AI Agent（Gemini 2.0 Flash 推理），支持自然语言发信与收信、Google Sheets 查询、Drive 浏览与存储分析、Python 代码执行，以及 Qwen 3:4B 经 Ollama 本地 GPU 加速的快速补全；PostgreSQL 持久化跨会话对话记忆，支持英语/波斯语双语。面向需要自托管 Google Workspace 自动化层的进阶用户与团队，需自行部署 WSL2、Docker、ngrok 与各服务凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双 Agent 架构：邮件 Agent 与数据 Agent 各配专属工具与推理模型
- Qwen 3:4B 经 Ollama Docker 容器本地 GPU 加速运行
- PostgreSQL 持久化跨会话对话记忆，双 Agent 共享记忆池
- 智能消息分类：按邮件/数据/代码关键词自动路由

## 适用场景

- 在 Telegram 里用自然语言收发 Gmail 邮件
- 对话式查询 Google Sheets 数据与浏览 Drive 文件
- 通过 Telegram 触发沙箱化 Python 代码执行
- 自托管一个 Google Workspace 自动化层

## 场景标签

`工作流自动化` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Amin's Smart Assistant** is an intelligent Telegram bot that connects Gmail, Google Drive, Google Sheets, and mult
> L5: The bot targets power users, developers, and teams who need a portable, self-hosted automation layer over their Goog
> L13: |Dual AI Agents|Email Agent and Data Agent — each with specialized tools and Gemini 2.0 Flash reasoning|✅|

## 星数曲线

```mermaid
xychart-beta
    title "Amin-Moniry/n8n_ExecutiveBot_Platform 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `81ab167aaf79` · [字段定义](../../DATASET.md)*
