# followanton/sleepwalker

⭐ 25 · JavaScript · MIT · 推送 2026-07-30 · [GitHub](https://github.com/followanton/sleepwalker) · [官网](https://www.sleepwalker.ai) · 组织维护

**面向品牌团队的 AI 可见性监测工具，追踪 AI 搜索中的回答与引用**

Sleepwalker 提供两大工作流：AI Visibility（在 ChatGPT、Perplexity、Grok、Gemini 上运行提示词，捕获回答、引用、竞争对手与提及类型）与 Content Intelligence（序列化公开页面、评估内容深度与新鲜度、返回建议）。可通过 App、公共 API、MCP 客户端与 CLI 使用，结果在各入口间互通。本仓库为公共开发者界面（CLI、API 示例、MCP 配置）；托管引擎与应用源码闭源，付费按积分计费。免费功能 okf export 在本地将公开页面导出为 AI 可读的 markdown 捆绑包，含内容与技术快照，无需账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨 ChatGPT/Perplexity/Grok/Gemini 运行提示词并捕获回答、引用与提及类型
- okf export 本地免费导出页面为 OKF markdown 捆绑（内容+AI 爬虫视角技术快照）
- App/API/MCP/CLI 四种访问路径，结果互通
- 付费按积分：可见性检查、内容评分与序列化消耗积分，读取类操作不计费

## 适用场景

- 监测品牌在各大 AI 搜索中的出现方式与引用来源
- 审计页面对 AI 爬虫的可读性（结构化数据、robots、meta 等）
- 把公开页面导出为 agent 可读的 markdown 供检索管线使用
- 通过 MCP 客户端（如 Claude）构建品牌监测自动化

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L22: - **AI Visibility**: run prompts across ChatGPT, Perplexity, Grok, and Gemini; capture full answers, citations, com
> L94: - **AI search (GEO) monitoring**: set up prompt tracking for specific URLs across ChatGPT, Perplexity, Grok, and Ge

## 星数曲线

```mermaid
xychart-beta
    title "followanton/sleepwalker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `dc1a57e85ce1` · [字段定义](../../DATASET.md)*
