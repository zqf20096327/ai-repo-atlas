# CDragon123-code/geo-copilot

⭐ 20 · JavaScript · 推送 2026-09-02 · [GitHub](https://github.com/CDragon123-code/geo-copilot) · 个人维护 · 中文 README

**面向产品 GEO 工作流的 Chrome 扩展：采集 LLM 回答并生成可发布文章**

Chrome/Edge（Manifest V3）扩展，用于以产品为中心的 GEO（生成式引擎优化）循环：在通用 LLM 平台搜索产品相关问题，采集回答、推荐产品与引用来源，分析平台信号与文章结构，再改写为面向匹配平台的可发布文章草稿，并支持发布后复测与复盘。分析由用户手动触发（GEO START），数据默认存于 chrome.storage.local，无后端服务。文本生成通过 OpenAI 兼容 /chat/completions API（内置 DeepSeek/Qwen/Doubao/Kimi/GLM 等预设），API key 仅存本地。自述为 MVP 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 采集 DeepSeek/Qwen/Doubao/Kimi/ChatGPT/Claude 等 LLM 回答与引用来源
- GEO 诊断、平台优先级、文章结构与可发布草稿生成
- 发布后复测对比并规划下一轮优化
- 数据本地存储，无后端，分析手动触发

## 适用场景

- 我想知道产品在各大 LLM 回答中被如何引用和推荐
- 按目标平台的文章结构改写出可发布的推广内容
- 发布内容后复测同一问题，对比 LLM 回答变化

## 场景标签

`网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L12:  A Chrome/Edge extension for product-focused GEO workflows: LLM source analysis, platform matching, content rewriti
> L45: - Generate GEO diagnosis, platform priority, article structure, publish-ready drafts, and post-publish review concl
> L62: The dashboard supports OpenAI-compatible `/chat/completions` APIs. Built-in presets include:

## 星数曲线

```mermaid
xychart-beta
    title "CDragon123-code/geo-copilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `cc02fb182c8a` · [字段定义](../../DATASET.md)*
