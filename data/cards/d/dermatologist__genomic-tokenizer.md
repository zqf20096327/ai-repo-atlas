# dermatologist/genomic-tokenizer

⭐ 14 · Python · MPL-2.0 · 推送 2026-01-26 · [GitHub](https://github.com/dermatologist/genomic-tokenizer) · [官网](https://www.biorxiv.org/content/10.1101/2025.04.02.646836v1) · 个人维护

**面向 DNA 序列的生物驱动分词器，供预训练 Transformer 模型**

以 Python 包提供的 DNA 序列分词器，将分子生物学中心法则的流程编码进 HuggingFace transformers 的标准 tokenizer 接口，用于在 DNA 序列上预训练基础 Transformer 模型。分词机制：定位首个起始密码子 ATG，从其起按长度 3 切分密码子，同义密码子映射为同一 token，终止密码子转为 [SEP] token；Fasta 头部信息被忽略。面向基因组学与生物信息学研究者，作者附有预印本与引用条目，请求使用者在研究中引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按中心法则流程切分：从首个 ATG 起按密码子（长度 3）分词
- 同义密码子映射为同一 token，终止密码子输出 [SEP]
- 兼容 HuggingFace transformers 标准分词器接口
- 支持直接读取 Fasta 序列（头部忽略）

## 适用场景

- 在 DNA 序列语料上预训练基础 Transformer 模型
- 以密码子/同义性为单位做基因组序列的 token 化
- 接入 HuggingFace 流水线处理 Fasta 输入

## 场景标签

 · 领域:生物信息学/NLP 工具

## 证据(README 行号)

> L7: This is a tokenizer for DNA :chains: that aligns with the central dogma of molecular biology. The Genomic Tokenizer 
> L39: * Identify the first occurrence of the start codon `ATG`.

## 星数曲线

```mermaid
xychart-beta
    title "dermatologist/genomic-tokenizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f1d431993e1f` · [字段定义](../../DATASET.md)*
