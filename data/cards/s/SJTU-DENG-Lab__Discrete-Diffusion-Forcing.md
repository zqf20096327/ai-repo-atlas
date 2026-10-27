# SJTU-DENG-Lab/Discrete-Diffusion-Forcing

⭐ 263 · Python · MIT · 推送 2026-02-03 · [GitHub](https://github.com/SJTU-DENG-Lab/Discrete-Diffusion-Forcing) · [官网](https://SJTU-DENG-Lab.github.io/Discrete-Diffusion-Forcing/) · 组织维护 · 中文 README

**加速扩散语言模型推理的训练与推理范式（D2F）**

上海交大团队的 ICLR 2026 论文官方代码库，提供离散扩散强制（D2F）的训练与推理实现：通过块级因果注意力使 dLLM 兼容 KV Cache，经非对称蒸馏从预训练双向 dLLM 训练学生模型，推理时用流水线并行解码同时精炼多个块。基准显示吞吐较 LLaDA/Dream 基线提升最多 50 倍以上，较 LLaMA3-8B 提升至 2.5 倍；含初步 vLLM 集成（HumanEval 分数下降）。面向复现实验的研究者与开发者，通过 git clone 源码运行，附评测、训练脚本与生成 demo。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 块级因果注意力使 dLLM 兼容标准 KV Cache
- 非对称蒸馏：从预训练双向 dLLM 训练 cache 友好学生模型
- 流水线并行解码异步精炼多个块以提升吞吐
- 提供 D2F-Dream / D2F-LLaDA LoRA 与初步 vLLM 引擎集成

## 适用场景

- 复现论文的评测与训练结果
- 在自己的项目中使用 D2F 模型做推理
- 研究 dLLM 推理加速与 vLLM 集成

## 场景标签

`微调` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L20: **Discrete Diffusion Forcing (D2F)** is a novel training and inference paradigm that, for the first time, enables o
> L26: This repository provides the code to reproduce our evaluation results and run generation demos.

## 星数曲线

```mermaid
xychart-beta
    title "SJTU-DENG-Lab/Discrete-Diffusion-Forcing 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 262 --> 264
    line [263, 263]
```

2026-10-18 263 → 2026-10-27 263（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `7ced1fc204f4` · [字段定义](../../DATASET.md)*
