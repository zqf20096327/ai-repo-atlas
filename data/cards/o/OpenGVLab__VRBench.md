# OpenGVLab/VRBench

⭐ 28 · Python · Apache-2.0 · 推送 2026-06-04 · [GitHub](https://github.com/OpenGVLab/VRBench) · [官网](https://vrbench.github.io) · 组织维护 · 中文 README

**长叙事视频多步推理基准：960 长视频、8,243 问答对**

ICCV 2025 论文配套的长叙事视频评测基准与评测套件：包含 960 条平均时长 1.6 小时的长视频、8,243 条人工标注的多步问答对与 25,106 条带时间戳的推理步骤，推理链覆盖事件归因、隐式推断等七种类型。评测流程分三步：运行推理脚本生成模型回答，调用 DeepSeek API 对推理过程打分（process-level LLM-guided 评分），再汇总 MCQ 与过程分为最终成绩。已在 12 个 LLM 与 19 个 VLM 上完成评测。代码基于 MMVU 结构实现，数据托管于 Hugging Face。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 960 条长视频 + 8,243 条人工标注多步问答 + 25,106 条带时间戳推理步骤
- 结果（MCQ）与过程（LLM 引导评分）双层评测管线
- 支持本地模型推理（示例为 Qwen2-VL-7B）与 DeepSeek API 过程评分
- 推理模块支持按 video_read_type 字段在 decord 与 pyav 间回退

## 适用场景

- 评测多模态模型在长视频上的多步推理与时间推理能力
- 复现论文对 12 个 LLM 与 19 个 VLM 的评测结果
- 按推理类型细分维度对比模型过程级推理质量

## 场景标签

`模型评测` `多模态` · 领域:评测与运维

## 证据(README 行号)

> L73: We present VRBench, the first long narrative video benchmark crafted for evaluating large models' multi-step reason
> L18: [07/2025] VRBench has been fully open-sourced! Check our data on Huggingface!

## 星数曲线

```mermaid
xychart-beta
    title "OpenGVLab/VRBench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-26 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fb6d479ce414` · [字段定义](../../DATASET.md)*
