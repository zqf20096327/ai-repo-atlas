# LiuLab-Bioelectronics-Harvard/STAgent

⭐ 63 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-11 · [GitHub](https://github.com/LiuLab-Bioelectronics-Harvard/STAgent) · [官网](https://doi.org/10.1101/2025.04.01.646731) · 组织维护

**空间转录组数据分析的多模态 LLM agent，面向科研用户**

基于 Streamlit 的空间转录组 AI agent，读取 .h5ad 数据集，通过自然语言对话（支持文本、语音、图像输入）完成预处理、分析、可视化与报告生成的端到端流程。内置冲突检查机制核验中间结论，可选接入 STAligner 空间域识别与 Tangram 基因插补外部工作流（需独立 GPU conda 环境），并集成文献检索模块提供生物学背景。需配置 OpenAI/Anthropic/Google 至少一家 API key，语音转写需 Whisper API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本/语音/图像多模态输入的对话式分析流程
- 冲突检查：复核中间结论的一致性与证据支持
- 可选 STAligner 空间域识别与 Tangram 基因插补外部工作流
- 结合文献检索的深度研究与结构化报告生成

## 适用场景

- 用自然语言对话探索空间转录组数据，无需编程经验
- 从原始 .h5ad 数据生成含方法与发现的解释性报告
- 跨样本空间域对齐与基因插补分析

## 场景标签

`数据分析` `科研工具` · 领域:效率与自动化

## 证据(README 行号)

> L9: **STAgent** is a Streamlit-based spatial transcriptomics AI agent for interactive analysis of `.h5ad` datasets. This
> L24: Supports text, voice, and image-based inputs, making it easier for researchers to explore datasets in the way that 
> L27: Combines tissue images, spatial gene expression patterns, and user questions to help carry out analysis steps and i

## 星数曲线

```mermaid
xychart-beta
    title "LiuLab-Bioelectronics-Harvard/STAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-24 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `188153ed0a37` · [字段定义](../../DATASET.md)*
