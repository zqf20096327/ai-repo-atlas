# eth-lre/mathtutorbench

⭐ 45 · Python · 推送 2026-08-27 · [GitHub](https://github.com/eth-lre/mathtutorbench) · [官网](https://eth-lre.github.io/mathtutorbench/) · 组织维护

**评测 LLM 数学导师开放教学能力的基准（EMNLP 2025）**

ETH 维护的基准框架，用 3 项教师技能与 7 个具体任务（解题、苏格拉底提问、错误定位/纠正、脚手架生成、教学指令遵循等，含 hard 版本）评测 LLM 的数学辅导能力。支持 OpenAI 兼容 completion API、Gemini API、OpenRouter 及 vllm 本地部署模型；对推理模型提供思考开关处理；附带 1.5B 脚手架打分奖励模型计算胜率，提供可视化脚本与公开排行榜，支持提交模型与新任务（PR 方式）。以 Python 仓库形式提供，pip 安装依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3 项教师技能 / 7 个任务的统一自动评测框架
- 任务标注教师 ground truth，基于胜率的教师 grounding 评测
- 1.5B 参数脚手架奖励模型，单 GPU 约 10 分钟完成打分
- 支持 completion API / Gemini / OpenRouter / 本地 vllm，含推理模型思考开关处理

## 适用场景

- 我想评测自研模型在数学辅导上的教学能力
- 比较不同 LLM 作为数学导师的表现并提交排行榜
- 为基准贡献新的辅导评测任务

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: **MathTutorBench** is a benchmark which provides a unified framework for evaluating open-ended pedagogical capabilit
> L10: - **Automatic Evaluation**: The benchmark is designed to be run automatically on any new models you are developing.

## 星数曲线

```mermaid
xychart-beta
    title "eth-lre/mathtutorbench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 43 --> 46
    line [44, 45, 45]
```

2026-10-18 44 → 2026-10-28 45（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cff2a1745f83` · [字段定义](../../DATASET.md)*
