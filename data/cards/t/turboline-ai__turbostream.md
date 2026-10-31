# turboline-ai/turbostream

⭐ 18 · Go · MPL-2.0 · 推送 2026-02-23 · [GitHub](https://github.com/turboline-ai/turbostream) · [官网](https://turboline.ai/) · 组织维护

**实时数据流后端：以 LLM 分析高速数据流的 Go 服务**

Go 编写的高性能后端，提供 REST API 与 WebSocket 流式接口，用于接入高速数据流并通过 LLM 做实时分析。采用 BYOM 模式，支持 7 家以上提供商（Anthropic/OpenAI/Azure/Gemini/Mistral/xAI/Ollama 等）经环境变量切换；内置 JWT 认证与 2FA、Feed 市场、按 Topic 隔离的 LLM 上下文及声称降低 40-60% token 的 TSLN 格式。运行必需 MongoDB、JWT 密钥与加密密钥；提供 Docker 构建与 Railway 部署路径，另有关联的 TUI 客户端仓库，Web 前端为商业授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- REST API + WebSocket 双通道，支持 SSE 流式 LLM 响应
- BYOM 多提供商接入：7 家以上 LLM 提供商环境变量切换
- Feed 市场与按 Topic（如 BTC-USD）隔离的 LLM 上下文管理
- JWT 认证、2FA（TOTP + 备份码）与敏感数据加密

## 适用场景

- 为金融行情等高速数据流接入实时 LLM 分析
- 团队搭建带认证与订阅机制的内部数据流 AI 监控后端
- 本地用 Ollama 起一套私有 LLM 流分析服务

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: **Real-time data streaming backend with AI-powered analysis**
> L120: - `POST /api/llm/query` - Query LLM with feed data
> L140: - **Multi-Provider LLM** - Support for 7+ LLM providers (BYOM)

## 星数曲线

```mermaid
xychart-beta
    title "turboline-ai/turbostream 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `01ee07be9c45` · [字段定义](../../DATASET.md)*
