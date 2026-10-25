# UCSC-VLAA/m1

⭐ 51 · Jupyter Notebook · Apache-2.0 · 推送 2025-12-21 · [GitHub](https://github.com/UCSC-VLAA/m1) · 组织维护

**医学推理大语言模型：少量数据微调+测试时扩展提升推理**

UCSC-VLAA 发布的医学 LLM 及配套训练/评测/数据代码：基于 Qwen2.5-7B/32B-Instruct，在 1K–23K 验证过的医学推理样本上做 SFT，并在推理阶段通过 token 预算扩展思考长度以提升医学 QA 表现（约 4K token 预算后可能因过度思考退化）。开源 7B/32B 模型、数据集与数据构建流水线（采集、蒸馏、去污染、按领域筛选、tokenize）。推理可部署于 vllm 或 Sglang，训练脚本在 src/train/sft.py，评测基于 sglang。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Qwen2.5-7B/32B 的 SFT 模型（1K–23K 医学推理样本）
- 推理阶段 token 预算扩展策略提升医学 QA 表现
- 完整数据构建流水线（采集/蒸馏/去污染/领域筛选/tokenize）
- 开源模型、数据、训练与评测代码及结果

## 适用场景

- 医学考试问答与医学推理任务的模型选型
- 复现测试时扩展在医学推理上的实验
- 基于其数据流水线构建自有医学推理数据集

## 场景标签

`微调` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: **m1** is a medical LLM designed to enhance reasoning through efficient test-time scaling. It enables lightweight mo
> L39: m1 can be used just like Qwen2.5-7b-Instruct. You can deploy it with tools like vllm or Sglang (we provide an examp

## 星数曲线

```mermaid
xychart-beta
    title "UCSC-VLAA/m1 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 49 --> 52
    line [50, 51, 51]
```

2026-10-18 50 → 2026-10-25 51（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4b99b650deb9` · [字段定义](../../DATASET.md)*
