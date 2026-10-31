# sharpapi/sharpapi-laravel-client

⭐ 43 · PHP · MIT · 推送 2026-01-10 · [GitHub](https://github.com/sharpapi/sharpapi-laravel-client) · [官网](https://sharpapi.com) · 组织维护

**已弃用的 SharpAPI AI 自动化 API 的 Laravel 客户端 SDK**

SharpAPI 官方 Laravel 客户端包，接入 SharpAPI 的 AI API，覆盖电商（商品介绍生成、评论情感分析、商品分类）、内容营销（翻译、校对、摘要、垃圾检测、关键词/SEO 标签）、HR（简历解析、职位描述生成、相关技能/职位）与旅游酒店分类等场景，支持 80 种语言。使用方式为分发异步任务后轮询取回 JSON 结果。需要 PHP >= 8.1、Laravel >= 9.0，通过 composer 安装并在 .env 配置 API key。README 顶部声明该包已弃用，由一批更细分的专用 Laravel 包替代。

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

- 异步任务模式：分发 AI 处理任务后按可配置间隔轮询获取结果
- 覆盖电商/内容营销/HR/旅游酒店多领域 AI 端点，支持 80 种语言
- 简历解析支持 PDF/DOC/DOCX/TXT/RTF 多格式输入
- 已声明弃用，列出 20+ 个替代专用包

## 适用场景

- 为 Laravel 电商站点做商品分类与评论情感分析
- 自动化生成职位描述并解析简历数据
- 批量处理内容翻译、摘要与 SEO 标签生成

## 场景标签

`文档解析` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L89: composer require sharpapi/sharpapi-laravel-client
> L92: 2. Register at SharpAPI.com and get the API key.
> L156: 1. Dispatch one of the available AI processing methods (this will return job processing status URL)

## 星数曲线

```mermaid
xychart-beta
    title "sharpapi/sharpapi-laravel-client 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-31 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e8fe691b620d` · [字段定义](../../DATASET.md)*
