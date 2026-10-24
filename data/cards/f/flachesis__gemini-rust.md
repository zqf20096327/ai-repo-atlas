# flachesis/gemini-rust

⭐ 79 · Rust · MIT · 推送 2026-09-05 · [GitHub](https://github.com/flachesis/gemini-rust) · [官网](https://crates.io/crates/gemini-rust) · 个人维护

**Google Gemini API 的 Rust 客户端库**

面向开发者的 Rust 客户端库，封装 Gemini API 的全部端点：Interactions API（服务端多轮状态、可观测执行步骤、后台执行与 webhook 回调）、托管 Agent（Deep Research、Antigravity）、函数调用与 Google Search/Maps 工具、流式输出、图像与语音生成、批量处理、内容缓存、嵌入与 File Search（RAG）、Gemini 2.5/3 的思考模式与代码执行。基于 tokio 异步运行时，类型含 serde 支持，内置 tracing 日志。通过 Cargo.toml 依赖安装，crates.io 发布版本 2.0.0。旧的 generateContent API 仍可用但标记为 deprecated。

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

- Interactions API：服务端会话状态、类型化执行步骤、后台执行与 webhook
- 托管 Agent（Deep Research、Antigravity）与远程沙箱环境
- 函数调用、Google Search/Maps grounding、OpenAPI schema 支持
- 覆盖图像生成、多说话人 TTS、批量处理、嵌入、File Search（RAG）

## 适用场景

- 在 Rust 项目中接入 Gemini 模型做文本/多模态生成
- 构建带工具调用与流式输出的对话应用
- 利用 File Search 做文档语义检索与引用溯源
- 通过批量处理与内容缓存优化 API 成本

## 场景标签

 · 领域:LLM 基础设施/SDK

## 证据(README 行号)

> L3: A comprehensive Rust client library for Google's Gemini API.
> L14: - **🚀 Complete Gemini API Implementation** - Full support for all Gemini API endpoints

## 星数曲线

```mermaid
xychart-beta
    title "flachesis/gemini-rust 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-24 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `56d1f03eda46` · [字段定义](../../DATASET.md)*
