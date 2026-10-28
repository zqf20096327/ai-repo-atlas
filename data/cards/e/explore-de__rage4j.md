# explore-de/rage4j

⭐ 20 · Java · MIT · 推送 2026-09-16 · [GitHub](https://github.com/explore-de/rage4j) · [官网](http://rage4j.dev) · 组织维护

**Java LLM 应用评测库：用 JUnit 断言测 RAG 输出质量**

面向 Java 开发者的 LLM 应用评测工具，提供正确性、相关性、忠实度、语义相似度与工具调用准确率等指标。四个模块：核心评测库、流式测试断言库（rage4j-assert）、评测结果持久化（JSONL/HTML 报告，rage4j-persist）及 JUnit 5 扩展。集成 LangChain4j，通过 OpenAI API key 构建评测器，支持工具调用断言（顺序/禁止/意外调用检查），可为 Jenkins 生成自包含 HTML 评测报告。要求 Java 21 与 Maven，以 Maven 依赖形式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- correctness/relevance/faithfulness/语义相似度/工具调用准确率等评测指标
- 流式断言 API 支持 RAG 管道测试（given/question/answerFrom）
- 工具调用断言：expectedToolCall、顺序校验、禁止与意外调用检查
- @Rage4jHtmlReport 生成自包含 HTML 报告，可配合 Jenkins 发布

## 适用场景

- 在 JUnit 测试中对 LLM 应用输出做质量断言
- CI 流水线中生成并归档 RAG 评测 HTML 报告
- 校验 LangChain4j AI 服务的工具调用行为

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: Test your LLM apps like the rest of your Java code.
> L15: Rage4J provides tools to evaluate and measure the quality of language model outputs using various metrics like corr

## 星数曲线

```mermaid
xychart-beta
    title "explore-de/rage4j 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `72624c646c66` · [字段定义](../../DATASET.md)*
