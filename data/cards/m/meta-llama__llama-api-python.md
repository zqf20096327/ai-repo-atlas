# meta-llama/llama-api-python

⭐ 64 · Python · MIT · 推送 2026-05-12 · [GitHub](https://github.com/meta-llama/llama-api-python) · 组织维护

**Meta Llama API 官方 Python 客户端库**

由 Stainless 生成的 Llama API 官方 Python SDK，封装对 Llama API Client REST API 的访问，覆盖 Python 3.9+ 应用。提供同步与异步客户端（默认 httpx，可选 aiohttp 后端）、全量请求/响应类型定义（TypedDict 与 Pydantic 模型）、SSE 流式响应、文件上传、自动重试（默认 2 次指数退避）、超时配置及未公开端点/参数的自定义请求能力。限制：需持有 Llama API Key，依赖远程托管服务。

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

- 同步/异步双客户端，可选 aiohttp 后端
- 完整类型定义（TypedDict/Pydantic），支持流式响应与文件上传
- 默认自动重试与可配置超时
- 支持未公开端点与自定义 HTTP 客户端（代理/自定义传输）

## 适用场景

- 在 Python 应用中调用 Llama API 的对话补全等接口
- 构建需要流式输出或异步并发的 Llama 应用
- 以类型安全方式集成 Llama API 并处理错误与重试

## 场景标签

 · 领域:LLM 基础设施/API 客户端

## 证据(README 行号)

> L5: The Llama API Client Python library provides convenient access to the Llama API Client REST API from any Python 3.9+
> L9: It is generated with Stainless.

## 星数曲线

```mermaid
xychart-beta
    title "meta-llama/llama-api-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-28 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e49ec6636e91` · [字段定义](../../DATASET.md)*
