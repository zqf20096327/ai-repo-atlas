# mdowis/anansi

⭐ 118 · Python · Apache-2.0 · 推送 2026-09-02 · [GitHub](https://github.com/mdowis/anansi) · 个人维护

**自愈式网页爬虫：选择器自修复、隐身浏览器与反检测身份层，附 MCP 服务器**

面向对抗性网站的 Python 爬虫框架：CSS 选择器带置信度评分，失效时由四种修复策略竞争并持久化胜者；检测到 JS 空壳时静默切换到隐身 Playwright 浏览器；提供 TLS/HTTP-2 指纹、persona 与请求头一致的拟真身份，含 Cloudflare/Akamai/DataDome 针对性处理；重爬时按 ETag/内容哈希等跳过未变页面；可用 Pydantic item_schema 校验数据。内置 FastMCP 服务器暴露 17 个工具，供 Claude Code、Cursor、ChatGPT 等 LLM 客户端通过对话驱动完整爬取。Apache 2.0 许可，需 Python 3.11+，README 提示使用需遵守目标网站条款与法律。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CSS 选择器自愈：四种修复策略竞争并持久化结果
- 按需静默切换隐身 Playwright 浏览器渲染（按域名缓存）
- 一致性反检测身份：TLS 指纹+persona+请求头，针对 Cloudflare/Akamai/DataDome
- FastMCP 服务器暴露 17 个工具，任意 LLM 可通过对话驱动爬取

## 适用场景

- 抓取结构频繁变动或对抗爬虫的网站并长期维护采集管线
- 让 Claude Code/Cursor 等 LLM 客户端通过对话执行抓取、提取与截图
- 对抓取数据用 Pydantic schema 做入库前校验

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L20: Ships with an **MCP server** so any LLM can drive a full crawl through conversation.
> L29: - **Driveable by any LLM** — a FastMCP server exposes 17 tools so an agent can fetch, extract, crawl, and screensho
> L58: Anansi ships a FastMCP server exposing 17 scraping tools over stdio or SSE, so an

## 星数曲线

```mermaid
xychart-beta
    title "mdowis/anansi 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 116 --> 119
    line [117, 118, 118]
```

2026-10-18 117 → 2026-10-29 118（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `eb14ba98baa6` · [字段定义](../../DATASET.md)*
