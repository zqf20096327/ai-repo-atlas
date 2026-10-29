# frieren-123/shopping-agent-ai

⭐ 25 · Python · 推送 2025-12-03 · [GitHub](https://github.com/frieren-123/shopping-agent-ai) · [官网](https://github.com/frieren-123/shopping-agent-ai/blob/main/README.md) · 个人维护 · 中文 README

**跨电商比价购物助手：LLM 分析商品并生成购买报告**

基于 LLM 的购物助手应用，聚合京东（Crawl4AI/OCR）、淘宝（Playwright）、唯品会三平台商品搜索，用 LLM（OpenAI 兼容接口/DeepSeek）提取参数、点评商品，基于价格、销量、店铺信誉计算性价比，生成含优缺点与适用人群建议的 HTML 购买报告。通过 .env 配置 LLM API Key，以 Streamlit Web 界面或 CLI 运行；内置独立浏览器环境、随机延迟等反爬对策，需注意电商平台反爬更新可能导致爬虫失效。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 京东/淘宝/唯品会三平台聚合搜索（Crawl4AI/Playwright/OCR）
- LLM 提取参数与商品点评，OpenAI 兼容接口/DeepSeek 可选
- Smart Scorer 基于价格、销量、店铺信誉计算性价比
- 生成含优缺点与适用人群建议的 HTML 购买报告

## 适用场景

- 跨平台搜索同一商品并对比价格
- 让 AI 帮我读详情页参数和评论再决定买不买
- 拿到一份带优缺点分析的购买决策报告

## 场景标签

`浏览器自动化` `网页抓取` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L11: > 一个基于大语言模型 (LLM) 的智能购物助手，能够跨平台（京东、淘宝、唯品会）搜索商品，利用 AI 帮你阅读复杂的参数和评论，生成客观的购买建议报告。
> L84:  - 利用 LLM (OpenAI/DeepSeek) 对商品进行深度点评。

## 星数曲线

```mermaid
xychart-beta
    title "frieren-123/shopping-agent-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `9717f49d7689` · [字段定义](../../DATASET.md)*
