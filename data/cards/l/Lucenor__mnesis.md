# Lucenor/mnesis

⭐ 20 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/Lucenor/mnesis) · [官网](https://mnesis.lucenor.tech/) · 组织维护

**长程 LLM agent 的无损上下文管理 Python 库**

面向长时运行的 LLM agent 的 Python 库，实现 LCM（Lossless Context Management）架构：由确定性引擎而非模型自身负责记忆管理。核心机制包括 SQLite 追加式不可变日志、按 token 阈值触发的三级压缩（结构化摘要→激进压缩→确定性截断）、工具输出后向扫描修剪、大文件内容寻址外部引用（含 AST/结构摘要），以及 LLMMap/AgenticMap 并行算子。通过 litellm 支持 Anthropic/OpenAI/Gemini/OpenRouter 等任意提供商，也支持 BYO-LLM 用自有 SDK 注入对话。示例可用 MNESIS_MOCK_LLM=1 无 API key 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三级自动压缩，最终级为无 LLM 的确定性截断
- SQLite 追加式不可变日志，每轮组装适配 token 预算的 Active Context
- 大文件以 FileRefPart 外部引用并生成结构摘要（AST/JSON schema/Markdown 标题）
- LLMMap/AgenticMap 并行算子，调用方上下文开销 O(1)

## 适用场景

- 长时运行 agent 避免上下文膨胀导致的推理质量下降
- 需要在多轮任务中保留文件路径、约束等关键信息的场景
- 对大量输入并行调用 LLM 或子 agent 而不占主会话上下文
- 接入自有 SDK 工作流，仅由库负责记忆与压缩

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L18: **mnesis** solves this by making the *engine* — not the model — responsible for memory. It is a Python implementati
> L42: The engine handles memory deterministically so the model can focus entirely on the task.
> L74: mnesis works with any LLM provider via litellm. Pass the model string and set the corresponding API key:

## 星数曲线

```mermaid
xychart-beta
    title "Lucenor/mnesis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b988fc6862ff` · [字段定义](../../DATASET.md)*
