# joshclemm/ai-search

⭐ 21 · HTML · MIT · 推送 2026-10-16 · [GitHub](https://github.com/joshclemm/ai-search) · [官网](https://yaddle.ai) · 个人维护

**PHP 实现的开源 AI 搜索引擎，仿 Perplexity 问答**

用 PHP 编写的简易 AI 搜索引擎示例项目：用户提问后先通过搜索引擎 API（Brave、Google via Serper 等）检索实时结果，将 8-10 条结果片段与自定义提示词拼入上下文调用 LLM（示例代码含 OpenAI 与 Groq），生成带引用标注的回答，并支持并行调用 LLM 生成相关追问。前端为 index.html 单页，提供流式回答、引用弹窗与 Markdown 高亮。运行需自行填入搜索与 LLM 的 API key，并安装 PHP 后以 php -S 本地启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 搜索结果注入 LLM 上下文的 RAG 问答流程（search.php）
- 回答内嵌引用，附来源列表与相关追问生成
- 流式输出、引用弹窗与 Markdown/代码高亮的前端 UI
- 示例代码内置 OpenAI 与 Groq 两种 LLM 接入

## 适用场景

- 自建一个带实时检索与引用的 AI 问答页面
- 学习 RAG 检索增强回答的最小实现
- 对比不同搜索 API 与 LLM 提供商的搭配效果

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L2: A Basic open source AI search engine, modeled after Perplexity.ai. If you’re not familiar with an AI-powered questio
> L13: The main challenge with LLMs like ChatGPT is that they have knowledge cutoffs (and they occasionally tend to halluc
> L25: In `search.php`, put your API keys where appropriate (look for "[Fill me in]"). For this example, I'm using OpenAI 

## 星数曲线

```mermaid
xychart-beta
    title "joshclemm/ai-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d7389f633ab6` · [字段定义](../../DATASET.md)*
