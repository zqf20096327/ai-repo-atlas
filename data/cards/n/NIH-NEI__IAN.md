# NIH-NEI/IAN

⭐ 20 · R · NOASSERTION · 推送 2026-02-23 · [GitHub](https://github.com/NIH-NEI/IAN) · 组织维护

**组学数据富集分析与 LLM 解读的 R 包**

NIH/NEI 免疫学实验室开发的 R 包：读取 DESeq2 差异表达结果、Seurat FindMarkers 输出或自定义 DEG 列表，执行 WikiPathways/KEGG/Reactome/GO/ChEA 富集分析与 STRING 蛋白互作网络分析，再用基于 Google Gemini API 的多智能体 LLM 系统对结果做汇总、分类与解释，生成机制模型网络与 HTML 报告。面向生物医学研究者，按量付费调用 API，提供 Docker 容器版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 DESeq2/Seurat/自定义 DEG 列表输入
- 多通路数据库富集分析与 STRING 蛋白互作、hub 基因打分
- Gemini 多智能体 LLM 解读并生成机制模型网络与 HTML 报告
- Docker 容器化保证分析可复现

## 适用场景

- 对差异表达基因做多数据库富集分析并获取 LLM 解读报告
- 构建疾病相关的机制模型网络用于假设生成
- 复现论文评估数据（如葡萄膜炎、白塞病数据集）的分析流程

## 场景标签

`多智能体` `科研工具` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L6: **IAN** is an R package designed to perform contextually integrated "omics" data analysis and reasoning, leveraging 
> L14: * **LLM-Driven Interpretation:** Employs a multi-agent system with carefully crafted LLM prompts to summarize, cate
> L40: * IAN uses Google Gemini as the LLM.

## 星数曲线

```mermaid
xychart-beta
    title "NIH-NEI/IAN 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `43d19dcdc546` · [字段定义](../../DATASET.md)*
