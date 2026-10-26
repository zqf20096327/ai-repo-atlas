# ivangabriele/mistralai-client-rs

⭐ 47 · Rust · Apache-2.0 · 推送 2026-06-30 · [GitHub](https://github.com/ivangabriele/mistralai-client-rs) · 个人维护

**面向 Rust 开发者的 Mistral AI API 客户端库**

以 Rust 库形式封装 Mistral AI API，覆盖同步与异步的 Chat（含流式与 Function Calling）、Embedding、模型列表等接口；API Key 可通过环境变量或 Client 参数传入。通过 Crates.io 分发（cargo add mistralai-client），文档发布于 Docs.rs。README 声明 v0 阶段次要版本可能引入破坏性变更，需参考 CHANGELOG。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持同步/异步 Chat、流式输出与 Function Calling
- 支持 Embedding 与模型列表接口
- 通过 Crates.io 发布并提供 Docs.rs 文档

## 适用场景

- 在 Rust 项目中接入 Mistral AI 的对话与嵌入能力
- 构建基于 Function Calling 的 Rust 应用
- 以流式方式消费 Mistral 模型输出

## 场景标签

 · 领域:LLM 基础设施/API 客户端

## 证据(README 行号)

> L8: Rust client for the Mistral AI API.
> L16: ## Supported APIs

## 星数曲线

```mermaid
xychart-beta
    title "ivangabriele/mistralai-client-rs 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 45 --> 48
    line [46, 47, 47]
```

2026-10-18 46 → 2026-10-26 47（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7ea5ff8a410d` · [字段定义](../../DATASET.md)*
