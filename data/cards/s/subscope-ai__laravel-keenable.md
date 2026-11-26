# subscope-ai/laravel-keenable

⭐ 4 · PHP · MIT · 推送 2026-10-20 · [GitHub](https://github.com/subscope-ai/laravel-keenable) · [官网](https://docs.keenable.ai) · 组织维护

**为 Laravel AI agent 提供网页搜索与抓取工具的客户端包**

封装 Keenable 搜索与抓取 API（POST /v1/search、GET /v1/fetch）的 Laravel 客户端：search() 支持 pro/realtime 两种模式及日期、片段过滤；fetch() 返回结构化页面内容，可选用 LLM 按自定义 prompt 抽取。包内附带实现 Laravel\Ai\Contracts\Tool 的 KeenableSearchTool 与 KeenableFetchTool，供 agent 两行配置接入；统一类型化异常（含限流元数据）与参数预校验，基于 Laravel HTTP client 便于 Http::fake() 测试。计费支持 API key、公共端点与 x402 按请求付费。

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

- search() 提供 pro（质量）与 realtime（时效）两种模式及日期/片段过滤
- fetch() 返回结构化页面内容，支持 LLM 按自定义 prompt 抽取
- 内置实现 Laravel\Ai\Contracts\Tool 的搜索与抓取两个 agent 工具
- 类型化异常含状态码、响应体与限流元数据，参数在 HTTP 调用前预校验

## 适用场景

- 给 Laravel AI agent 接入网页搜索能力
- 抓取未被索引页面的干净正文供 agent 阅读
- 在 Laravel 项目中统一处理搜索 API 的错误与限流

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L8: Laravel client for the Keenable search and fetch API (`POST /v1/search`, `GET /v1/fetch`), with tools for Laravel AI
> L16: - `KeenableSearchTool` and `KeenableFetchTool` — ready-made `Laravel\Ai\Contracts\Tool` implementations, so an agen

## 星数曲线

```mermaid
xychart-beta
    title "subscope-ai/laravel-keenable 星数(近 3 点)"
    x-axis ["2026-10-30", "2026-11-08", "2026-11-26"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-30 3 → 2026-11-26 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `f2ceab9ef400` · [字段定义](../../DATASET.md)*
