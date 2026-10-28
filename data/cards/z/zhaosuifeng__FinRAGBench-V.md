# zhaosuifeng/FinRAGBench-V

⭐ 24 · Python · Apache-2.0 · 推送 2026-01-13 · [GitHub](https://github.com/zhaosuifeng/FinRAGBench-V) · [官网](https://arxiv.org/abs/2505.17471) · 组织维护 · 中文 README

**金融领域多模态 RAG 可视化引用评测基准（EMNLP 2025）**

面向金融文档多模态检索增强生成的基准数据集：构建含 60,780 中文页与 51,219 英文页的多模态语料（研报、财报、招股书、论文、杂志、新闻），并提供人工标注 QA 数据集，覆盖图表、表格、文本及七类问题（时间敏感、数值计算、比较排序、多页查询等）。附带基线系统 RGenCite（检索+生成+页级/块级可视化引用）与自动引用评测方法（多级 precision/recall，边界框与图像裁剪对齐评估）。通过 git clone + pip 源码安装，按检索、生成、评测三步运行。

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

- 112k 页中英多模态金融语料，源自 2,209 份真实金融文档
- 人工标注 QA 数据集，覆盖 7 类问题与图表/表格/文本异构类型
- RGenCite 基线支持页级与块级细粒度可视化引用
- 自动引用评测：多级 precision/recall，边界框与图像裁剪对齐

## 适用场景

- 评测多模态大模型在金融文档问答中的引用忠实性
- 作为多模态 RAG 检索与生成系统的对比基准
- 复现或扩展金融领域视觉引用评测方法

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: FinRAGBench-V is a **comprehensive benchmark for visual retrieval-augmented generation (RAG) in finance**, addressin
> L13: - 📊 **Multimodal Retrieval Corpus:** We construct a multimodal financial corpus by collecting documents from variou
> L15: - 📝 **High-Quality QA Dataset:** We construct a high-quality, human-annotated question-answering (QA) dataset spann

## 星数曲线

```mermaid
xychart-beta
    title "zhaosuifeng/FinRAGBench-V 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `650123c855b2` · [字段定义](../../DATASET.md)*
