# radlab-dev-group/llm-router

⭐ 15 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/radlab-dev-group/llm-router) · [官网](https://llm-router.cloud/) · 组织维护

**可本地部署的开源 LLM 网关：统一接口、负载均衡与安全审查**

部署在应用与 LLM 提供商之间的开源网关服务（Apache 2.0）：以统一 REST 接口代理 OpenAI 兼容、Ollama、vLLM、LM Studio、Anthropic、Google Vertex AI、AWS Bedrock、Azure OpenAI 等后端，提供多提供商负载均衡、健康检查、模型级回退与故障转移。内置插件管线做 PII 掩码（正则与 ML）、安全护栏及基于 FAISS 的语义路由与 RAG 注入。项目拆分为五个仓库：核心网关、Python SDK、Flask 配置/匿名化 UI、插件与服务。提供 Docker 镜像与 Helm chart 部署。

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

- 统一 REST 接口代理 8 类 LLM 后端，含流式响应
- 多提供商负载均衡（Redis 共享计数器）、模型级 fallback 与故障转移
- 插件管线：PII 掩码、安全护栏（HerBERT-PL-Guard/Bielik-Guard）、语义路由、RAG
- Codex CLI 与 Claude Code 的 agentic 模型路由

## 适用场景

- 在企业内网统一管控对多个 LLM 提供商的访问
- 在多个模型后端间做负载均衡与故障转移
- 对出站请求做 PII 掩码与安全护栏审查
- 按语义意图自动选择路由到的模型

## 场景标签

`模型网关` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L3: **LLM Router** is a service that can be deployed on‑premises or in the cloud. It adds a
> L16: |**llm-router-api** (subdirectory)|REST proxy that routes requests to any supported LLM backend (OpenAI‑compatible,
> L38: |**Multi‑provider model support**|Each model can be backed by multiple providers (VLLM, Ollama, OpenAI, Anthropic, 

## 星数曲线

```mermaid
xychart-beta
    title "radlab-dev-group/llm-router 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `c84bc6cda47b` · [字段定义](../../DATASET.md)*
