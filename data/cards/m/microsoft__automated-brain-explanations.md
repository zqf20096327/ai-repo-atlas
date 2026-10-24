# microsoft/automated-brain-explanations

⭐ 67 · Jupyter Notebook · MIT · 推送 2026-06-01 · [GitHub](https://github.com/microsoft/automated-brain-explanations) · [官网](https://microsoft.github.io/automated-brain-explanations/) · 组织维护

**用 LLM 与 fMRI 数据生成并验证脑语言加工解释的科研代码库**

微软团队维护的神经科学研究代码库，支撑 2 项神经科学研究与多项 ML 研究：包括生成因果测试（GCT，用 LLM 生成脑区语言选择性的简洁解释并用 LLM 生成刺激做后续实验验证）、QA 编码模型（用 LLM 回答是非题标注语言刺激构建特征）、可解释嵌入（QA-Emb）、黑箱文本模块自然语言解释（SASC）等。面向脑成像数据分析研究者，数据基于 HuthLab fMRI 被动听觉数据集，通过 uv 安装 neuro 包，运行 experiments 脚本拟合编码模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GCT：从预测模型生成脑区解释并用 LLM 生成刺激做实验验证
- QA 编码模型/QA-Emb：用 LLM 回答是非题构建可解释特征与嵌入
- Aug-imodels：训练期用 LLM、推理期完全可解释的预测模型
- 提供 3 名被试快速入门数据与 TR 级解码示例

## 适用场景

- 分析 fMRI 语言数据并拟合编码模型
- 为脑区的语言选择性生成自然语言解释并实验验证
- 构建可解释的文本嵌入与预测模型做科研对比

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3:  We’ve been studying how to scalably answer this question using
> L15: Generative causal testing (GCT) is a framework for generating concise explanations of language selectivity in the b
> L25: Aug-imodels is a framework for LLMs to build extremely efficient and interpretable prediction models, e.g. linear n

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/automated-brain-explanations 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-24 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `b675541aeba2` · [字段定义](../../DATASET.md)*
