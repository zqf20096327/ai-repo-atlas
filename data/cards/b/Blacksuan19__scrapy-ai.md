# Blacksuan19/scrapy-ai

⭐ 43 · Python · MIT · 推送 2026-01-17 · [GitHub](https://github.com/Blacksuan19/scrapy-ai) · 个人维护

**给 Scrapy 开发者的 LLM 中间件：按 pydantic 模式抽取网页数据**

Scrapy-LLM 是嵌入 Scrapy 的中间件：用语言模型从网页文本中抽取数据，抽取结果按用户定义的 pydantic 模式进行校验，可配置嵌套展开、模型、温度与系统提示词。底层组合 Instructor（模式定义与校验）与 LiteLLM（接入任何兼容 OpenAI API 规范的服务），API key 通过 OPENAI_API_KEY 环境变量设置，支持无 key API。以 pip 包提供，需已有 Scrapy 项目，附示例工程抽取大学网站容量数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用 LLM 从网页文本抽取数据并按 pydantic 模式校验
- 支持任何兼容 OpenAI API 规范的模型服务（经 LiteLLM）
- 支持多响应模型按页面切换、嵌套字段展开、自定义系统提示词

## 适用场景

- 在 Scrapy 爬虫中按预定义 schema 抽取结构化数据
- 用不同网页分别应用不同抽取模式
- 切换不同 OpenAI 兼容模型服务进行数据抽取

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: LLM integration for Scrapy as a middleware. Extract any data from the web using your own predefined schema with your
> L257: Under the hood, `scrapy-llm` utilizes two libraries to facilitate data extraction from web page text. The first li
> L259: The second library is LiteLLM, which enables seamless integration between instructor and any API compatible with t

## 星数曲线

```mermaid
xychart-beta
    title "Blacksuan19/scrapy-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-25 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9f4dd60695c2` · [字段定义](../../DATASET.md)*
