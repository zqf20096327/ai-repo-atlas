# gia-uh/cecilia

⭐ 30 · TeX · MIT · 推送 2026-09-22 · [GitHub](https://github.com/gia-uh/cecilia) · [官网](https://cecilia.uhgia.org/) · 组织维护

**面向古巴西班牙语的 2B 持续预训练语言模型**

Cecilia 2B v0.1 是基于 Salamandra 2B 架构、在约 10 亿 token 古巴书面语料（报纸、百科、法律、文学、歌词等）上持续预训练的 20 亿参数模型，由哈瓦那大学 GIA-UH 与阿利坎特大学 GPLSI 合作开发。当前版本未量化、未做指令微调，定位为语言建模而非指令跟随任务。支持文本生成、情感分析、命名实体识别、古巴西班牙语理解等 NLP 任务，通过 Hugging Face Transformers 加载，兼容 vLLM 与 LM Studio，以 CC BY-SA 4.0 许可发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 2B 参数模型，自 Salamandra 2B 在约 10 亿 token 古巴文本上持续预训练 2 个 epoch
- 未量化、未指令微调，定位语言建模任务；量化与指令微调版本将后续发布
- 通过 Hugging Face Transformers 加载，兼容 vLLM 推理与 LM Studio 本地部署
- CC BY-SA 4.0 许可，允许研究与商业使用

## 适用场景

- 对古巴西班牙语文本做生成、补全与情感分析
- 识别古巴特有实体的命名实体识别
- 面向古巴语言学现象与文化研究的应用
- 通过 LM Studio 或 vLLM 在本地运行与部署

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L1: Cecilia is a family of language models continual pretrained specifically on Cuban written text, capturing the lingui
> L39: - Text generation and completion.
> L6: This repository contains **Cecilia 2B v0.1**, a 2 billion parameter model continual pretrained on Cuban written text

## 星数曲线

```mermaid
xychart-beta
    title "gia-uh/cecilia 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-29 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a33fdddbebeb` · [字段定义](../../DATASET.md)*
