# MaurerKrisztian/two-step-llm-tool-call

⭐ 19 · TypeScript · 推送 2026-08-21 · [GitHub](https://github.com/MaurerKrisztian/two-step-llm-tool-call) · 个人维护

**两步 LLM 工具调用方案：按需发送工具 schema 降 token 成本**

针对函数数量多的 LLM 应用：第一步只发送工具名与简述，由模型通过 tools_descriptor 指定所需工具，第二步再发送对应详细 schema，从而减少每请求的输入 token。仓库附带基准测试（npm run bench），在本地 Ollama qwen3.5:4b 上对比经典与两步策略的 token 用量，并报告失败原因分类。README 同时记录限制：枚举菜单随工具数增长、161 工具时出现循环失败、无 prompt caching 下收益可能缩水、解锁工具仅存活一个请求。作者声明当前代码仅为演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 两步工具调用：先简述菜单，再按需发送详细 schema
- 基准测试对比两种策略的真实 token 计数（来自 provider usage 字段）
- 失败原因分类（called_unavailable_tool / hallucinated_tool 等 8 类）
- 默认对接本地 Ollama，可经 --base-url 指向任何 OpenAI 兼容端点

## 适用场景

- 工具数量多的 LLM 应用想降低每请求的输入 token 成本
- 测量自己项目的工具 schema 对 token 消耗的影响
- 研究函数调用策略在规模扩大时的行为与失效模式

## 场景标签

 · 领域:LLM 基础设施/工具调用

## 证据(README 行号)

> L5: So, I had an idea to save money and improve performace: What if we only send the details of the functions the AI act
> L177: |`src/two-step-tool-call.ts`|the method — descriptor tool, recursion, tool dispatch|

## 星数曲线

```mermaid
xychart-beta
    title "MaurerKrisztian/two-step-llm-tool-call 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2ada3e54ad51` · [字段定义](../../DATASET.md)*
