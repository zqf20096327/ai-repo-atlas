# OpenNyAI/Opennyai

⭐ 103 · Python · MIT · 推送 2026-04-01 · [GitHub](https://github.com/OpenNyAI/Opennyai) · 组织维护

**印度法律文书 NLP 库：NER、修辞角色与摘要三模型管线**

OpenNyAI 开发的 Python 库，面向印度法院判决文本提供自然语言预处理管线，统一封装三个预训练模型：命名实体识别（NER）、基于句子修辞角色的判决结构化、抽取式摘要。主要用于在用户自定义判决文本上运行这些预训练模型，模型训练细节见各独立仓库。通过 uv 或 pip 安装，要求 Python >= 3.13，GPU 使用需自行安装对应 CUDA 版本的 Cupy，并提供 Colab 推理笔记本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一访问 3 个预训练模型：NER、修辞角色判决结构化、抽取式摘要
- Pipeline API 对自定义判决文本批量推理
- 支持 GPU（通过 Cupy/CUDA）与 CPU 运行
- 提供 Colab 推理笔记本

## 适用场景

- 对印度法院判决做命名实体识别
- 按修辞角色结构化判决文本并生成抽取式摘要
- 在自己的判决语料上批量运行 OpenNyAI 预训练模型

## 场景标签

 · 领域:法律 NLP

## 证据(README 行号)

> L10: This library provides unified access to the following 3 pre-trained AI models developed by OpenNyAI which focus on
> L21: This library is mainly for running the pretrained models on your custom input judgments text. For more details abou

## 星数曲线

```mermaid
xychart-beta
    title "OpenNyAI/Opennyai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 102 --> 104
    line [103, 103]
```

2026-10-18 103 → 2026-10-26 103（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `a3f9456a928b` · [字段定义](../../DATASET.md)*
