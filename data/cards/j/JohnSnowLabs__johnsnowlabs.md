# JohnSnowLabs/johnsnowlabs

⭐ 78 · Python · NOASSERTION · 推送 2026-10-22 · [GitHub](https://github.com/JohnSnowLabs/johnsnowlabs) · [官网](https://nlp.johnsnowlabs.com) · 组织维护

**John Snow Labs 生态的统一 Python API 网关：一行代码加载 NLP 模型**

John Snow Labs 的入口库，提供统一 Python API 访问其 NLP 生态：一行代码加载 15,000+ 开源模型（250+ 语言），支持命名实体识别、问答、情感分类等推理，并可训练文本分类器。通过 nlp.install() 接入付费授权的 Healthcare/Legal/Finance NLP 模型（各 1,000+），附带可视化（NER、依存树、实体消解）与 Streamlit 交互界面。开源部分采用 Apache 2.0 许可，Spark NLP 为其底层之一。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一行代码加载 15,000+ 免费模型，覆盖 250+ 语言
- 支持 predict/fit/viz/viz_streamlit 的统一 API
- 凭 license key 接入 Healthcare/Legal/Finance NLP 付费模型
- 支持对字符串、NumPy、Pandas、Modin、Spark DataFrame 的预测

## 适用场景

- 在 Python 中快速加载并运行 NER、问答、情感分类等模型
- 医疗文本抽取 ICD-10-CM 编码与时序关系
- 训练自定义文本分类或 NER 模型并可视化结果

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: The John Snow Labs library provides a simple & unified Python API for delivering enterprise-grade natural language p
> L4: 1. 15,000+ free NLP models in 250+ languages in one line of code. Production-grade, Scalable, trainable, and 100% op
> L31: from johnsnowlabs import nlp
> L32: nlp.load('emotion').predict('Wow that was easy!')

## 星数曲线

```mermaid
xychart-beta
    title "JohnSnowLabs/johnsnowlabs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-25 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a8dc5322f46c` · [字段定义](../../DATASET.md)*
