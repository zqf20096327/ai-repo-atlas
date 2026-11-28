# squirrelscan/squirrelscan

⭐ 339 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/squirrelscan/squirrelscan) · [官网](https://squirrelscan.com) · 组织维护

**为编码 agent 提供网站 QA 审计的 CLI 工具**

开源 CLI 工具，对网站执行 SEO、性能、安全、无障碍与 agent 体验（AX）审计，覆盖 360+ 条规则、22 个类别，输出健康评分、问题排序与可直接粘贴给编码 agent 的修复提示。可通过 CLI、MCP 服务器（托管/本地）、skills 或 API 运行，支持 Claude Code、Cursor、Codex、opencode 等编码 agent 的接入；提供 JSON/HTML/Markdown/LLM 等多种输出格式，并有云端定时审计、链接监控与浏览器渲染等付费功能。

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

- 360+ 条审计规则覆盖 22 个类别（SEO/安全/无障碍/性能等）
- Agent Experience 类别审计 llms.txt、AGENTS.md、AI 爬虫内容一致性
- 以 MCP 服务器、skills 和插件形式接入多种编码 agent
- 单二进制、零依赖 CLI，支持 JSON/HTML/Markdown/LLM 等输出格式

## 适用场景

- 让编码 agent 自动完成网站审计、修复与复审循环
- 上线前检查网站的 SEO、安全头与无障碍合规问题
- 评估网站对 AI 爬虫与 agent 的可读性

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: squirrelscan is an Open Source cli tool that audits websites for SEO, performance, security, accessibility, agent ex
> L28: - **Built for coding agents** - Skills for Claude Code, Cursor, Codex and any coding agent run the audit, fix and r
> L31: - **Agent experience** - Audit how well AI agents can read, discover and act on your site: llms.txt, AGENTS.md, Mar

## 星数曲线

```mermaid
xychart-beta
    title "squirrelscan/squirrelscan 星数(近 21 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-13", "2026-11-15", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 292 --> 343
    line [296, 298, 299, 300, 301, 296, 308, 310, 311, 312, 313, 314, 316, 317, 320, 321, 330, 334, 336, 337, 339]
```

2026-10-26 296 → 2026-11-28 339（+43）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `4ab382984b34` · [字段定义](../../DATASET.md)*
