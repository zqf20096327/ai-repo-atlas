# AMALIA-LLM/AMALIA

⭐ 77 · 推送 2026-06-30 · [GitHub](https://github.com/AMALIA-LLM/AMALIA) · 组织维护

**面向欧洲葡萄牙语的完全开源 LLM 项目（模型+数据+评测）**

AMALIA 是针对欧洲葡萄牙语（pt-PT）的开源大语言模型项目，覆盖数据处理、预训练、后训练与评测全流程：发布 9B 语言模型 AMALIA-9B 与 9B 视觉语言模型 AMALIA-VL（托管于 HuggingFace），并开源基于 Megatron-LM 的预训练代码、SFT/DPO 后训练管线、datatrove 数据处理组件及 ALBA、P3B3、PHEB 等评测基准。模型可通过 vLLM 部署，用 curl、requests 或 openai 库以 OpenAI 兼容 API 调用；推荐 Python >=3.12 环境。多篇论文发表/预印于 arXiv、PROPOR、ACL、LREC。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AMALIA-9B 语言模型与 AMALIA-VL 视觉语言模型，HuggingFace 开放权重
- 开源 Megatron-LM 预训练、SFT/DPO 后训练与数据处理管线
- 多个欧洲葡萄牙语评测基准（ALBA、P3B3、PHEB）
- vLLM 部署，OpenAI 兼容 API 调用

## 适用场景

- 欧洲葡萄牙语场景下的文本与图文生成应用
- 研究低资源语言变体的针对性训练与评测方法
- 复用其数据处理与训练管线构建其他语言模型

## 场景标签

`模型训练` `微调` `模型评测` `多模态` · 领域:评测与运维

## 证据(README 行号)

> L3: **A Fully Open Large Language Model for European Portuguese**
> L16: To support the development of high-quality pt-PT language models, AMALIA provides an end-to-end open ecosystem span
> L40: |AMALIA-9B|9B|Language|🤗 Link|

## 星数曲线

```mermaid
xychart-beta
    title "AMALIA-LLM/AMALIA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 76 --> 78
    line [77, 77]
```

2026-10-18 77 → 2026-10-31 77（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `898793ad231f` · [字段定义](../../DATASET.md)*
