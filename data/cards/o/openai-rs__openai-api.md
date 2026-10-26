# openai-rs/openai-api

⭐ 238 · Rust · MIT · 推送 2025-11-05 · [GitHub](https://github.com/openai-rs/openai-api)

**简洁的 Rust 库：同步调用 OpenAI API**

社区维护的 OpenAI API Rust 客户端库，声称无复杂 async 与冗余依赖。支持 Models、Completions、Chat、Images、Embeddings、Audio 六类接口，Files、Fine-tunes、Moderations、Engines 不支持。通过 crates.io 以 Cargo.toml 依赖方式安装，API key 经环境变量传入，可从环境变量或手动方式设置 HTTP 代理。MIT 许可。

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

- 无复杂 async 与冗余依赖的设计
- 支持 Models/Completions/Chat/Images/Embeddings/Audio 六类 API
- 支持环境变量与手动两种代理配置方式

## 适用场景

- 在 Rust 项目中调用 OpenAI 的 Chat 或 Embeddings 接口
- 需要通过代理访问 OpenAI API 的场景

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L8: A community-maintained library provides a simple and convenient way to interact with the OpenAI API.
> L14: |API|Support|

## 星数曲线

```mermaid
xychart-beta
    title "openai-rs/openai-api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 237 --> 239
    line [238, 238]
```

2026-10-18 238 → 2026-10-26 238（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2fb371be31b5` · [字段定义](../../DATASET.md)*
