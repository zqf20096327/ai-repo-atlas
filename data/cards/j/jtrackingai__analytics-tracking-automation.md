# jtrackingai/analytics-tracking-automation

⭐ 145 · TypeScript · Apache-2.0 · 推送 2026-04-29 · [GitHub](https://github.com/jtrackingai/analytics-tracking-automation) · [官网](https://www.jtracking.ai/skills) · 组织维护

**让 AI agent 规划并交付 GA4+GTM 埋点方案的技能包**

面向 Cursor、Codex 等 AI agent 的本地优先技能（skill）：通过自然语言对话驱动 agent 完成站点分析、按业务意图分组页面、起草 GA4 事件方案、对比现有 GTM 配置、生成 GTM 就绪产物并在发布前做预览验证，支持通用网站与 Shopify 店铺两条路径，产物按站点目录存档可断点续跑。浏览器步骤依赖 Playwright Chromium，GTM 同步使用 Google OAuth，运行时发送匿名启动信号，更丰富的诊断需用户显式选择加入。

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

- 对话驱动：站点分析→页面分组→事件方案→GTM 生成→预览验证的工作流
- 每个站点独立产物目录，支持断点恢复与只审计/只评审等范围控制
- 通用网站与 Shopify 店铺双路径
- 附 Playwright 调试命令（debug:open / debug:codegen）用于定位选择器问题

## 适用场景

- 让 agent 为新站点从零规划 GA4+GTM 埋点方案
- 审计现有 GTM 配置，判断修复还是重建
- 对已产出的埋点方案做日常维护与漂移检查
- 为 Shopify 店铺走专用埋点流程

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L12: `analytics-tracking-automation` is a local-first AI skill for planning, reviewing, and delivering GA4 + GTM trackin
> L2:  Works with Cursor · Codex · Any AI Agent

## 星数曲线

```mermaid
xychart-beta
    title "jtrackingai/analytics-tracking-automation 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29"]
    y-axis "stars" 143 --> 146
    line [144, 145, 145]
```

2026-10-18 144 → 2026-10-29 145（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `633dab71a253` · [字段定义](../../DATASET.md)*
