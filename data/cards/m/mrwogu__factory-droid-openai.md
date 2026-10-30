# mrwogu/factory-droid-openai

⭐ 16 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/mrwogu/factory-droid-openai) · 个人维护

**非官方 OpenAI 兼容桥：让任意 OpenAI 客户端调用 Factory Droid**

本地运行的 API 桥接服务，基于 FastAPI，把 OpenAI Chat Completions 与 Responses API 请求翻译为 Factory Droid 会话，使 VS Code、Cursor、Continue、Aider、Zed 等支持自定义 base_url 的工具接入 Factory 账号可用的模型。核心机制：完整序列化 OpenAI 转写为 Droid 提示、 warmed Droid 会话池降低延迟、严格文本协议解析多种模型的 tool_call 方言并校验。限制：不支持 embeddings/images/audio 等 API 族，sampling 参数与 logprobs 被忽略；桥本身不运行工具、不读取凭据。以 Docker 镜像、uv/pipx/pip 或源码方式安装，声明与 Factory 无隶属关系。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容的 /v1/chat/completions、/v1/responses、/v1/models 端点
- 多方言 tool_call 解析（Hermes/Qwen3/Kimi/DeepSeek/GLM/gpt-oss 等）并统一校验
- Droid 会话预热池、队列准入控制与 Prometheus 风格指标
- 支持流式 SSE、函数调用、结构化输出与带签名的推理块

## 适用场景

- 让 Cursor/VS Code/Continue 等编辑器用 Factory Droid 模型做补全和对话
- 已有 OpenAI SDK 代码不改协议直接切换到 Factory 后端
- 本地部署统一入口，配合凭据隔离使用 Factory API

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L14: This bridge runs locally on your machine. It translates between OpenAI's
> L165: - OpenAI-compatible `POST /v1/chat/completions`

## 星数曲线

```mermaid
xychart-beta
    title "mrwogu/factory-droid-openai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [16, 15, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `bde38cfe8a6e` · [字段定义](../../DATASET.md)*
