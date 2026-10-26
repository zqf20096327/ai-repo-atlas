# tahrirchi/uzlib

⭐ 27 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/tahrirchi/uzlib) · 组织维护

**乌兹别克语语言学基准：评测 LLM 的乌语能力**

UzLiB 是面向大语言模型的多项选择题基准，用于评测模型对乌兹别克语正确形式、用法与细微差别的理解。题目取自四个乌语语言学 Telegram 频道的测验，经人工校验与标准化（含拉丁转写与选项乱序），原始与处理后数据均在 data/ 目录。评测采用统一提示模板与标准生成参数（temperature=1.0, top-p=0.95），提供评测脚本、模型输出与本地 vLLM 评测路径，支持生成排行榜并接受新模型贡献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 首个综合性乌兹别克语语言学多项选择题基准
- 题目来自 4 个乌语语言学 Telegram 频道并经人工校验标准化
- 统一提示模板与生成参数（temperature=1.0, top-p=0.95）评测
- 支持通过 vLLM 本地部署开源模型（Mistral/Llama/Gemma）评测

## 适用场景

- 评测我的模型在乌兹别克语语言学上的表现
- 复现或扩展排行榜，提交新模型的评测结果
- 获取已标准化的乌语语言学测试题数据集

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: UzLiB is the first comprehensive multiple-choice question benchmark designed to evaluate the linguistic abilities of
> L13: UzLiB questions were sourced from popular quizzes on the following Telegram channels specializing in Uzbek linguist
> L25: The results presented in the leaderboard were obtained using a consistent prompt template and standard generation p

## 星数曲线

```mermaid
xychart-beta
    title "tahrirchi/uzlib 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-26 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `955494c4e3d4` · [字段定义](../../DATASET.md)*
