# aurorallm/aurora

⭐ 41 · Go · Apache-2.0 · 推送 2026-08-01 · [GitHub](https://github.com/aurorallm/aurora) · [官网](http://aurorallm.online) · 组织维护

**自托管企业 AI 网关：单一 API 路由多家 LLM 提供商流量**

用 Go 编写的 LLM API 网关，部署在应用与 LLM 提供商之间：应用以标准 OpenAI/Anthropic SDK 指向网关地址，网关将请求路由到配置的 14 类提供商（OpenAI、Anthropic、Gemini、Groq、Ollama、vLLM 等）。提供密钥自动发现、提供商池负载均衡与故障转移、精确/语义缓存、PII 脱敏与提示注入拦截等护栏、审计日志、用量计费与 Prometheus 指标，内嵌 React 管理面板。安装方式为 npm 全局包、Docker 镜像或 Helm 图表，面向需要自托管统一 LLM 入口的开发与企业团队。

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

- 14 类提供商路由，OpenAI 与 Anthropic 双兼容 API 面
- 提供商池负载均衡、熔断器与自动故障转移
- 精确/语义/提示三级缓存与 PII 脱敏、提示注入拦截等护栏
- 内嵌 React 管理面板、审计日志、用量计费与 Prometheus 指标

## 适用场景

- 多个 LLM 提供商统一为一个 API 入口，应用无需改 SDK
- 企业内部对 LLM 流量做密钥管理、限流与审计合规
- 按密钥/模型做用量与成本预算控制
- Kubernetes 上以 Helm 部署生产级 LLM 网关

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L23: Aurora sits between your app and LLM providers. Your app sends requests using the standard OpenAI or Anthropic SDK 
> L39: - **14 provider types** — OpenAI, Anthropic, Gemini, Groq, DeepSeek, OpenRouter, xAI, Z.ai, MiniMax, Azure OpenAI, 

## 星数曲线

```mermaid
xychart-beta
    title "aurorallm/aurora 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 39 --> 42
    line [41, 40, 41]
```

2026-10-18 41 → 2026-10-27 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2679640e7ded` · [字段定义](../../DATASET.md)*
