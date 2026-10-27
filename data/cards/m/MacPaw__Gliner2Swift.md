# MacPaw/Gliner2Swift

⭐ 43 · Swift · Apache-2.0 · 推送 2026-09-14 · [GitHub](https://github.com/MacPaw/Gliner2Swift) · 组织维护

**GLiNER2 的 Swift/MLX 移植：Apple 设备上信息抽取**

MacPaw 出品的 GLiNER2 统一模式信息抽取框架的 Swift/MLX 实现，运行于 Apple Silicon 的 Metal GPU。支持命名实体识别、文本分类、结构化数据抽取（JSON schema 与字段描述语法）与关系抽取，长文档自动分块并映射回原文。支持 int8 编码器量化（约省 40% 内存）、加载 HuggingFace 模型权重（仅 safetensors）并在加载时合并 LoRA 适配器。局限：训练循环未实现，当前仅支持 deberta-v3-base 模型变体。以 Swift Package Manager 分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- NER/文本分类/结构化抽取/关系抽取四类任务
- MLX 原生 Apple Silicon 支持（Metal GPU）
- int8 编码器量化约减 40% 内存
- LoRA 适配器加载时合并，与 Python 结果数值一致

## 适用场景

- 在 macOS/iOS 应用中做本地命名实体识别
- 用 JSON schema 从文本抽取结构化数据
- 长文档抽取实体且不依赖云端模型

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L11: Swift/MLX implementation of GLiNER2 - a unified schema-based information extraction framework.
> L17: - Named Entity Recognition (NER)

## 星数曲线

```mermaid
xychart-beta
    title "MacPaw/Gliner2Swift 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-27 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d6cf1e9085d0` · [字段定义](../../DATASET.md)*
