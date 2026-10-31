# teabranch/open-bedrock-server

⭐ 13 · Python · MIT · 推送 2026-04-08 · [GitHub](https://github.com/teabranch/open-bedrock-server) · [官网](https://open-bedrock-server.teabranch.dev/) · 个人维护

**统一 OpenAI 与 AWS Bedrock 的聊天补全 API 服务器**

Python 实现的 provider 无关 API 服务器：通过单一 /v1/chat/completions 端点接入 OpenAI 与 AWS Bedrock，自动检测请求格式（OpenAI / Bedrock Claude / Bedrock Titan），按模型 ID 模式路由到对应 provider，并在格式间双向转换，支持流式输出。附带文件上传与查询系统（S3 存储，支持文本/CSV/JSON/HTML/XML/Markdown）、CLI 工具、认证与多种 AWS 凭证方式（静态密钥/Profile/角色扮演/OIDC/默认链）。需 Python 3.12+，文件功能需 S3 配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 /v1/chat/completions 端点统一 OpenAI 与 Bedrock
- OpenAI ↔ Bedrock Claude ↔ Titan 三种格式自动检测与双向转换
- 按模型 ID 模式（gpt-*/anthropic.*/amazon.* 等）自动路由
- 基于 S3 的文件上传与对话内文件查询系统，支持 6 种文件类型

## 适用场景

- 用 OpenAI 客户端代码直接调用 Bedrock 上的 Claude/Titan 模型
- 在不同 LLM provider 之间切换而无需改写客户端
- 在聊天请求中携带上传文件作为上下文

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: A unified, provider-agnostic chat completions API server that seamlessly integrates OpenAI and AWS Bedrock through a
> L11: - **🔄 Unified Endpoint**: Single `/v1/chat/completions` endpoint handles all providers and formats
> L14: - **⚡ Model-Based Routing**: Automatic provider selection based on model ID patterns

## 星数曲线

```mermaid
xychart-beta
    title "teabranch/open-bedrock-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `cc52a824ffa6` · [字段定义](../../DATASET.md)*
