# NightOwlDev19/duckduckgo-ai-openai-api

⭐ 60 · Python · Apache-2.0 · 推送 2026-01-27 · [GitHub](https://github.com/NightOwlDev19/duckduckgo-ai-openai-api) · [官网](https://api.chatgpto.ooguy.com/) · 个人维护

**把 DuckDuckGo AI Chat 封装为 OpenAI 兼容 API 的 FastAPI 服务**

基于 FastAPI 的服务，通过开源库 duckduckgo_search 将 DuckDuckGo AI Chat 转换为 OpenAI 兼容的 /chat/completions 接口，支持流式（NDJSON）与非流式响应，可调用 gpt-4o-mini、llama-3.3-70b、claude-3-haiku、o3-mini、mixtral-8x7b 等模型。提供 API Key 的创建/列出/删除端点，密钥存于 PostgreSQL 或 SQLite，也可通过环境变量跳过鉴权免数据库。安装方式为 git clone 源码 + pip 依赖 + uvicorn 运行。README 声明仅供教育用途，不得商用或违反 DuckDuckGo 服务条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容的 /chat/completions 端点，支持流式与非流式
- 5 种模型可用（gpt-4o-mini/llama-3.3-70b/claude-3-haiku/o3-mini/mixtral-8x7b）
- API Key 管理端点，支持 PostgreSQL/SQLite 存储，可配置跳过鉴权

## 适用场景

- 让支持 OpenAI API 格式的客户端接入 DuckDuckGo AI Chat
- 本地部署一个带密钥管理的对话 API 服务用于测试

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L4: The **DuckDuckGo AI OpenAI API** is an innovative and free solution that transforms DuckDuckGo AI Chat capabilities 
> L90: - **🛠️ Endpoint**: `/chat/completions`
> L92: - **📜 Description**: Returns a chat completion based on the provided messages. If `stream` is `True`, a streaming r

## 星数曲线

```mermaid
xychart-beta
    title "NightOwlDev19/duckduckgo-ai-openai-api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-28 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `a3f2315b1095` · [字段定义](../../DATASET.md)*
