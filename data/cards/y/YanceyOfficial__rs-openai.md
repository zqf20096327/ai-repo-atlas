# YanceyOfficial/rs-openai

⭐ 31 · Rust · MIT · 推送 2026-09-02 · [GitHub](https://github.com/YanceyOfficial/rs-openai) · [官网](https://docs.rs/rs_openai/) · 个人维护

**Rust 语言的 OpenAI API 客户端库**

以 crate 形式发布的 OpenAI API Rust 绑定，覆盖 Chat/Completions/Embeddings/Responses/Conversations/Vector Stores/Realtime WebSocket/组织管理等接口，多数支持 SSE 流式输出，内置指数退避自动重试。使用时通过环境变量配置 API key，在 Cargo.toml 中声明依赖后以 Rust 代码调用。另有 Assistants 等接口因 OpenAI 官方弃用而标记为 deprecated（2026-08-26 sunset）。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 Responses/Conversations/Vector Stores/Realtime 等 OpenAI 接口
- 多处接口支持 SSE 流式输出
- 内置指数退避自动重试
- 实现 OpenAI 组织/管理层 API（审计日志、项目、权限等）

## 适用场景

- 在 Rust 应用中调用 OpenAI 的 Chat 与 Responses 接口
- 构建 OpenAI Realtime WebSocket 会话（语音、函数调用）
- 通过 Rust 管理 OpenAI 文件、微调与向量库

## 场景标签

 · 领域:LLM 基础设施/API 客户端

## 证据(README 行号)

> L10: The OpenAI Rust library provides convenient access to the OpenAI API from Rust applications.
> L16: rs_openai = { version = "0.9.0" }

## 星数曲线

```mermaid
xychart-beta
    title "YanceyOfficial/rs-openai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-27 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5ad9ece66f0c` · [字段定义](../../DATASET.md)*
