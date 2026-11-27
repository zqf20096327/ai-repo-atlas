# lian84/memora

⭐ 5 · TypeScript · AGPL-3.0 · 推送 2026-11-26 · [GitHub](https://github.com/lian84/memora) · 个人维护

**自托管的文件优先个人 AI 助手，基于 Pi 构建**

基于 Pi agent 引擎的自托管个人助手，提供流式聊天、Markdown 第二大脑（附可重建的 SQLite 索引）、需人工审批的记忆收件箱、项目与版本化产物、带编号引用的网络检索、定时自动化和可选 Telegram 投递。默认单用户本地/局域网部署，公开暴露要求 HTTPS 与反向代理。需要 Node.js 24 与 pnpm，提供 git clone、pnpm 及 systemd install.sh 安装路径。v0.1.4 的恢复/更新/回滚验证仍在进行中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Markdown 为权威来源的第二大脑与可重建 SQLite/FTS5 索引
- 记忆收件箱默认需人工审批，可选本地嵌入语义检索
- PDF/DOCX/XLSX/PPTX 生成不依赖 LibreOffice
- 定时自动化支持 cron/时区与可选 MCP 访问

## 适用场景

- 在家庭服务器上自托管一个私人 AI 助手
- 把笔记和文档整理成可检索的 Markdown 第二大脑
- 定时运行自动化任务并把结果推送到 Telegram

## 场景标签

`AI 助手` `知识库管理` `语义搜索` · 领域:对话与助手

## 证据(README 行号)

> L26: Memora is a self-hosted personal assistant built on
> L64: - Streaming chat, persistent Pi sessions and background turns.
> L68: - Memory Inbox with explicit approval by default and optional auto-save; optional LLM Memory Curator.

## 星数曲线

```mermaid
xychart-beta
    title "lian84/memora 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 2 --> 6
    line [3, 5]
```

2026-11-26 3 → 2026-11-27 5（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `a76b06a2ac29` · [字段定义](../../DATASET.md)*
