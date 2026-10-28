# arcmira/arcmira

⭐ 28 · TypeScript · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/arcmira/arcmira) · [官网](https://arcmira.com) · 组织维护

**Arcmira 官方 TypeScript SDK/CLI：搜索 YouTube 转录与品牌提及**

Arcmira 平台的官方 TypeScript/JavaScript SDK 与 CLI：通过 API 拉取 YouTube 转录文本（含时间戳）、按说话人/公司/频道/日期搜索语音片段、读取实体提及、频道赞助商与推荐内容，并支持设置公司提及监控（邮件/Slack/webhook 告警）。需 ARCMIRA_API_KEY，功能受积分与付费计划限制（免费 1,000 积分/月，付费自 $20/月起）。提供 MCP server 供 AI agent 接入，支持 Claude Code、Cursor 等。零运行时依赖，Node.js 18+。

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

- 带时间戳的 YouTube/播客转录文本搜索与拉取
- 公司提及监控与邮件/Slack/webhook 告警
- 实体提及、频道赞助商、有机推荐查询
- MCP server 供 AI agent 调用（npx arcmira setup）

## 适用场景

- 调研某公司或产品在 YouTube/播客中被提及的内容
- 为 AI agent 接入带时间戳的转录搜索能力
- 监控自家或竞品公司的媒体提及与告警

## 场景标签

 · 领域:媒体监测/搜索服务

## 证据(README 行号)

> L3: Pull YouTube transcripts, search spoken passages, and monitor company mentions with Arcmira. Results include timesta
> L97: For tasks such as "pull YouTube transcripts", "find quotes with timestamps", "research podcast sponsors", or "monit
> L122: Zero runtime dependencies. Node.js 18+ supports ESM and CommonJS. Deno installation. For Workers, pass your API ke

## 星数曲线

```mermaid
xychart-beta
    title "arcmira/arcmira 星数(近 3 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-28"]
    y-axis "stars" 27 --> 32
    line [31, 28, 28]
```

2026-10-22 31 → 2026-10-28 28（-3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2681432cc4a8` · [字段定义](../../DATASET.md)*
