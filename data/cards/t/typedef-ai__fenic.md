# typedef-ai/fenic

⭐ 673 · Python · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/typedef-ai/fenic) · [官网](https://fenic.ai) · 组织维护

**带 AI 算子的语义 DataFrame 引擎，供人与 agent 共用**

fenic 是一个 Python 语义 DataFrame 查询引擎：在 PySpark/SQL 风格操作（select/filter/join/group_by）之上内建调用语言模型的语义算子——extract、classify、summarize、embed、语义 join、情感分析、PDF 解析等。流水线为惰性编译执行，提供自动批处理、限流、重试、token/成本核算与响应缓存；表或视图可发布为 MCP 工具供 agent 调用。模型在 Session 上配置一次，支持 OpenAI/Anthropic/Google/Cohere/OpenRouter。限制：GPT-5/GPT-6 等模型输出仍是概率性的；聚类、相似度 join、PDF 解析需安装可选 extras。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语义算子内建于查询模型：extract/classify/summarize/embed/语义 join 等
- 流水线可检查与重跑：explain、行级 lineage 双向追溯、逐查询 token/成本指标、响应缓存
- 表/视图可发布为 MCP 工具，经 fenic-serve 从 catalog 直接提供服务
- 原生支持 Markdown/SRT/WebVTT/JSON/HTML/PDF 等非结构化类型，可读本地文件、S3 与 Hugging Face 数据集

## 适用场景

- 把文档、日志、工单、转录等杂乱数据转成带类型的行与可复用流水线
- 将 LLM 评测 trace 的探索固化为可重跑的回归分析流水线
- 把数据流水线包装成 MCP 工具给 AI agent 调用
- 让 AI 编程助手正确编写 fenic 代码（skill install + check 静态检查）

## 场景标签

 · 领域:数据工程/LLM 基础设施

## 证据(README 行号)

> L12: It's a DataFrame query engine for semantic data processing, with AI operators — `extract`, `classify`, `summarize`,
> L26: fenic is a **semantic DataFrame engine**. You write the PySpark/SQL-style operations you already know — `select`, `

## 星数曲线

```mermaid
xychart-beta
    title "typedef-ai/fenic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 672 --> 674
    line [673, 673]
```

2026-10-18 673 → 2026-10-22 673（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `f0e8f0dad274` · [字段定义](../../DATASET.md)*
