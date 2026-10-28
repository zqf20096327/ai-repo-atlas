# fseixas/super-geo-agent-readiness

⭐ 26 · 推送 2026-06-26 · [GitHub](https://github.com/fseixas/super-geo-agent-readiness) · 个人维护

**面向 Claude 的 GEO 与 Agent 就绪优化技能包**

一个 Claude Skill（SKILL.md 路由 + references 参考库），覆盖生成式引擎优化（GEO）与站点 agent 就绪：内容可引用性模式、llms.txt/Schema.org/robots.txt 技术配置、按引擎（ChatGPT/Perplexity/Google AI Overviews 等）的校准策略，以及 MCP Server Cards、OAuth 元数据、x402 等 agent 接入规范。证据来自 Ahrefs 14 项研究与 ChatGPT 网络流量分析，并注明单项研究与相关性数据的局限。安装方式为 Claude.ai 上传 .skill 包或 Claude Code 克隆到 skills 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SKILL.md 路由 + references 参考库的组织结构
- 整合 Ahrefs 14 项研究（约 10 亿数据点）与 ChatGPT 流量分析证据
- 覆盖内容/技术/平台/agent 就绪四个优化面
- 包含 MCP Server Cards、OAuth RFC 8414/9728、x402 等 agent 协议就绪项

## 适用场景

- 让 Claude 审计我的网站在 AI 引擎中的可见性
- 为站点生成 llms.txt 与 AI 爬虫 robots.txt 配置
- 按引擎制定 GEO 内容策略以获得 AI 回答引用

## 场景标签

 · 领域:AI 搜索优化/知识技能包

## 证据(README 行号)

> L3: A Claude Skill that covers Generative Engine Optimization (GEO) and agent readiness in one place. SEO targeted blue 
> L54: super-geo-agent-readiness/
> L55: ├── SKILL.md                              Router. Picks the right reference for the task.

## 星数曲线

```mermaid
xychart-beta
    title "fseixas/super-geo-agent-readiness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1d5565224db2` · [字段定义](../../DATASET.md)*
