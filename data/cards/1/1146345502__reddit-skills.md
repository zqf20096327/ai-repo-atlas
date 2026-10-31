# 1146345502/reddit-skills

⭐ 16 · Python · MIT · 推送 2026-04-24 · [GitHub](https://github.com/1146345502/reddit-skills) · 个人维护

**让 AI agent 用真实浏览器账号操作 Reddit 的技能集**

面向 OpenClaw 及兼容 SKILL.md 格式的 agent 平台（如 Claude Code）的 Reddit 自动化技能集，含认证、发布、浏览、互动、复合操作五类技能，支持链式自然语言指令。通过 Chrome 扩展桥接用户已登录的浏览器与真实账号执行操作，另内置 MCP 服务器（16 个工具，兼容 Claude Desktop、Cursor 等客户端）与带 JSON 输出的 CLI。需 Python 3.11+、uv、Google Chrome，README 提示需控制操作频率以避免触发 Reddit 限流或账号限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 类技能：认证/发布/浏览/互动/复合操作，支持链式自然语言指令
- Chrome 扩展桥接，用真实浏览器登录会话执行操作
- 内置 MCP 服务器，暴露 16 个工具，兼容任意 MCP 客户端
- CLI 全功能可用，输出 JSON 供脚本调用

## 适用场景

- 让 AI agent 代我搜索、浏览和总结 Reddit 帖子
- 用自然语言指令批量执行发帖、评论、点赞等 Reddit 操作
- 通过 MCP 客户端（Claude Desktop/Cursor）接入 Reddit 自动化能力

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: Reddit automation Skills — directly uses your logged-in browser and real account, operating Reddit as an ordinary us
> L5: Supports OpenClaw and all AI Agent platforms compatible with the `SKILL.md` format (e.g. Claude Code).
> L100: reddit-skills includes a built-in Model Context Protocol server, making it compatible with any MCP client (Claude 

## 星数曲线

```mermaid
xychart-beta
    title "1146345502/reddit-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `13e1e46c2a89` · [字段定义](../../DATASET.md)*
