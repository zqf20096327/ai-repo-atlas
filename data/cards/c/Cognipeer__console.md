# Cognipeer/console

⭐ 26 · TypeScript · AGPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/Cognipeer/console) · [官网](https://docs.cognipeer.com/console/) · 组织维护

**面向多租户组织的自托管 AI 网关与一体化控制台**

开源、自托管的 AI 网关平台：提供 OpenAI 兼容的 LLM 路由（接入 OpenAI、Anthropic、AWS Bedrock、Vertex AI、vLLM、Ollama 等）、RAG 与向量存储管理、MCP Hub、沙箱化编码代理运行环境、GPU 池化（MIG 切片）、AI 红队与护栏、成本追踪与多租户隔离（Cedar 策略引擎、LDAP/SSO）。面向需要统一管理模型接入、代理运行与合规审计的企业团队。技术栈为 Next.js 15 + TypeScript，默认 SQLite 存储，支持 Docker 部署。社区版 AGPL-3.0，商业许可另行提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容 API 网关，支持 7 类以上上游模型提供商与回退链路由
- MCP Hub、代理沙箱（快照/fork/恢复）与浏览器自动化管理
- Cedar 策略引擎统一裁决角色/权限/API token 作用域
- GPU 池化推理与 MIG 切片、成本追踪与预算告警

## 适用场景

- 企业内统一接入多家 LLM 提供商并做配额与成本管控
- 为代理提供隔离沙箱运行环境与 MCP 工具管理
- 多租户组织做数据隔离、审计日志与权限合规
- 对自托管推理服务器做监控与红队测试

## 场景标签

`模型网关` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L3: Open-source, self-hosted AI gateway for multi-tenant organizations — OpenAI-compatible LLM routing, RAG, agent orche
> L12: - **LLM Gateway** — OpenAI-compatible chat completions, embeddings, batch, and moderations across OpenAI, Anthropic

## 星数曲线

```mermaid
xychart-beta
    title "Cognipeer/console 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5de44bdf42b7` · [字段定义](../../DATASET.md)*
