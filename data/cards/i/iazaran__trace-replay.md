# iazaran/trace-replay

⭐ 104 · PHP · MIT · 推送 2026-08-04 · [GitHub](https://github.com/iazaran/trace-replay) · [官网](https://iazaran.github.io/trace-replay/) · 个人维护

**Laravel 执行追踪与 HTTP 重放调试包，附带 AI 修复提示生成**

Laravel Composer 包，以步骤级 instrumentation 追踪业务流程：记录每步耗时、内存、DB 查询与错误，在瀑布时间线仪表盘中展示；支持队列任务与 Artisan 命令自动追踪、概率采样、PII 掩码与多租户作用域。提供确定性 HTTP 重放（默认阻断非 GET、剥离敏感头、返回 JSON diff）。AI 部分为失败追踪生成结构化修复提示，可复制到外部 AI 助手，也可配置 OpenAI/Anthropic/Ollama 驱动在仪表盘内直接问答，并暴露 MCP JSON-RPC 端点供 agent 调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 步骤级追踪记录耗时/内存/DB 查询/错误，瀑布时间线仪表盘
- 确定性 HTTP 重放：默认阻断非 GET 方法，敏感头剥离，返回 JSON diff
- AI Fix Prompt 一键生成结构化调试提示，无需 API key
- MCP JSON-RPC 2.0 端点供自主 AI agent 查询追踪与触发重放

## 适用场景

- 排查 Laravel 复杂业务流程中的失败步骤并生成 AI 调试提示
- 在 staging 环境安全重放录制的 HTTP 请求并对比响应差异
- 低采样率下对生产环境请求做追踪与数据保留管理

## 场景标签

 · 领域:Web 开发/调试可观测性

## 证据(README 行号)

> L12: TraceReplay is not a standard error logger. It is a full-fledged **execution tracer** that captures every step of y
> L271: For any failed trace the dashboard shows an **AI Fix Prompt** button that generates a structured markdown prompt i

## 星数曲线

```mermaid
xychart-beta
    title "iazaran/trace-replay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 103 --> 105
    line [104, 104]
```

2026-10-18 104 → 2026-10-28 104（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `29c3babf7e23` · [字段定义](../../DATASET.md)*
