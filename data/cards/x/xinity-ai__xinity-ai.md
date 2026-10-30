# xinity-ai/xinity-ai

⭐ 61 · TypeScript · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/xinity-ai/xinity-ai) · [官网](https://xinity.ai) · 组织维护

**面向企业的本地化 AI 平台：自有硬件上运行模型并统一管理**

开源的企业级 AI 运营平台，面向受 GDPR、银行保密等法规约束、数据不能出境的组织。提供 OpenAI 兼容 API 网关、带 RBAC/SSO/2FA 的 Web 管理面板、多模型与多 GPU 编排、负载均衡、数据标注导出、审计日志与多节点扩展；底层使用 Ollama 与 vLLM 作为推理引擎，模型不发送到云端。部署途径含 CLI、Docker Compose 与 NixOS Flake，另带 MCP Server 让 Claude/Cursor 等 AI 助手管理基础设施。本地开发需 Bun≥1.3 与 Docker Compose，daemon 需运行在带 GPU 的机器上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容 API 网关，现有 OpenAI SDK 代码改 base URL 即可使用
- 多模型/多 GPU 编排、负载均衡与多组织租户隔离
- 带 RBAC、SSO/2FA 的管理面板与审计日志
- 提供 MCP Server 供 AI 助手以自然语言管理基础设施

## 适用场景

- 受监管企业在自有硬件上部署 AI 且数据不出境
- 统一管理多节点 GPU 推理、API 密钥与租户权限
- 让 Claude/Cursor 等 AI 助手通过 MCP 管理部署

## 场景标签

`模型网关` `推理引擎` · 领域:Agent 开发

## 证据(README 行号)

> L5:  The open-source AI platform for enterprises that cannot send data to the cloud:
> L25: Xinity gives them a complete AI platform: model orchestration, an OpenAI-compatible API, a management dashboard, da
> L59: **Xinity isn't a model runner: it's the full operations layer.** Ollama and vLLM are excellent inference engines (X

## 星数曲线

```mermaid
xychart-beta
    title "xinity-ai/xinity-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 58 --> 62
    line [59, 61, 61]
```

2026-10-18 59 → 2026-10-30 61（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `09dbc1320447` · [字段定义](../../DATASET.md)*
