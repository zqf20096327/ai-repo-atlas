# agoodway/html2markdown

⭐ 39 · Elixir · MIT · 推送 2026-08-11 · [GitHub](https://github.com/agoodway/html2markdown) · 个人维护

**Elixir 库：把 HTML 转成 Markdown，供内容提取与 RAG 使用**

Elixir 语言的 HTML 转 Markdown 库，面向内容提取场景：自动过滤导航、脚本、广告等非内容元素，支持 HTML5 语义元素、表格、嵌套列表、实体解码，并可通过选项自定义 navigation_classes、non_content_tags 等过滤行为。以 Hex 依赖（~> 0.3.2）安装，文档发布于 hexdocs.pm。README 列出网页抓取、内容迁移、邮件处理三类用例，主题标签含 rag，可作为 RAG 管道中的文档预处理环节。MIT 许可。

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

- 自动移除导航、广告等非内容元素的内容提取
- 表格、嵌套列表、HTML5 语义元素与实体解码支持
- 可通过选项配置过滤与处理行为

## 适用场景

- 抓取网页后提取可读正文并转为 Markdown
- 把存量 HTML 内容迁移为 Markdown 格式
- RAG 管道中清洗 HTML 文档供向量化使用
- 清理 HTML 邮件为纯文本存储

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L8: Convert HTML to clean, readable Markdown. Designed for content extraction, this library handles common HTML patterns
> L12: Add `html2markdown` to your list of dependencies in `mix.exs`:

## 星数曲线

```mermaid
xychart-beta
    title "agoodway/html2markdown 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-28 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c0217e437439` · [字段定义](../../DATASET.md)*
