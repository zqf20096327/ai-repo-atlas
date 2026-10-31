# lfoppiano/grobid-superconductors

⭐ 25 · HTML · Apache-2.0 · 推送 2026-09-02 · [GitHub](https://github.com/lfoppiano/grobid-superconductors) · 个人维护

**从科学文献中提取超导材料与属性的 Grobid 模块**

基于 GROBID 的文献信息抽取模块：从 PDF 科学文献中识别并链接超导材料与其属性（临界温度 Tc、测量方法类型、施加压力），同时识别空间群与晶体结构。抽取步骤为基于机器学习的 NER 任务，支持线性 CRF（Wapiti）、BiLSTM-CRF 及 BERT/SciBERT（DeLFT）等模型；链接步骤为基于 SpaCy 规则的关系抽取，经微服务实现。提供 API 与 UI，输出含书目数据的 JSON。本地构建要求 8<JDK<11；提供 docker-compose 与逐服务 Docker 部署方式；链接等 Python 工具需 Python 3.7 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 材料-属性（Tc/压力/测量方法）抽取与关系链接两步流程
- 支持 CRF、BiLSTM-CRF、BERT/SciBERT 多种模型架构
- 提供 API 与 UI，抽取结果可视化到 PDF 原文
- 提供预训练模型与 80/20 自动划分的训练评估命令

## 适用场景

- 从超导领域论文中批量提取材料与临界温度数据
- 构建超导材料科学数据库的文献抽取环节
- 在 PDF 原文上查看材料与属性标注结果

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L14: The goal of this GROBID module is to identify, extract, and link materials with their properties from scientific li
> L26: The Extraction step is a Named Entities Recognition (NER) task and is performed using machine learning.
> L29: The Linking is a relation extraction (RE) tasks and is implemented via rule-based using the SpaCy library. The impl

## 星数曲线

```mermaid
xychart-beta
    title "lfoppiano/grobid-superconductors 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `b0ef5868b25c` · [字段定义](../../DATASET.md)*
