# blogminhquy/javis-os

⭐ 931 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/blogminhquy/javis-os) · [官网](https://javisos.com) · 个人维护 · 中文 README

**自托管 AI 工作队仪表盘：多模型协作、共享记忆与后台任务**

以 Python/Docker 自托管的 agentic 应用，把 Claude、ChatGPT、Gemini、Grok 等订阅式 CLI 与 API 作为可替换的"大脑"接入统一工具箱（MCP Hub、技能、后台任务）。核心机制是 Second Brain：Obsidian 兼容的 markdown 记忆库与知识图谱，每次学习提交为 git 可撤销记录，模型切换不迁移数据。支持语音、Telegram/Slack/WhatsApp 等多渠道对话、Kanban 任务、定时循环与多 agent 团队。README 提示订阅账号长时间后台运行存在被服务商封号的风险。

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

- 15 个模型提供方接入，Models 页面一键切换，记忆/技能/工作流保持不变
- Second Brain：markdown 记忆库 + 知识图谱，Obsidian 兼容，可同步 GitHub 私有仓库
- 后台工作：Kanban 任务、定时循环与提醒、多 agent 团队协作
- 语音输入输出、Telegram/Slack/WhatsApp/Zalo 等多渠道接入

## 适用场景

- 在自己的服务器上运行 24/7 的 AI 助手处理日常任务
- 把业务数据接入后让多个 agent 分工协作并定期汇报
- 随时切换底层模型而不丢失积累的记忆与配置

## 场景标签

`多智能体` `AI 助手` `知识库管理` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L7: Javis OS turns **Claude, ChatGPT, Gemini, Grok** and the models you choose into one 24/7 workforce on your own machi
> L57: Javis OS is **not** a chatbot. It is a **self-hosted agentic AI** that runs on your own machine or VPS: it reads an
> L111: Pick the brain on the **Models** page and change it whenever you like. Javis supports **15 providers** today.

## 星数曲线

```mermaid
xychart-beta
    title "blogminhquy/javis-os 星数(近 27 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 216 --> 996
    line [286, 330, 350, 371, 380, 401, 490, 513, 281, 714, 738, 743, 755, 764, 816, 826, 830, 839, 849, 853, 855, 884, 894, 906, 920, 926, 931]
```

2026-10-26 286 → 2026-11-28 931（+645）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `f7c6855b2f26` · [字段定义](../../DATASET.md)*
