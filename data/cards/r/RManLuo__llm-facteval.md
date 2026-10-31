# RManLuo/llm-facteval

⭐ 19 · Python · 推送 2026-03-17 · [GitHub](https://github.com/RManLuo/llm-facteval) · 个人维护

**论文配套框架：基于知识图谱系统评测 LLM 事实知识**

EMNLP Findings 2023 论文 'Systematic Assessment of Factual Knowledge in Large Language Models' 的源码，提供从知识图谱读取与预处理、抽取问题三元组、生成问答、到评测 LLM 回答的四组件框架（kg/extractor/generator/evaluator）。支持 LAMA（trex、google_re）与 BioLAMA（umls、wiki-bio）等知识图谱，生成器支持 template、llm-mask、llm-question 三种方式；通过扩展基类可接入新 KG 与抽取器，以 python run_certlm.py 命令分步运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四组件框架：kg / extractor / generator / evaluator
- 支持 LAMA（trex、google_re）与 BioLAMA（umls、wiki-bio）知识图谱
- 三种问题生成器：template / llm-mask / llm-question
- 可通过继承 BaseKG、BaseExtractor 等基类扩展新数据源

## 适用场景

- 复现论文中 LLM 事实知识评测实验
- 基于知识图谱生成问答对评测模型
- 接入自定义知识图谱构建评测集

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L7: - `generator`: to generate questions/answers from extracted triplets
> L8: - `evaluator`: to evaluate LLM's response

## 星数曲线

```mermaid
xychart-beta
    title "RManLuo/llm-facteval 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4d98d69db664` · [字段定义](../../DATASET.md)*
