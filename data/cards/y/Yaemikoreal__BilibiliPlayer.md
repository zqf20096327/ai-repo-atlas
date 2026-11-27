# Yaemikoreal/BilibiliPlayer

⭐ 3 · JavaScript · MIT · 推送 2026-11-18 · [GitHub](https://github.com/Yaemikoreal/BilibiliPlayer) · 个人维护 · 中文 README

**给 AI Agent 用的B站 MCP Server：29 个工具本机操作B站**

一个跑在本机的 MCP Server（FastMCP/stdio），把B站 Web API 封装成 29 个工具，覆盖扫码登录、视频/评论/字幕/弹幕采集、热门与排行榜、动态与图文发布、单/多P投稿、评论点赞私信通知等读写操作。接入 Claude Code、Cursor、Cline、OpenClaw 等 MCP 客户端后可用自然语言调用；附 DeepSeek Harness 插件「B站分身」，按值班章程自动运营小号，值班轮仅暴露最小工具白名单。凭证存本地文件，不经过第三方服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 29 个 MCP 工具基于 bilibili-api-python，读写走B站 Web API 与官方扫码登录
- 本地运行，凭证写在本地文件且已在 .gitignore，无远程后端
- 支持批量操作内置请求间隔（0.3/0.5/1 秒）与 BILI_MCP_TOOLS 白名单限权
- 附 DSH 插件「B站分身」：看板 + 操作台 + 值班章程自动运营小号

## 适用场景

- 让 AI 搜索B站视频并总结 AI 字幕和评论区观点
- 通过对话发布动态、投稿视频、管理B站内容
- 批量采集关键词相关视频的评论与字幕做分析
- 用 DSH 插件按配额自动运营一个B站小号

## 场景标签

 · 领域:AI Agent 工具接入/社交媒体自动化

## 证据(README 行号)

> L5:  29 个 MCP 工具，一个跑在本机的 MCP Server —— 把B站变成 Agent 可调用的能力。
> L13: - 🤖 **Agent 拿来就能干活**：标准 MCP（stdio）接入 Claude Code / Cursor / Cline / OpenClaw；还附赠 DSH 插件「B站分身」——看板 + 操作台 + 值班章程，能让 A
> L149: 技术栈：MCP（Model Context Protocol） · FastMCP · `bilibili-api-python` · Python 3.10+；插件侧是纯 ESM 的 Node.js 模块，没有第三方运行时依赖


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `466e6771a58c` · [字段定义](../../DATASET.md)*
