# ANGEL-NTU/ESGenius

⭐ 18 · HTML · Apache-2.0 · 推送 2026-06-15 · [GitHub](https://github.com/ANGEL-NTU/ESGenius) · [官网](https://angel-ntu.github.io/ESGenius/) · 组织维护

**评测 LLM 的 ESG 与可持续知识基准（1,136 题多项选择）**

EMNLP 2025 Main Oral 论文配套基准：1,136 道带出处（IPCC、GRI、SASB、IFRS/ISSB 等）的 ESG 与可持续性多项选择题，含普通版 CSV/JSON 与带参考文档/页码/摘录的 reference-aware 版本；提供本地 Hugging Face 模型、参考片段前置提示与 Dashscope 兼容 Qwen API 三条评测脚本路径，结果以 Excel 与交互式 50 模型热力图呈现，数据集同步发布于 Hugging Face（cy0307/ESGenius）。面向研究人员与模型评测者。

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

- 1,136 道专家编制、来源可溯的 ESG 多项选择题，含 Z（不确定）选项协议
- reference-aware 版本提供 ref_doc/ref_page/source_text 字段，支持审计与检索实验
- 三条评测路径：本地 HF 模型、参考感知提示、Dashscope 兼容 Qwen API
- 已评测 50 个模型，附交互式 Plotly 模型-题目热力图

## 适用场景

- 评测大模型在 ESG 披露与可持续报告领域的知识水平
- 做引用感知/检索增强的对照评测实验
- 复现论文结果或诊断模型在具体题目上的表现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L24: ESGenius is an expert multiple-choice benchmark for evaluating whether large language models understand ESG and sus
> L46: |Questions|1,136 multiple-choice ESG and sustainability questions|

## 星数曲线

```mermaid
xychart-beta
    title "ANGEL-NTU/ESGenius 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `730ad1d565e2` · [字段定义](../../DATASET.md)*
