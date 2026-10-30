# hugoabonizio/clinical-protocols-br

⭐ 15 · Python · 推送 2026-05-07 · [GitHub](https://github.com/hugoabonizio/clinical-protocols-br) · [官网](https://hugoabonizio.github.io/clinical-protocols-br/) · 个人维护

**面向巴西 SUS 临床指南的 Qwen2.5-14B 领域适配：模型、数据集与基准**

研究仓库，含三阶段适配流水线：先由四个生成 LLM 将巴西卫生部 178 份官方临床指南改写为约 7000 万 token 合成语料，再对 Qwen2.5-14B-Instruct 做持续预训练（CPT），最后用 GRPO+LoRA 强化学习。发布两个基准（HealthBench-BR 真假临床断言、PCDT-QA 开放问答）、8 个模型 checkpoint 与训练脚本。评测含 LLM-as-a-judge 流水线与 RAG 实验，并提供 OOD 遗忘评测目录。面向医疗 NLP 研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 178 份官方指南生成约 7000 万 token 合成语料（四个生成 LLM）
- CPT + GRPO(LoRA) 两阶段适配 Qwen2.5-14B-Instruct
- 两个基准：HealthBench-BR（1,780 真假断言）与 PCDT-QA（890 开放问答）
- 8 个消融 checkpoint 与 CPT/SFT/RL 训练脚本开源

## 适用场景

- 下载巴西葡萄牙语临床领域适配的 14B 模型做本地推理
- 用 HealthBench-BR / PCDT-QA 评测医疗 LLM 的指南事实召回
- 复现 CPT+GRPO 领域适配实验或做遗忘（OOD）分析

## 场景标签

`微调` `强化学习` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: Adapting LLMs to the clinical knowledge of Brazil's Unified Health System (SUS) through continual pre-training (CPT)
> L9: We collected the 178 official clinical guidelines published by the Brazilian Ministry of Health (PCDTs, DDTs, Protoc
> L48: **Models** (Qwen2.5-14B-Instruct base, with test-split accuracy on HB-BR / PCDT-QA)

## 星数曲线

```mermaid
xychart-beta
    title "hugoabonizio/clinical-protocols-br 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `de6e7e135ade` · [字段定义](../../DATASET.md)*
