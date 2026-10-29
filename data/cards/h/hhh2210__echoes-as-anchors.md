# hhh2210/echoes-as-anchors

⭐ 45 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/hhh2210/echoes-as-anchors) · [官网](https://hhh2210.github.io/projects/echoes-as-anchors/) · 个人维护

**ICLR 2026 论文代码：研究 LLM 推理中 Echo of Prompt 的作用机制**

论文 'Echoes as Anchors' 的官方代码仓库，研究大型推理模型在思维链中复述用户问题（Echo of Prompt, EOP）的行为。提供三个组件的实现：Echo-Distilled SFT（ED-SFT）数据准备脚本、免训练的 Echoic Prompting（EP）推理策略，以及用 MLP 探针、概率与注意力分析测量 EOP 与推理表现的关系。概率与注意力分析仅基于 DeepSeek-R1-Distill-Llama-8B 在 GSM8K 的 1,319 条轨迹。提供打包评测器（pip 安装，支持 HF 与 vLLM 后端）、conda 环境配置与三个复现工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ED-SFT 数据准备：用教师模型生成含 EOP 的 CoT 蒸馏数据
- Echoic Prompting：两阶段生成的免训练推理策略
- MLP 探针检测推理过程中的复述模式（测试准确率 0.912）
- echoes-lm-eval 命令行评测器，支持 Transformers 与 vLLM 后端，写出 run_manifest.json

## 适用场景

- 复现论文中 ED-SFT、MLP 探针与 EP 评测的实验结果
- 研究生成含 Echo of Prompt 的微调数据
- 用概率与注意力工具分析推理轨迹中的复述行为

## 场景标签

`模型评测` `微调` · 领域:评测与运维

## 证据(README 行号)

> L3: This repository contains the source code for the ICLR 2026 paper **"Echoes as Anchors: Probabilistic Costs and Atten
> L24: The repository provides code for three linked components: **echo-distilled supervised fine-tuning (ED-SFT)**, **ech
> L43: The codebase includes implementations for:

## 星数曲线

```mermaid
xychart-beta
    title "hhh2210/echoes-as-anchors 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 43 --> 46
    line [44, 45, 45]
```

2026-10-18 44 → 2026-10-29 45（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8164f0c6055e` · [字段定义](../../DATASET.md)*
