# isartor-ai/Isartor

⭐ 21 · Rust · Apache-2.0 · 推送 2026-06-03 · [GitHub](https://github.com/isartor-ai/Isartor) · [官网](https://github.com/isartor-ai/Isartor) · 组织维护

**开源 Prompt 防火墙：本地拦截冗余 LLM 流量再转发云端**

纯 Rust 单二进制的本地 LLM 网关，部署在 AI 编码工具与上游 LLM 提供商之间。请求依次经过分层偏转栈：MiniLM 分类路由、精确缓存、语义缓存（candle 嵌入）、本地 SLM（Qwen-1.5B GGUF）与上下文压缩，未命中的才转发云端。支持多提供商回退链、模型别名、密钥池轮换与配额，提供 Copilot/Claude Code/Cursor/Codex/Gemini 等工具的一键连接命令。支持 Docker、脚本安装与源码编译，可空气隔离运行。README 给出的偏转率基准从 38% 到 95% 不等，取决于工作负载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分层偏转栈：精确缓存/语义缓存/本地 SLM/上下文压缩
- 纯 Rust 单二进制，可空气隔离运行，无隐藏遥测
- 11 种编码工具的一键连接（MCP/Base URL 覆盖等机制）
- 多提供商回退链、密钥池轮换与配额策略

## 适用场景

- 降低编码 Agent 重复请求的云端调用成本
- 在本地先行应答简单请求，减少数据出网
- 统一管理多个 LLM 提供商的路由与密钥

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L158: Isartor sits **between your AI tools and upstream LLM providers**. Every request goes through a local deflection s
> L189: Request ──► L0.5 MiniLM Router ──► L1a Exact Cache ──► L1b Semantic Cache ──► L2 SLM Router ──► L2.5 Context Optim
> L202: |**L3** Cloud Logic|Routes complex prompts to OpenAI / Anthropic / Azure|Ordered multi-provider fallback plus per-

## 星数曲线

```mermaid
xychart-beta
    title "isartor-ai/Isartor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `034dec037aba` · [字段定义](../../DATASET.md)*
