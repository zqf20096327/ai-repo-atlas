# aiproxer/aiproxer

⭐ 20 · Python · AGPL-3.0 · 推送 2026-10-01 · [GitHub](https://github.com/aiproxer/aiproxer) · [官网](https://github.com/matdev83/llm-interactive-proxy) · 个人维护

**本地 LLM 代理：把各类 AI 客户端接入多种推理后端并统一路由**

LLM Interactive Proxy 是一个通用翻译、路由与控制层：将 OpenAI、Anthropic、Gemini 等协议的客户端指向单一本地或共享端点，即可获得跨协议转换、多后端路由（含 failover 链、加权、并行竞速）、重试与熔断等可靠性机制、上下文压缩与工具输出压缩等 token 节省能力，以及流量捕获与诊断端点。后端目录涵盖 OpenAI、Anthropic、Gemini、OpenRouter、通义千问、Kimi、MiniMax、智谱等。以 Python 源码方式安装运行，通过 config.yaml 与 CLI 配置。面向运行 agent/编码类工作负载的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 跨协议转换：一个端点同时服务 OpenAI/Anthropic/Gemini 风格客户端
- 路由选择器语法支持 failover 链、加权分流、并行竞速与上下文限制
- 上下文压缩与内容感知的工具输出压缩以节省 token
- 重试、熔断、健康监控等生产可靠性机制与 wire 级流量诊断

## 适用场景

- 让编码 agent 等既有客户端不改代码切换后端供应商
- 长会话编码工作负载下压缩历史与工具输出以降低 token 开销
- 多后端加权分流与故障切换
- 检查实际线上流量以调试 agent 行为

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L11: `LLM Interactive Proxy` is a universal translation, routing, and control layer for modern AI clients. Point OpenAI-
> L33: - **One endpoint, many clients** - Keep existing OpenAI-, Anthropic-, and Gemini-style clients while changing routi

## 星数曲线

```mermaid
xychart-beta
    title "aiproxer/aiproxer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `a2105c3d60f2` · [字段定义](../../DATASET.md)*
