# google-deepmind/anthro-benchmark

⭐ 14 · Python · Apache-2.0 · 推送 2025-11-17 · [GitHub](https://github.com/google-deepmind/anthro-benchmark) · 组织维护

**评测 LLM 拟人化行为的对话生成、评级与分析库**

AnthroBench 是 Google DeepMind 开发的 Python 库，配套论文《AnthroBench: A Multi-turn Evaluation of Anthropomorphic Behaviours in Large Language Models》。它通过用户 LLM 与目标 LLM 生成多轮对话，用 LLM 分类器（可多模型多数投票、多次采样）对对话轮次按拟人化行为（如 empathy、desires）评级，部分行为（第一人称代词使用）用 regex 逻辑处理，并生成汇总与图表。行为分四类：internal states、personhood、physical activity、relationship building。通过 API key 接入 OpenAI、Gemini 等 LLM 提供商，需设置对应环境变量。安装方式为 git clone 后 pip install -e .，提供 anthro-eval CLI。Apache-2.0 许可。

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

- 用户 LLM 与目标 LLM 生成多轮对话
- LLM 分类器按拟人化行为评级，支持多模型与多样本多数投票
- 四类行为类别过滤提示集（internal states/personhood/physical activity/relationship building）
- 评级结果分析与可视化，输出汇总与图表

## 适用场景

- 评测多个 LLM 在对话中表现出的拟人化行为
- 研究 LLM 的共情、人格等行为维度差异
- 生成并保存带行为标签的多轮对话数据集

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A library for generating, rating, and analyzing dialogues to evaluate anthropomorphic behaviors in LLMs, developed i
> L9: - `anthro_benchmark/generator`: Handles dialogue generation between the user LLM and target LLM.
> L10: - `anthro_benchmark/classifier`: Contains logic for classifying dialogue turns based on anthropomorphic behaviors, 

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/anthro-benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `cc417fdf199a` · [字段定义](../../DATASET.md)*
