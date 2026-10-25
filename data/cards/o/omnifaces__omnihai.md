# omnifaces/omnihai

⭐ 37 · Java · NOASSERTION · 推送 2026-10-18 · [GitHub](https://github.com/omnifaces/omnihai) · [官网](https://omnihai.org) · 组织维护

**统一 Java API 接入多家 AI 提供商的工具库**

面向 Java/Jakarta EE 与 MicroProfile 开发者的统一 AI 客户端库：通过单一一致 API 直接调用 OpenAI、Anthropic、Google AI、xAI、Mistral、Azure OpenAI、OpenRouter、Ollama 等提供商的 REST 端点。提供 CDI @AI 注入、流式/异步聊天、多轮对话记忆（默认 20 条滑窗）、文件附件、token 用量跟踪与成本计算、预算上限、结构化输出（JSON Schema 生成与解析）、Web 搜索、文本分析与分类。硬性要求仅 Java 17 与 JSON-P 实现，也可运行于纯 Java SE。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 API 直连 11 类提供商（含 Ollama 本地、Custom 自定义端点）
- CDI @AI 注入与 MicroProfile 集成，@AITool 方法自动发现
- 结构化输出：从 Java record/bean 生成 JSON Schema 并解析回类型对象
- token 用量跟踪、三档计价与预算硬停（AIBudgetExceededException）

## 适用场景

- 在 Jakarta EE / MicroProfile 应用中接入多家 AI 提供商而不换代码
- 对多模型回答做交叉验证或聚合以降低偏差
- 为带预算上限的聊天功能做成本监控与止损
- 从 AI 回答直接得到类型化的 Java 对象（如情感分析结果）

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L10: A unified Java AI utility library, with first-class Jakarta EE and MicroProfile integration.
> L14: OmniHai provides a single, consistent API to interact with multiple AI providers. It achieves that by interacting w

## 星数曲线

```mermaid
xychart-beta
    title "omnifaces/omnihai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7de374948835` · [字段定义](../../DATASET.md)*
