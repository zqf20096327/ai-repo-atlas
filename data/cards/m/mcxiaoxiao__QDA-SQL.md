# mcxiaoxiao/QDA-SQL

⭐ 15 · Python · MIT · 推送 2026-10-07 · [GitHub](https://github.com/mcxiaoxiao/QDA-SQL) · 个人维护

**给 Text-to-SQL 研究者：LLM 生成多样化多轮对话训练样本**

CICAI2026 论文的官方实现：利用 LLM 从问题示例与数据库出发，按主题关系与问答类型组合生成多轮 Text-to-SQL 对话样本，用于数据增广。流程分三步：解析 CoSQL 数据集为 CSV、多线程生成问答对、合并过滤与优化；附带基于 SParC 方法（EM/IEM/EX/IEX）的评测脚本。以 CoSQL 为示例数据集，需领域知识时需在 CSV 中自行指定，token 用量经 OpenAI API 计费追踪。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三步流水线：数据集解析→问答对多线程生成→合并过滤优化
- 按主题关系与 Q-A 类型组合控制生成多样性
- 提供适配 SParC 方法（EM/IEM/EX/IEX）的评测脚本
- 支持 Spider/CoSQL/SParC/BIRD 等数据集格式

## 适用场景

- 为多轮 Text-to-SQL 模型扩充训练数据
- 按指定问答类型组合生成定制对话样本
- 复现论文生成流程并评测生成质量

## 场景标签

 · 领域:自然语言处理/Text-to-SQL 数据生成

## 证据(README 行号)

> L4: QDA-SQL leverages large language models (LLMs) to generate multi-turn dialogue samples with diverse question types f
> L17: Run `classification_generate_multithread.py` to generate multi-turn dialogues with classification. Parameters:

## 星数曲线

```mermaid
xychart-beta
    title "mcxiaoxiao/QDA-SQL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f2e4955268d4` · [字段定义](../../DATASET.md)*
