# robbyczgw-cla/web-search-plus

⭐ 25 · Python · MIT · 推送 2026-10-10 · [GitHub](https://github.com/robbyczgw-cla/web-search-plus) · [官网](https://websearchplus.xyz) · 个人维护

**面向 OpenClaw agent 的多源网页搜索与 URL 抽取 CLI 技能**

以 Python 脚本 CLI 形式提供的 OpenClaw skill：聚合 11 个搜索服务商（Brave/Serper/Exa/Tavily/Linkup/Firecrawl/You.com/SearXNG 等）与 7 个抽取服务商，按查询类型自动路由并逐级降级重试；输出排序链接与页面文本，不产出模型生成的回答。支持研究模式（并发多服务商查询、跨源去重）、质量报告、本地缓存、SSRF 防护与隐私披露。自 5.0.1 起内置 hermes 引擎，与主线引擎同版本发布；敏感查询可用 --provider 显式指定服务商。给构建 agent 工作流的开发者使用。

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

- 11 个搜索服务商按查询类型自动路由并逐级降级
- URL 抽取链（Tavily→Exa→Linkup→Firecrawl→You→Keenable→Serper）自动重试
- 研究模式并发多服务商查询、跨源去重与 top source 抽取
- SSRF 防护、本地缓存与 owner-only 权限的隐私处理

## 适用场景

- 为 OpenClaw agent 工作流提供统一的多服务商网页搜索
- 对多个 URL 做文本抽取并获得逐 URL 成功/错误结果
- 研究模式下并发查询多个搜索源并合并排序结果

## 场景标签

`网页抓取` `语义搜索` · 领域:效率与自动化

## 证据(README 行号)

> L5: Unified multi-provider web search and URL extraction for OpenClaw-style agent workflows.
> L9: > **Status: stable OpenClaw skill — compatibility path, not the main engine-development path.**

## 星数曲线

```mermaid
xychart-beta
    title "robbyczgw-cla/web-search-plus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-26 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c6093a2cf716` · [字段定义](../../DATASET.md)*
