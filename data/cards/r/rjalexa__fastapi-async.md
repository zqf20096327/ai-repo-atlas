# rjalexa/fastapi-async

⭐ 25 · Python · MIT · 推送 2026-07-27 · [GitHub](https://github.com/rjalexa/fastapi-async) · 个人维护

**面向开发者的 FastAPI/Redis 分布式异步任务处理系统与监控面板**

基于 FastAPI、Redis 与 React 的分布式后台任务处理框架：API、队列、执行三层解耦，用 Redis 列表/有序集合实现 FIFO 主队列、重试队列、延迟队列与死信队列，提供指数退避重试、外部 API 调用的熔断保护、令牌桶分布式限流，以及基于 SSE 的实时监控前端。以两个调用 OpenRouter 大模型的示例任务（文本摘要、报纸 PDF 文章抽取）演示系统能力，并提供 OpenRouter 状态、余额与用量指标的管理端点。通过 Docker Compose 部署全部服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自研 Redis 队列：主队列/重试队列/延迟队列/死信队列与六态任务生命周期
- 外部 API 熔断保护与分布式令牌桶限流
- React 实时监控面板（SSE 推送队列深度、任务状态、worker 健康）
- OpenRouter 服务状态/余额/用量指标端点与缓存

## 适用场景

- Web 应用中把耗时外部 API 调用移到后台执行
- 监控分布式任务队列、worker 健康与死信队列
- 对慢速且有限流的外部 API 调用做重试与熔断管理

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L21: To demonstrate the system's capabilities with realistic resource-intensive scenarios, we simulate two demanding rem
> L19: AsyncTaskFlow is designed to solve the common problem of managing long-running, resource-intensive tasks in a web a

## 星数曲线

```mermaid
xychart-beta
    title "rjalexa/fastapi-async 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-26 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `2e264f5b91de` · [字段定义](../../DATASET.md)*
