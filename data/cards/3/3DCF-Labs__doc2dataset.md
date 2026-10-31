# 3DCF-Labs/doc2dataset

⭐ 54 · Rust · Apache-2.0 · 推送 2026-02-10 · [GitHub](https://github.com/3DCF-Labs/doc2dataset) · 组织维护

**面向 RAG 与微调的文档转数据集流水线，含数值完整性校验**

以 Rust 为核心的开源文档层与 doc→dataset 流水线：将 PDF、Markdown、HTML、CSV、TeX、图像等格式摄取为三份规范化 JSONL 索引（documents/pages/cells），为数值单元格提取 NumGuard 哈希用于完整性校验，并生成 QA/Summary/RAG 样本，导出为 HuggingFace、LLaMA-Factory、Axolotl、OpenAI 微调及通用 RAG 格式。通过 YAML 配置或 CLI 运行，可配置 LLM 提供方（OpenAI/Anthropic/local 等），另提供 HTTP 服务（Axum）与捆绑浏览器 UI、Docker 镜像及 Python/Node 绑定。面向 ML 平台团队、金融/合规团队与 LLM 研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多格式摄取（PDF/MD/HTML/JSON/CSV/TeX/图像等）并转换为规范化 macro-cell JSONL 索引
- NumGuard 数值单元格哈希校验，评测中 A 桶损坏检出率 recall 1.0
- QA/Summary/RAG 样本生成与 HuggingFace/LLaMA-Factory/Axolotl/OpenAI 多框架导出
- HTTP 服务 + 浏览器 UI、Docker 镜像、Python/Node 绑定

## 适用场景

- 把公司报告与文档批量转成微调数据集
- 为 RAG 流水线构建 token 更省的文档上下文
- 审计文档处理流水线中的数值完整性

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: Open document layer and doc→dataset pipeline for LLMs, with NumGuard numeric integrity and multi-framework exports.
> L5: 3DCF/doc2dataset ingests PDFs, Markdown, plain text and other text-like formats into a normalized index (`documents.
> L29: - **ML / AI platform teams** – need a reproducible document layer that feeds RAG and fine-tuning pipelines.

## 星数曲线

```mermaid
xychart-beta
    title "3DCF-Labs/doc2dataset 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-31 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `1ac1da50345b` · [字段定义](../../DATASET.md)*
