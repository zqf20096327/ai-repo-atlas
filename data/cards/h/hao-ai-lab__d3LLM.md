# hao-ai-lab/d3LLM

⭐ 157 · Python · 推送 2026-05-01 · [GitHub](https://github.com/hao-ai-lab/d3LLM) · [官网](https://arxiv.org/abs/2601.07568) · 组织维护

**ICML'26 论文官方实现：伪轨迹蒸馏的高速扩散语言模型及训练评测代码**

d3LLM 的官方开源实现，包含三个已发布于 HuggingFace 的模型（d3LLM-LLaDA、d3LLM-Dream、d3LLM-Coder）、DeepSpeed 训练脚本、蒸馏数据集与基准评测代码。核心机制为伪轨迹蒸馏（提取教师模型的解码顺序指导学生模型）与基于熵的多块并行解码加 KV-Cache 周期刷新；README 报告在 H100 上相对自回归模型 5× 加速。限制：蒸馏数据以代码与数学推理任务为主，加速效果主要出现在此类提示上。另提供 SGLang 推理支持与扩散 LLM 排行榜。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 伪轨迹蒸馏 + 多块并行解码，README 报告 5-10× TPF 加速
- 提供 DeepSpeed 训练脚本与已提取的蒸馏轨迹数据集
- d3LLM-LLaDA / Dream / Coder 三个模型发布于 HuggingFace
- SGLang 引擎推理支持与多基准评测脚本

## 适用场景

- 研究与复现扩散语言模型蒸馏训练方法
- 在代码与数学推理任务上部署高速扩散 LLM 推理
- 对比评测扩散 LLM 与自回归基线（含 AUP 指标）

## 场景标签

`模型训练` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L13: This is the official implementation of the paper d3LLM: Ultra-Fast Diffusion LLM using Pseudo-Trajectory Distillati
> L33: **d3LLM** (_pseuDo-Distilled Diffusion LLM_) is a novel framework for building ultra-fast diffusion language models
> L91: Based on the d3LLM framework, we have released three models on 🤗 HuggingFace: d3LLM-LLaDA, d3LLM-Dream, and d3LLM-C

## 星数曲线

```mermaid
xychart-beta
    title "hao-ai-lab/d3LLM 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 155 --> 158
    line [156, 157, 157]
```

2026-10-18 156 → 2026-10-24 157（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `8b1387745fac` · [字段定义](../../DATASET.md)*
