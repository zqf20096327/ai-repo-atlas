# aaronkaplan/cti-llm

⭐ 24 · Jupyter Notebook · 推送 2026-09-09 · [GitHub](https://github.com/aaronkaplan/cti-llm) · 个人维护

**LLM 用于 CTI 报告的用例演示代码集（会议演讲配套）**

配合 FIRST Fukuoka 2024 演讲的代码仓库，展示 LLM 在网络威胁情报（CTI）中的五个用例：自由文本 CTI 摘要、命名实体识别（NER）、基于 RAG 的 CTI 问答、TTP 标签提取，以及提取“谁用何工具对谁做了什么”关系的图谱抽取。每个用例有独立子目录，需查看各子目录 README 获取运行方式。数据来源为 Palo Alto UNIT42 GitHub 与 CISA 通告网站的 STIX 报告。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五个 CTI 用例：摘要/NER/RAG 问答/TTP 标注/图谱关系抽取
- 每用例独立子目录组织
- STIX 数据取自 UNIT42 GitHub 与 CISA 通告

## 适用场景

- 了解 LLM 在威胁情报分析中的应用方式
- 复用 CTI 文本摘要与实体识别的示例代码
- 基于 RAG 对 CTI 文本做问答实验

## 场景标签

`RAG` `网络安全` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L3: This repo contains the code for the presentation of our talk on how to use LLMs for CTI purposes.
> L10: 1) *UC 1*: Summarization of free text CTI

## 星数曲线

```mermaid
xychart-beta
    title "aaronkaplan/cti-llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2ea79dc44b8f` · [字段定义](../../DATASET.md)*
