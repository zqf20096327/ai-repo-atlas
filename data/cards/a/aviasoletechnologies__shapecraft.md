# aviasoletechnologies/shapecraft

⭐ 14 · TypeScript · NOASSERTION · 推送 2026-10-09 · [GitHub](https://github.com/aviasoletechnologies/shapecraft) · 组织维护

**Node.js LLM 结构化输出库：八种 schema 输入、统一 API 多后端**

面向 Node.js/TypeScript 开发者的 LLM 结构化输出生成库：以 generate(model, schema, prompt) 统一接口接受 Zod、JSON Schema、正则、自定义校验器、XML 模板、GBNF 语法、YAML、OpenAPI spec 八种输入。云端 API 走原生 JSON 模式，本地模型（llama.cpp/llama-cpp）提供 token 级约束保证；无语法参数的后端以提示注入加校验重试，保证级别随后端不同。GBNF 校验为有子集限制的解释器（左递归、深右递归规则引用有限制），XML/YAML 为提示驱动属尽力而为。以 npm 包分发，按需安装各后端 SDK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 八种 schema 输入类型（Zod/JSON Schema/正则/XML 模板/GBNF/YAML/OpenAPI 等）
- llama.cpp 后端 token 级语法约束，输出构造性有效
- 内置 GBNF 解释器校验输出并在不匹配时重试
- Ollama 无需额外 SDK 即可作为后端

## 适用场景

- 让本地 .gguf 模型按 JSON Schema 或 GBNF 语法确定性输出
- 用 Zod schema 统一 OpenAI/Groq/Anthropic 等云端模型的结构化生成
- 从现有 OpenAPI spec 的 operationId 直接生成符合接口形状的数据

## 场景标签

 · 领域:LLM 基础设施/结构化生成

## 证据(README 行号)

> L5: Structured output generation for LLMs in Node.js. Token-level constraints for local models, native JSON modes for cl
> L44: Full guide and reference docs — schema inputs, backends & guarantee levels, streaming, `createClient()` & middlewar
> L227: **The guarantee is backend-dependent — this is the one input where that's true.** On

## 星数曲线

```mermaid
xychart-beta
    title "aviasoletechnologies/shapecraft 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `285b2c4cafe5` · [字段定义](../../DATASET.md)*
