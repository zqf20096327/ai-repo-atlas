# huggingface/fineweb-2

⭐ 268 · Python · Apache-2.0 · 推送 2025-10-27 · [GitHub](https://github.com/huggingface/fineweb-2) · 组织维护

**1000+ 语言预训练数据集 FineWeb 2 的处理管线代码库**

Hugging Face 团队发布的多语言预训练数据集 FineWeb 2 配套代码仓库，为超过 1000 种语言提供经筛选的预训练数据（数据本体托管于 HuggingFaceFW/fineweb-2）。管线基于原 FineWeb 的非英语数据，逐语言调优过滤阈值（configs 目录的 YAML 配置），执行语言识别（GlotLID）、按语言全局去重（记录 minhash_cluster_size 供再水化上采样）、过滤与 PII 匿名化。附带 FineTasks 评测、1.46B 模型消融训练与 tokenize 脚本；数据集 ODC-By 许可，代码 Apache 2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐语言单独调优过滤器阈值与停用词（YAML 配置）
- 按语言全局去重并保存 minhash_cluster_size，支持再水化上采样
- 提供 FineTasks 评测、nanotron 训练与预分词脚本
- 附论文（arXiv 2506.20920）与参考数据集处理代码

## 适用场景

- 获取 1000+ 语言的高质量 LLM 预训练语料
- 复现或定制多语言数据处理管线
- 研究去重簇上采样（re-hydration）对训练效果的影响

## 场景标签

 · 领域:NLP/预训练数据

## 证据(README 行号)

> L4: FineWeb 2 is the second iteration of the popular 🍷 FineWeb dataset, bringing high quality pretraining data to over 1
> L10: The processing pipeline had to be heavily adapted for a multilingual setting. As each language has its own peculiar

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/fineweb-2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 267 --> 269
    line [268, 268]
```

2026-10-18 268 → 2026-10-22 268（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a319aa4d16bc` · [字段定义](../../DATASET.md)*
