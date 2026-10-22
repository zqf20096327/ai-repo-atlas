# huggingface/finepdfs

⭐ 191 · Python · NOASSERTION · 推送 2026-01-09 · [GitHub](https://github.com/huggingface/finepdfs) · [官网](https://huggingface.co/datasets/HuggingFaceFW/finepdfs) · 组织维护

**FinePDFs 数据集的端到端 PDF 数据处理流水线代码**

HuggingFace 团队随 FinePDFs 数据集发布的代码库：对大规模 CommonCrawl PDF 数据执行过滤、文本抽取、OCR 路由、后处理、去重、语言/质量分类与打包。关键机制包括 XGBoost OCR 路由分类器、OpenVINO INT8 量化的 Docling 布局模型、基于 Gemma 标注的语言阈值选取、蒸馏 edu/dclm 质量分类器（英文用 ModernBERT 多头结构）。需要 GPU（vLLM 步骤），安装采用 uv 工作区并 vendor 特定版本 Docling。README 声明该流水线为生产流水线的粗略复现，部分代码仅为参考实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 端到端流水线：过滤/抽取/OCR/去重/分类/打包
- XGBoost OCR 路由分类器与 OpenVINO INT8 量化 Docling 布局模型
- 基于 Qwen3 标注蒸馏的 edu/dclm 质量分类器
- 多语言语言过滤阈值自动发现（F-beta 优先精度）

## 适用场景

- 复现或定制大规模 PDF 文本数据集的构建流程
- 训练自己的 OCR 路由或质量分类器
- 了解生产级语料清洗管线的各步骤实现

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L5: This repository accompanies the FinePDFs dataset release and contains the end‑to‑end code to filter, extract, OCR, p
> L20: Requirements are in `pyproject.toml` (notable: `torch==2.6.0`, `vllm>=0.8.5.post1`, `pymupdf==1.26.1`). A GPU is ne

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/finepdfs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 190 --> 192
    line [191, 191]
```

2026-10-18 191 → 2026-10-22 191（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `65048a367d73` · [字段定义](../../DATASET.md)*
