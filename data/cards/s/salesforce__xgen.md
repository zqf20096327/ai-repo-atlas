# salesforce/xgen

⭐ 728 · Python · Apache-2.0 · 推送 2026-06-02 · [GitHub](https://github.com/salesforce/xgen) · 组织维护

**Salesforce 开源的 7B 长序列 LLM 系列模型（4K/8K 上下文）**

Salesforce AI Research 发布的 XGen 模型族（7B 参数）官方研究版本，配套论文《Long Sequence Modeling with XGen: A 7B LLM Trained on 8K Input Sequence Length》。提供三个变体：4K 序列长度的基础版、8K 基础版和 8K 指令微调版，模型卡片发布于 HuggingFace Hub。分词使用 OpenAI Tiktoken 包，可通过 transformers 的 AutoModelForCausalLM 加载并作为自回归采样器使用。声明仅供研究用途，未针对下游任务做安全性与公平性评估。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7B 参数、最长 8K 输入序列长度的模型族
- 三个变体：4K-Base、8K-Base、8K 指令微调版
- 模型权重发布于 HuggingFace Hub，transformers 可直接加载
- 使用 OpenAI Tiktoken 进行分词

## 适用场景

- 研究长上下文（8K）语言建模能力
- 需要开源 7B 基座或指令模型的实验
- 学术论文复现与引用

## 场景标签

 · 领域:自然语言处理/大语言模型

## 证据(README 行号)

> L3: Official research release for the family of **XGen** models (`7B`) by Salesforce AI Research:
> L5: *Title*: Long Sequence Modeling with XGen: A 7B LLM Trained on 8K Input Sequence Length
> L17: * XGen-7B-4K-Base with support for 4K sequence length.

## 星数曲线

```mermaid
xychart-beta
    title "salesforce/xgen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 727 --> 729
    line [728, 728]
```

2026-10-18 728 → 2026-10-24 728（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `c27676c83424` · [字段定义](../../DATASET.md)*
