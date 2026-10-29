# liuboacean/mubu-integration

⭐ 18 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/liuboacean/mubu-integration) · [官网](https://clawhub.ai/liuboacean/skills/mubu-integration) · 个人维护 · 中文 README

**幕布大纲的命令行与 AI Agent Skill：Markdown 无损导入导出**

面向幕布（Mubu）用户的非官方 Python 集成工具：通过幕布 Web 端相同 HTTPS 接口（JWT 认证、令牌自动刷新）实现 Markdown 与幕布文档的无损双向转换（标题、复选框、备注保留），并支持 OPML/FreeMind 导出与整树批量操作。既可作为 CLI 使用（20+ 子命令），也可作为 AI Agent Skill 安装，让 Agent 直接读写幕布作为结构化记忆。限制：折叠状态、有序列表、图片附件不在 round-trip 内，无双向同步。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Markdown⇄幕布无损 round-trip（diff 无差异）
- OPML/FreeMind 导出与整树批量操作
- 可作为 AI Agent Skill 安装，Agent 直接读写幕布
- 115 个 pytest 用例 × 4 个 Python 版本的 CI 矩阵

## 适用场景

- 让 AI Agent 把幕布当作长期结构化记忆直接读写
- Obsidian 与幕布之间以 Markdown 双向搬运大纲
- 命令行批量备份/归档幕布文档

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L14: Manage your Mubu (幕布) outlines from the command line — **and as an AI Agent Skill** — with lossless Markdown import
> L39: **① Let your AI Agent read & write Mubu directly** — turn Mubu into your Agent's long-term, structured memory.
> L118: mubu-integration is an **unofficial** integration that uses the same endpoints as the Mubu web client. All request

## 星数曲线

```mermaid
xychart-beta
    title "liuboacean/mubu-integration 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `68467f93f18e` · [字段定义](../../DATASET.md)*
