# somastllc/somali-nlp-corpus

⭐ 108 · Rust · 推送 2026-10-19 · [GitHub](https://github.com/somastllc/somali-nlp-corpus) · [官网](https://www.somast.so/en/datasets/somali-nlp-corpus) · 组织维护

**索马里语 NLP 语料库与 Rust 数据处理管线，产出训练用 JSONL**

面向索马里语这一低资源语言的开放文本语料库项目：用 Rust 实现的流式管线下载 14 个公共数据集（HPLT、mC4、OPUS、Wikipedia 等），经合并、精确去重、清洗、语言识别、MinHash/LSH 近重去除后产出 8.27 亿词、11.3 亿 subword token 的训练用 JSONL；每条记录携带来源、许可、内容哈希与质量元数据，并按记录自身许可导出 open/non-commercial 两个 Parquet 层。附带 48k 词表 ByteLevel BPE 分词器及可复现训练脚本。语料以 gated 数据集形式发布于 Hugging Face，完整构建约需 45 GB 磁盘。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 个公共来源合并去重后产出 791 万文档 / 8.27 亿词的训练就绪 JSONL
- 记录级来源、许可、内容哈希与去重元数据，按许可字段导出 open/non-commercial 双层
- 48k 词表 ByteLevel BPE 分词器，round-trip fidelity 1.000，含可复现训练与评测脚本
- Rust 流式管线，各阶段留存率与拒绝统计可审计

## 适用场景

- 为索马里语 LLM 预训练或微调获取语料
- 研究低资源语言的数据清洗与去重管线
- 按商业/非商业许可分层选用语料子集

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L8: Somali NLP Corpus downloads public Somali datasets, normalizes and filters their text,
> L9: removes exact and near duplicates, and emits training-ready JSONL. The repository also

## 星数曲线

```mermaid
xychart-beta
    title "somastllc/somali-nlp-corpus 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-10-23", "2026-10-24"]
    y-axis "stars" 85 --> 109
    line [87, 107, 107]
```

2026-10-19 87 → 2026-10-24 107（+20）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `3976cf27ff96` · [字段定义](../../DATASET.md)*
