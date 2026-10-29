# lupikovoleg/instagram-cli

⭐ 44 · Python · 推送 2026-07-02 · [GitHub](https://github.com/lupikovoleg/instagram-cli) · 个人维护

**终端 Instagram 分析下载 CLI，含自然语言 Agent 与 MCP 服务**

基于 HikerAPI 的 Instagram 数据工具，以 Python CLI、Python 库和本地 MCP 服务器三种形式提供：支持主题搜索（多语言 reels、深度分页）、按新鲜度过滤、抓取主页/评论/粉丝等统计、下载 reels 与故事、导出 csv/json。CLI 模式经 OpenRouter 做自然语言工具调用；MCP 模式供 Claude 等 MCP 客户端接入且不依赖 OpenRouter。需 macOS/Linux、Python 3.10+ 及 HikerAPI 密钥。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 搜索->检查->排序->导出的链式工作流
- 同一能力层以 CLI / Python 库 / MCP 服务器三种形式暴露
- 自然语言交互经 OpenRouter 实现工具调用
- 下载 reels、帖子、音频、故事与精选集合并导出 csv/json

## 适用场景

- 用自然语言在终端查询和导出 Instagram 数据
- 给 Claude 等 MCP 客户端接入 Instagram 数据能力
- 在自己的 Python 项目中嵌入 Instagram 数据抓取

## 场景标签

`网页抓取` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: Terminal-first Instagram analytics, downloads, and MCP tools powered by HikerAPI, OpenRouter, and FastMCP.
> L36: - Support natural-language interaction with tool calling in the CLI
> L41: - Expose the same capability layer through a local MCP server for Claude and other MCP clients

## 星数曲线

```mermaid
xychart-beta
    title "lupikovoleg/instagram-cli 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-29 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `b4e0e08d99fa` · [字段定义](../../DATASET.md)*
