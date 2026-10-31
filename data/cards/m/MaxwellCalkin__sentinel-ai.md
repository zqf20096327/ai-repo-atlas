# MaxwellCalkin/sentinel-ai

⭐ 25 · Python · Apache-2.0 · 推送 2026-03-09 · [GitHub](https://github.com/MaxwellCalkin/sentinel-ai) · [官网](https://maxwellcalkin.github.io/sentinel-ai/) · 个人维护

**给 LLM 应用的实时安全防护层：11 类扫描器拦截注入与泄露**

面向 LLM 应用开发者的安全中间件：以正则规则扫描提示注入、PII、有害内容、代码漏洞、混淆攻击等，自称平均约 0.05ms、无需 GPU 与 API 调用，核心依赖仅 regex。提供 Python/TypeScript SDK、CLI、FastAPI 中间件、LLM API 反向代理防火墙、MCP 服务器与 Claude Code 插件/hooks，另含项目级安全审计、依赖供应链与密钥扫描。定位为模型化安全工具之前的确定性过滤层。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个内置扫描器覆盖 OWASP LLM Top 10，无需 GPU/API 调用
- Python + TypeScript 双 SDK，零重量级依赖（核心仅需 regex）
- LLM API 反向代理防火墙扫描请求/响应并自动脱敏 PII
- MCP 服务器（14 个工具）与 Claude Code hooks/插件集成
- 项目级扫描：CLAUDE.md 注入、供应链、硬编码密钥、MCP 工具 schema 校验

## 适用场景

- 在 LLM 应用入口拦截提示注入与 PII 泄露
- 给 Claude Code / MCP 客户端挂载自动安全扫描
- CI/CD 中对项目做依赖供应链与密钥审计
- 以反向代理形式为任意 LLM API 加防护

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L11: Sentinel AI is a lightweight, zero-dependency safety layer that protects your LLM applications from prompt injectio
> L25: - **Drop-in integrations**: Works with Claude, OpenAI, LangChain, LlamaIndex, and any LLM.
> L292: Transparent reverse proxy that sits between your app and any LLM API, scanning all requests and responses:

## 星数曲线

```mermaid
xychart-beta
    title "MaxwellCalkin/sentinel-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-31 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3651b660f681` · [字段定义](../../DATASET.md)*
