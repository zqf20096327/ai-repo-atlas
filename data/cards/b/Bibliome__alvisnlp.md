# Bibliome/alvisnlp

⭐ 19 · Java · Apache-2.0 · 推送 2026-08-17 · [GitHub](https://github.com/Bibliome/alvisnlp) · [官网](https://bibliome.github.io/alvisnlp/) · 组织维护

**可配置的 NLP 批处理流水线引擎，用于文本文档语义标注**

AlvisNLP 是法国 Inra Bibliome 团队维护的可配置 NLP 批处理流水线：对文本做句切分、分词、命名实体识别、术语分析、语义类型标注与关系抽取，并依赖术语库/本体等资源适配领域；附带基于机器学习的（半）自动资源获取工具。新组件可集成进流水线。构建需 Unix（或参考 WINDOWS.md）+ Java >= 8 + Maven，git clone 后 mvn 编译，运行 install.sh 安装命令行界面并配置主机默认参数。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 集成分句、分词、命名实体识别、术语分析、语义类型与关系抽取的流水线
- 依赖术语库/本体资源适配应用领域，含 ML 工具半自动获取资源
- 新组件可集成进流水线
- 提供命令行界面与主机级默认参数/选项配置

## 适用场景

- 对文本语料批量执行语义标注与关系抽取
- 利用术语库和本体做领域适配的 NLP 处理
- 构建可组合的 NLP 处理工作流

## 场景标签

 · 领域:自然语言处理/语料处理

## 证据(README 行号)

> L3: AlvisNLP is a configurable NLP batch processing pipeline. It annotates text documents for the semantic annotation of
> L5: AlvisNLP is held by the Bibliome group at Inra Jouy-en-Josas, France

## 星数曲线

```mermaid
xychart-beta
    title "Bibliome/alvisnlp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `d131a2270ac2` · [字段定义](../../DATASET.md)*
