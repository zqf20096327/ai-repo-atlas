# MantisAI/sieves

⭐ 126 · Python · MIT · 推送 2026-05-11 · [GitHub](https://github.com/MantisAI/sieves) · [官网](https://sieves.ai) · 组织维护

**面向文档 AI 的框架无关流水线构建库，零训练结构化抽取**

Python 库，为文档 AI 提供与语言模型框架解耦的统一抽象层：把解析（docling/marker）、分块（chonkie）、零样本结构化预测、蒸馏（setfit/model2vec）串成声明式流水线，后端可在 dspy、langchain、outlines、gliner2、transformers 之间切换而无需重写业务逻辑。内置分类、信息抽取、关系抽取、摘要、翻译、NER、PII 匿名化等任务库，支持流水线持久化、缓存、评测与 DSPy 提示优化。README 声明不适用于聊天机器人和一次性 LLM 调用。pip 安装，解析/蒸馏/优化为可选 extras。

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

- 统一接口下多后端切换（dspy/langchain/outlines/gliner2/transformers），无需重写流水线逻辑
- 零训练即时推理：分类、信息抽取、NER、PII 匿名化等任务库
- 端到端文档流水线：PDF/图像/Office 解析 + 分块 + 结构化生成
- 零样本预测蒸馏为专用小模型（setfit/model2vec），可导出 HuggingFace Dataset

## 适用场景

- 从原始 PDF/Office 文档快速原型化结构化数据抽取，无需训练数据
- 在本地小模型与远端 LLM 后端之间切换同一套流水线
- 用零样本结果蒸馏低延迟专用小模型用于生产

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L13: `sieves` provides a **framework-agnostic abstraction for building document AI pipelines**.
> L26: `sieves` unifies the entire workflow:
> L34: Define your task pipeline once, then swap execution engines without rewriting your pipeline logic. Use the task lib

## 星数曲线

```mermaid
xychart-beta
    title "MantisAI/sieves 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 125 --> 127
    line [126, 126]
```

2026-10-18 126 → 2026-10-25 126（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `0bc606078865` · [字段定义](../../DATASET.md)*
