# kornkutan/groq4j

⭐ 13 · Java · MIT · 推送 2026-11-26 · [GitHub](https://github.com/kornkutan/groq4j) · [官网](https://github.com/kornkutan/groq4j/releases) · 个人维护

**Java 开发者接入 GroqCloud API 的零依赖客户端库**

面向 Java 21+ 开发者的非官方 GroqCloud API 客户端：以单个 jar 提供聊天补全、Responses、嵌入、重排序、语音识别/合成、文件与批量任务端点，基于 java.net.http 实现，无传递依赖。支持流式输出、工具调用、JSON Schema 结构化输出、文档引用、reasoning effort 配置；按 HTTP 状态码抛出细分异常并携带 retry-after；可自定义 HttpClient 与 baseUrl，离线测试套件以内置 fake 服务器运行，无需 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零运行时依赖单 jar，基于 java.net.http
- 覆盖 chat/responses/embeddings/reranking/audio/files/batches 端点
- 流式输出、工具调用、JSON Schema 结构化输出与 reasoning 配置
- 按状态码细分的异常体系，携带 retry-after 与 request id

## 适用场景

- 在 Java 项目中调用 GroqCloud 的聊天与嵌入模型
- 以流式方式消费聊天补全响应
- 用批量任务接口离线处理大规模请求
- 在 CI 中运行无需 API key 的离线测试套件

## 场景标签

 · 领域:LLM 基础设施/API 客户端

## 证据(README 行号)

> L8: Java library for the Groq API (GroqCloud): chat completions, responses, embeddings, reranking, speech, transcription
> L10: ## Install


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `9faab22e8717` · [字段定义](../../DATASET.md)*
