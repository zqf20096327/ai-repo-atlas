# AISmithLab/HumanStudy-Bench

⭐ 18 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/AISmithLab/HumanStudy-Bench) · [官网](humanstudy-hub.com) · 组织维护

**LLM 参与者模拟基准：端到端重放人类被试实验并评估对齐**

面向社会科学研究者与 agent 设计者的评测基准：由执行引擎（从已发表论文重建完整实验流程）与标准化基准两部分组成，可让 AI agent 以指定设计（如带人口学画像的提示词）跑完 12 项经典研究（认知、策略互动、社会心理学），覆盖 6,000+ 试次、人类样本最多 2,100+ 人。评估指标为现象层面的概率对齐分 PAS 与数据层面的效应一致性分 ECS，输出统计结果与人类真值对比。支持自定义 agent 设计与通过解析研究 PDF 自动添加新研究。pip 安装依赖后以 Python 脚本运行，模型经 API key 接入 OpenAI/Anthropic/Google/OpenRouter。

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

- 执行引擎从已发表研究重建完整实验流程并端到端重放
- 12 项基础研究、6,000+ 试次、最多 2,100+ 人类被试的人类真值基线
- PAS（现象层面概率对齐）与 ECS（效应一致性）两级评估指标
- 解析研究 PDF 自动生成模拟代码以添加新研究

## 适用场景

- 在同一实验上比较不同 agent 设计的人类对齐表现
- 验证 LLM 模拟被试能否复现既有社会科学结论
- 构建自定义人群画像的参与者模拟并量化评估

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L14: HumanStudy-Bench treats participant simulation as an *agent design problem* and provides a **standardized testbed**
> L20: - **Run agents through real studies** reconstructed from published human-subject research

## 星数曲线

```mermaid
xychart-beta
    title "AISmithLab/HumanStudy-Bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `91790cee46e7` · [字段定义](../../DATASET.md)*
