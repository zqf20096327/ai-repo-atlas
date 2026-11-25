# Raytorin/triton-openai-gateway

⭐ 10 · Python · Apache-2.0 · 推送 2026-11-17 · [GitHub](https://github.com/Raytorin/triton-openai-gateway) · [官网](https://triton-gateway.space/) · 个人维护

**为 Triton/vLLM 提供兼容 OpenAI API 的网关**

运行在 NVIDIA Triton Inference Server 旁的 FastAPI 网关，在 8080 端口暴露 OpenAI 兼容 API。它按模型应用聊天模板、翻译工具调用、处理图像/视频/音频/PDF 多模态输入，并提供准入队列、背压、Prometheus 指标与 OTLP 追踪，同时不替代 Triton 的模型生命周期与 vLLM 调度器。面向已有 Triton 推理运行时、但需要统一 API 供 LiteLLM、LibreChat、OpenAI SDK 等客户端接入的团队。独立社区项目，非 NVIDIA 官方产品，不含模型权重，无内置用户认证。

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

- OpenAI 兼容端点：/v1/chat/completions、/v1/responses、/v1/embeddings、/rerank
- 图像、视频、音频、PDF 多模态输入路由与有界预处理
- SSE 流式输出、工具调用翻译（含 Qwen3-Coder XML）、JSON Schema 结构化输出
- 准入队列、取消、结构化日志、Prometheus 指标与 OTLP 追踪

## 适用场景

- 让 LiteLLM/LibreChat 等客户端通过统一 API 访问 Triton 上的模型
- 生产环境中为长对话做滚动摘要与上下文溢出策略管理
- 通过混合嵌入端点同时获取稠密与词法稀疏向量
- 在 Kubernetes 集群用 Helm 部署 GPU 推理网关

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L16: Triton OpenAI Gateway runs next to NVIDIA Triton Inference Server and exposes a
> L77: continuous batching remain inside Triton/vLLM; the gateway only owns the client

## 星数曲线

```mermaid
xychart-beta
    title "Raytorin/triton-openai-gateway 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-25"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-23 10 → 2026-11-25 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `e0015e7cbc1f` · [字段定义](../../DATASET.md)*
