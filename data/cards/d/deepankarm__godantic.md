# deepankarm/godantic

⭐ 32 · Go · Apache-2.0 · 推送 2026-03-11 · [GitHub](https://github.com/deepankarm/godantic) · 个人维护

**Go 的 JSON 校验与 Schema 生成库：一个结构体驱动校验、序列化与 OpenAPI**

Go 语言库，用 `Field{Name}()` 类型化方法（而非 struct tag）在一个结构体定义上同时驱动 JSON Schema 生成、运行时校验与序列化。面向构建 LLM 结构化输出与 REST API 的开发者：为 OpenAI/Anthropic/Gemini 生成展平 JSON Schema，校验 LLM 返回的类型错误、缺失字段与非法枚举；支持流式部分 JSON 解析（自动修复未闭合结构）、anyOf/oneOf 判别联合类型、生命周期钩子。附带 gingodantic 包为 Gin 提供自动 OpenAPI 3.0.3 生成、请求校验与 Swagger UI/ReDoc。限制：联合类型基于 any 与接口实现，非 Go 原生 union。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个结构体定义同时驱动 JSON Schema 生成、校验与序列化
- 流式部分 JSON 解析器：修复未闭合结构、跟踪待完成字段
- anyOf/oneOf 判别联合类型校验与 Schema 生成
- gingodantic：Gin 自动 OpenAPI 生成、五类参数校验与内置 Swagger UI/ReDoc

## 适用场景

- 用结构体约束引导并校验 LLM 结构化输出
- 长文本生成时实时解析流式部分 JSON 更新 UI
- Gin REST API 自动生成 OpenAPI 文档并默认校验请求

## 场景标签

 · 领域:后端/LLM 应用开发库

## 证据(README 行号)

> L7: **Pydantic for Go - JSON schema generation, LLM response validation, partial JSON streaming.**
> L11: godantic fixes this. One struct definition with typed methods drives schema generation, validation, and serializati
> L35: Godantic solves a common problem: LLMs sometimes return invalid data (wrong types, missing fields, out-of-range val

## 星数曲线

```mermaid
xychart-beta
    title "deepankarm/godantic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `33fe36b26afb` · [字段定义](../../DATASET.md)*
