# openlayer-ai/openlayer-python

⭐ 18 · Python · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/openlayer-ai/openlayer-python) · [官网](https://www.openlayer.com) · 组织维护

**面向开发者的 Openlayer 平台官方 Python API 客户端库**

Openlayer（持续模型改进平台）的官方 Python 库，封装其 REST API，提供同步与异步客户端（默认 httpx，可换 aiohttp 后端），包含全量请求参数与响应的类型定义（TypedDict 与 Pydantic 模型）。由 Stainless 生成，自动重试（默认 2 次）、超时配置、流式响应、未公开端点访问、自定义 httpx 客户端与代理支持。需 Python 3.9+，通过 pip 安装，使用 API key 认证。README 仅覆盖库用法，平台功能细节在 openlayer.com 文档。

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

- 同步 AsyncOpenlayer 双客户端，httpx/aiohttp 可选后端
- 全量请求/响应类型定义（TypedDict + Pydantic）
- 自动重试、超时、流式响应与原始响应访问
- 支持未公开端点、额外参数与自定义 HTTP 客户端（代理/自定义传输）

## 适用场景

- 在 Python 应用中调用 Openlayer 平台 API 管理 ML 流程
- 需要异步高并发调用时切换 aiohttp 后端
- 访问文档未列出的端点或附加请求参数

## 场景标签

 · 领域:ML 基础设施/MLOps

## 证据(README 行号)

> L5: The Openlayer Python library provides convenient access to the Openlayer REST API from any Python 3.9+
> L9: It is generated with Stainless.

## 星数曲线

```mermaid
xychart-beta
    title "openlayer-ai/openlayer-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `6364313a83c3` · [字段定义](../../DATASET.md)*
