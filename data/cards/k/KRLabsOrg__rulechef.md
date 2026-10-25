# KRLabsOrg/rulechef

⭐ 34 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/KRLabsOrg/rulechef) · [官网](https://krlabsorg.github.io/rulechef/) · 组织维护

**从标注示例学习规则模型的Python库，用LLM合成、推理免调用**

Python 库，通过 LLM 合成从标注示例中学习 regex、Python 代码与 spaCy 模式三类规则，支持抽取、NER、分类、转换四种任务类型；学到的规则在本地推理运行，无需 LLM 调用。机制包括缓冲区优先架构、纠错反馈、增量修补、Agentic 协调器、观察模式（自动捕获 OpenAI 兼容客户端调用并自动发现任务）与规则报告工具。兼容任意 OpenAI 兼容 API，提供 CLI 与 FastAPI+React Web 界面。限制：纯语义类任务上 LLM 仍领先，规则定位为高精度层而非完全替代。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 合成 regex/code/spaCy 规则，推理零 LLM 调用
- 观察模式可捕获任意 OpenAI 兼容客户端调用并自动发现任务
- 内置实体级 P/R/F1 评测与逐规则精度 HTML 报告
- 增量修补与纠错驱动再学习，无需全量重合成

## 适用场景

- 用少量示例生成可读可编辑的抽取/分类规则，替代推理期 LLM 调用
- PII/匿名化等格式结构化实体的高精度抽取
- 记录现有 LLM 调用并学规则以削减后续调用量

## 场景标签

 · 领域:NLP/信息抽取

## 证据(README 行号)

> L23: RuleChef learns regex, Python code, and spaCy patterns from labeled examples using LLM-powered synthesis. You provi
> L102: |Type|Output|Use Case|
> L104: |`EXTRACTION`|`{"spans": [...]}`|Find text spans (untyped)|

## 星数曲线

```mermaid
xychart-beta
    title "KRLabsOrg/rulechef 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-25 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c54cb7e672bf` · [字段定义](../../DATASET.md)*
