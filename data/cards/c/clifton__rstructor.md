# clifton/rstructor

⭐ 33 · Rust · MIT · 推送 2026-10-11 · [GitHub](https://github.com/clifton/rstructor) · [官网](https://crates.io/crates/rstructor) · 个人维护

**Rust 版 Instructor：从 LLM 提取经校验的结构化数据到原生类型**

面向 Rust 开发者的结构化输出库：在结构体和枚举上派生 Instructor 宏，自动生成 JSON Schema、调用模型、解析响应并按配置上限自动重试校验失败。OpenAI、Anthropic、Grok (xAI)、Gemini 四个内置 provider 共用一个 extract() 调用，客户端可替换；也支持 Ollama、LM Studio、Groq、OpenRouter、Moonshot 等兼容端点。支持嵌套/递归类型、动态映射、自定义校验、流式输出、工具调用、请求构建器与 prompt 缓存语义，并提供 schemars 互操作桥接。以 crates.io 上的 Cargo 依赖形式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 派生宏从 Rust 类型生成 JSON Schema 与校验解析器
- 校验失败自动反馈给模型并按上限重试（re-ask）
- 四个内置 provider 统一 extract() API，客户端可替换
- 支持嵌套/递归结构、动态映射、流式输出、工具循环与 schemars 桥接

## 适用场景

- 把自由文本或图像/PDF 提取为类型安全的 Rust 结构体
- 在 axum 服务中注入 LLMClient 做结构化 JSON 请求处理
- 通过 Ollama 等本地端点离线运行结构化提取
- 用 mock 与 fixture 回放在无网络环境下测试提取流程

## 场景标签

 · 领域:LLM 基础设施/结构化输出

## 证据(README 行号)

> L9: Get structured, validated data from supported LLM providers as native Rust structs and enums. Define the shape you w
> L14: - **Multi-provider, one API** — OpenAI, Anthropic, Grok (xAI), and Gemini behind a single `extract()` call with swa
> L17: - **Familiar if you know Pydantic + Instructor** — The same structured-output workflow as Python's Instructor + Pyd

## 星数曲线

```mermaid
xychart-beta
    title "clifton/rstructor 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-29 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7952fd85dd84` · [字段定义](../../DATASET.md)*
