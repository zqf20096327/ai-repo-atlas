# DatanoiseTV/aigateway

⭐ 14 · Go · 推送 2026-03-04 · [GitHub](https://github.com/DatanoiseTV/aigateway) · 个人维护

**自托管 LLM API 网关：按客户端独立配置路由多提供商**

用 Go 编写的自托管 API 网关，部署在应用与 LLM 提供商之间：为每个客户端 API key 独立配置后端提供商、上游密钥、默认模型、模型白名单、限速与 token 配额。支持 Gemini、OpenAI、Anthropic、Mistral、Ollama、LM Studio 等提供商，对外暴露 OpenAI 兼容接口与 Gemini 原生透传。提供 WebSocket 实时管理面板、Prometheus 指标与 Grafana 面板、per-client 系统提示注入与工具调用模式。以预编译二进制或源码构建分发，Docker 支持尚未提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- per-client 后端路由：每个 API key 可指向不同提供商与模型白名单
- OpenAI 兼容接口 + Gemini 原生 API 透传，SSE 流式响应
- 实时管理面板：请求/令牌统计、模型自动发现、请求历史
- Prometheus 指标输出与预置 Grafana 面板

## 适用场景

- 多团队/多应用共享 LLM 出口时按 key 分发配额与限速
- 将本地 Ollama/LM Studio 以 OpenAI 兼容接口暴露给现有工具
- 按客户端注入系统提示与模型白名单做访问管控

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L6: A lightweight, self-hosted API gateway that sits between your applications and LLM providers. Each client gets their

## 星数曲线

```mermaid
xychart-beta
    title "DatanoiseTV/aigateway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e14978578f90` · [字段定义](../../DATASET.md)*
