# heripo-lab/llm-newsletter-kit-core

⭐ 50 · TypeScript · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/heripo-lab/llm-newsletter-kit-core) · 个人维护

**TypeScript 工具包：自动化 LLM 驱动的领域新闻信生成流水线**

面向开发者的 ESM/TypeScript 工具包，编排抓取→分析→内容生成→保存（可选预览邮件）的端到端新闻信流程。各阶段通过可依赖注入的 Provider 接口替换：爬虫、LLM、数据库、邮件均可换成自有实现；核心内置重试、结构化日志、部分抓取失败处理与预览投递，持久化/调度/订户投递由应用自行提供。基于 AI SDK 7 与 Zod 4，需另行安装兼容的模型 provider；源自韩国文化遗产新闻信服务 Research Radar 的通用化抽取。

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

- 抓取→分析→生成→保存四阶段编排，各阶段 Provider 可替换
- 分析阶段用结构化输出产出三个标签、图片语境与 1-10 重要度评分
- 内置重试（LLM 5 次、chain 3 次）、链式选项与预览邮件
- 生成因 token 截断（finishReason: 'length'）时抛错而非保存截断内容

## 适用场景

- 为特定领域（如学术研究、文化遗产）搭建自动新闻信服务
- 需要自选模型、爬虫与持久化的代码式新闻信自动化
- 按重要度评分与发布条件筛选候选文章并生成 HTML 邮件

## 场景标签

`AI 写作` `工作流自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L19: A type‑first, extensible toolkit that automates LLM‑based newsletter creation end‑to‑end. It orchestrates Crawling 
> L44: - **Core (This Repository):** A domain-agnostic, type-safe engine. It orchestrates the full lifecycle (Crawling → A
> L76: - The core uses AI SDK 7 and Zod 4. Install an AI SDK-compatible model provider separately; provider adapters are d

## 星数曲线

```mermaid
xychart-beta
    title "heripo-lab/llm-newsletter-kit-core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-30 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fbd134332e26` · [字段定义](../../DATASET.md)*
