# huspacy/huspacy

⭐ 193 · Python · Apache-2.0 · 推送 2025-11-19 · [GitHub](https://github.com/huspacy/huspacy) · [官网](https://huspacy.github.io) · 组织维护

**面向匈牙利语的 spaCy 工业级 NLP 工具包与模型集**

基于 spaCy 构建的匈牙利语自然语言处理库，提供分词、断句、词形还原、词性标注（含形态句法特征）、依存句法分析与命名实体识别的完整流水线，并附带词/短语向量。提供 4 个预训练模型：CNN 版 hu_core_news_lg（默认）、基于 huBERT 的 hu_core_news_trf（建议 GPU）、高吞吐的 hu_core_news_md，以及基于 XLM-RoBERTa-large 的实验性 trf_xl。模型发布到 Hugging Face Hub，兼容 spaCy API，可 pip 安装后经 huspacy.download() 获取模型。由 SzegedAI 团队在匈牙利 AI 国家实验室 MILAB 计划下实现，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 完整匈牙利语流水线：分词/断句/词形还原/词性/依存分析/NER
- 4 个预训练模型（CNN、huBERT、XLM-RoBERTa-large 变体）覆盖 CPU/GPU 场景
- 附带预训练词向量，兼容 spaCy API
- 模型发布于 Hugging Face Hub，pip 可直接安装

## 适用场景

- 对匈牙利语文本做命名实体识别与依存句法分析
- 构建匈牙利语信息抽取或检索管线时获取词向量
- 按吞吐或精度需求选择 CPU/GPU 模型处理大规模语料

## 场景标签

 · 领域:自然语言处理

## 证据(README 行号)

> L19: HuSpaCy is a spaCy library providing industrial-strength Hungarian language processing facilities through spaCy mod
> L20: The released pipelines consist of a tokenizer, sentence splitter, lemmatizer, tagger (predicting morphological feat

## 星数曲线

```mermaid
xychart-beta
    title "huspacy/huspacy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 192 --> 194
    line [193, 193]
```

2026-10-18 193 → 2026-10-24 193（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8573cff22729` · [字段定义](../../DATASET.md)*
