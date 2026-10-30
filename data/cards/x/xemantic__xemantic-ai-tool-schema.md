# xemantic/xemantic-ai-tool-schema

⭐ 52 · Kotlin · Apache-2.0 · 推送 2026-01-29 · [GitHub](https://github.com/xemantic/xemantic-ai-tool-schema) · 组织维护

**Kotlin 多平台库：为 @Serializable 类生成 LLM 工具调用 JSON Schema**

Kotlin 多平台库，从标记 @Serializable 的 Kotlin 类（基于 kotlinx.serialization）生成 JSON Schema，并支持附加约束与元数据（Title 等），供 OpenAI API、Anthropic API 等大模型 tool use（function calling）使用；LLM 返回的 JSON 载荷可直接反序列化为原 Kotlin 类，免去手工定义 schema。另支持 JVM 下 BigDecimal 以字符串序列化并附加 description/pattern。开发方式为 git clone 后 ./gradlew build，通过 Maven Central 分发。README 声明其非通用 JSON Schema 建模工具，不应用于反序列化既有 schema。

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

- 从任意 @Serializable Kotlin 类自动生成 JSON Schema（jsonSchemaOf()）
- LLM 返回的 JSON 载荷可直接反序列化回原 Kotlin 类
- 支持 JVM BigDecimal 字符串序列化与 description/pattern 注入
- Kotlin 多平台（multiplatform/JVM）支持

## 适用场景

- 为 Kotlin AI agent 项目自动生成工具调用 schema，省去手写 JSON
- anthropic-sdk-kotlin 等 SDK 项目中承接 tool use 输入的反序列化
- 处理含地址、金额等结构化数据的 agent 工具参数定义

## 场景标签

 · 领域:LLM/Agent 开发工具

## 证据(README 行号)

> L30: These projects are heavily dependent on tool use (function calling) functionality provided by many Large Language M
> L72: And this is the input accepted by Large Language Model APIs like OpenAI API and Anthropic API.

## 星数曲线

```mermaid
xychart-beta
    title "xemantic/xemantic-ai-tool-schema 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-30 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4be147854572` · [字段定义](../../DATASET.md)*
