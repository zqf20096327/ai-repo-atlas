# exmergo/research-llm-car-wash-test

⭐ 10 · Python · MIT · 推送 2026-06-01 · [GitHub](https://github.com/exmergo/research-llm-car-wash-test) · [官网](https://viz.exmergo.com/share/0de28433-4857-4e99-8e1b-3e943acbbc52) · 组织维护

**面向研究者的 LLM 语义陷阱基准：400 次调用揭示四模型分歧**

Exmergo 发布的开放研究项目：向四个前沿 LLM 各提出同一道歧义提示（洗车店距家 100 米，走路还是开车）各 100 次，记录其二元决策与推理 token 消耗。分类只看回答的首个 token，结果确定性可复现。原始、清洗后与聚合数据均提交入仓库，可零 API 花费重跑分析管线；重新采集需 OpenRouter API key。项目用 uv 管理依赖，采集/清洗/转换三阶段模块化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 400 次调用（4 模型 × 100 次）的决策与推理 token 数据集
- 数据全部提交入仓库，Path 1 无 API key 即可复现全部分析
- collect→clean→transform 三阶段管线，各阶段可独立重跑
- 严格确定性分类：仅对回答首 token 判定 Pass/Fail

## 适用场景

- 我想复现或验证这个 LLM 歧义测试的结果数据
- 设计 LLM 推理行为评测时参考其方法与局限性讨论
- 零成本重新生成清洗与聚合数据集

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: How do LLMs deal with contextual ambiguity in low-stakes situations?
> L15: **We asked four frontier LLMs this exact question 100 times each (N = 400)** and
> L159: Raw, cleaned, and aggregate datasets are all **committed to this repo**, so the

## 星数曲线

```mermaid
xychart-beta
    title "exmergo/research-llm-car-wash-test 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-25 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `25a3e0ab4292` · [字段定义](../../DATASET.md)*
