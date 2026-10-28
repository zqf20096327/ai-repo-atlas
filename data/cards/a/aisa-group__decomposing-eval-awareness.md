# aisa-group/decomposing-eval-awareness

⭐ 20 · Python · NOASSERTION · 推送 2026-09-29 · [GitHub](https://github.com/aisa-group/decomposing-eval-awareness) · [官网](https://arxiv.org/abs/2605.23055) · 组织维护

**评测意识研究代码与 EvalAwareBench 基准：测量模型是否识别自己在被评测**

论文《Decomposing and Measuring Evaluation Awareness》的实验复现代码：将评测意识分解为环境成分（八类触发因素，如占位符实体、评分式输出格式）与模型成分（识别 vs 行动倾向），并通过思维链监控在九个前沿模型、四个基准上测量识别率与行为变化。提出 EvalAwareBench——100 对安全/能力配对任务、八个因素可独立开关的因素受控基准。代码支持 OpenRouter/Anthropic/OpenAI/DeepSeek 后端，评测默认用 GPT-5 判分模型，并提供 SLURM 集群脚本与 OpenAI Batch API 批量评测路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- EvalAwareBench：100 对安全/能力配对任务，八因素可独立开关
- 覆盖 HarmBench / Agentic Misalignment / AgentHarm / EvalAware-Bench 四个基准的运行与评测脚本
- 思维链评测、自我报告、目的猜测、第三人称、因素分析（9 因素分类、k=5 多数投票）五种评测方法
- 支持 SLURM 阵列作业与 OpenAI Batch API（成本减半）

## 适用场景

- 复现论文中评测意识的测量与因素分析实验
- 用 EvalAwareBench 检验自家模型对各评测触发因素的敏感度
- 在集群上批量运行九个模型的基准评测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L18: Frontier language models sometimes recognize that they are being evaluated and adjust their behavior, undermining v
> L109: ### 2.4 EvalAware-Bench (Our Benchmark)
> L113: The full dataset is also available on Hugging Face: https://huggingface.co/datasets/aisa-group/EvalAwareBench

## 星数曲线

```mermaid
xychart-beta
    title "aisa-group/decomposing-eval-awareness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0ffdd02ca85e` · [字段定义](../../DATASET.md)*
