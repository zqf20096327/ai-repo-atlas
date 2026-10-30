# sattyamjjain/agent-airlock

⭐ 17 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/sattyamjjain/agent-airlock) · [官网](https://sattyamjjain.github.io/agent-airlock/) · 个人维护

**AI agent 工具调用的进程内契约校验层，默认拒绝**

面向 agent 开发者的 Python 装饰器库：在工具函数执行前按固定顺序运行校验、授权、隔离、净化等关卡，用 Pydantic V2 严格模式校验参数类型、剥离签名外参数，拦截时返回带 fix_hints 的结构化错误供模型重试。另含 RBAC、速率限制、沙箱执行（E2B/Docker/Modal/本地后端）、PII 脱敏与针对 MCP 的安全防护。进程内运行，非代理或网关；为 12 个框架提供适配模块，AutoGen/LlamaIndex 仅示例兼容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Pydantic V2 严格模式参数校验与 ghost-argument 剥离，返回带 fix_hints 的可重试结构化错误
- 12 个框架适配模块（LangChain/LangGraph/OpenAI/Anthropic/CrewAI/PydanticAI 等）
- MCP 防护：stdio 注入、OAuth、DNS rebinding、SSRF、eval-RCE 等 per-CVE 守卫
- 按 OWASP Agentic Top-10（2026）与 MCP Top-10 逐项映射安全覆盖

## 适用场景

- 为 agent 的工具调用加参数契约校验，拦截类型错误与注入参数
- 给 MCP server 的工具层加默认拒绝的访问控制与审计
- 限制 agent 的文件系统与网络访问，做最小权限隔离

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: **Strict argument validation, ghost-argument stripping, and self-healing retries — one decorator, any agent or MCP s
> L61: The decorator runs a fixed sequence of gates before your function and sanitises after it.
> L130: Both paths use the same `@Airlock()` decorator. **Adapter-shipped** means a dedicated module

## 星数曲线

```mermaid
xychart-beta
    title "sattyamjjain/agent-airlock 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `72650267c89d` · [字段定义](../../DATASET.md)*
