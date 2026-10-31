# crossoverJie/skills

⭐ 19 · Python · Apache-2.0 · 推送 2026-07-01 · [GitHub](https://github.com/crossoverJie/skills) · 个人维护 · 中文 README

**面向 Claude Code/Codex 等 agent 的个人技能合集（8 个）**

遵循 Agent Skills 规范的 AI agent 技能集合，收录 8 个技能：图床上传（sm.ms/Imgur/GitHub+jsDelivr）、渐变封面生成、博客封面自动化、会话导出 Markdown、多渠道 agent 通知（含 Telegram/钉钉等）、剪贴板管理 CLI、StarRocks 升级兼容性对比（11 个扫描器）、gRPC+Java 项目 Wiki 生成。通过 npx skills CLI 一键安装，自动检测 Claude Code、Codex、Cursor 等 agent 并安装到对应位置，也可 git clone 后手动复制安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个技能：图床上传、封面生成、会话导出、agent 通知等
- npx skills CLI 自动检测目标 agent 并安装到正确位置
- StarRocks 升级工具含 11 个兼容性扫描器与四阶段并行分析
- Agent Notifier 支持 7 类通知渠道（声音/macOS/Telegram/邮件/Slack/Discord/钉钉）

## 适用场景

- 给 Claude Code/Codex/Copilot CLI 装 image-uploader 之类技能处理博客图片
- agent 执行长任务时通过钉钉/Telegram 收到完成或等待输入通知
- 用 agent 对 StarRocks 两个版本做升级兼容性对比

## 场景标签

 · 领域:AI agent 工具/技能

## 证据(README 行号)

> L3: A collection of useful skills for AI agents (like Claude Code/ Codex/ GitHub Copilot CLI), following the Agent Skill
> L37: The CLI automatically detects your agent (Claude Code, Codex, Cursor, etc.) and installs to the correct location.

## 星数曲线

```mermaid
xychart-beta
    title "crossoverJie/skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `8b94422607eb` · [字段定义](../../DATASET.md)*
