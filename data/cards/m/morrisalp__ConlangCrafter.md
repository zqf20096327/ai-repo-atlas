# morrisalp/ConlangCrafter

⭐ 49 · Python · MIT · 推送 2026-07-25 · [GitHub](https://github.com/morrisalp/ConlangCrafter) · [官网](https://conlangcrafter.github.io) · 组织维护

**多阶段 LLM 流水线自动构造人造语言（语音/语法/词汇/翻译）**

基于 ACL 2026 Oral 论文的研究系统：通过多跳 LLM 流水线分阶段生成人造语言，涵盖音系、语法、词汇与翻译能力。支持 Google Gemini、OpenAI、DeepSeek（经 Together AI）模型，默认 gemini-2.5-pro。带 QA 自精炼循环、断点续跑、构造性翻译（翻译中扩充词汇语法）与 WALS 类型学特征提取。提供 64 个预生成语言的数据集，Python 源码运行，需配置 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多阶段流水线生成音系、语法、词汇与翻译
- QA 自精炼循环默认开启，支持断点续跑
- 构造性翻译：新词汇语法回写语言草稿
- WALS 类型学特征提取（词序/形态/音位库等）

## 适用场景

- 语言学研究者批量生成多样性人造语言
- 创作虚构作品所需的自定义语言
- 复现论文并做类型学多样性分析

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: We introduce a fully automated system for constructing languages (conlangs) using large language models. Our multi-s
> L24:    python src/run_pipeline.py

## 星数曲线

```mermaid
xychart-beta
    title "morrisalp/ConlangCrafter 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 47 --> 50
    line [48, 49, 49]
```

2026-10-18 48 → 2026-10-27 49（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `5c8266a84c61` · [字段定义](../../DATASET.md)*
