# arbazsiddiqui/Ozan

⭐ 10 · Python · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/arbazsiddiqui/Ozan) · [官网](https://huggingface.co/arbazsiddiqui/Ozan-v1-12B) · 个人维护

**面向开发者的低 slop 长篇创作写作 12B 模型训练配方**

以 Mistral-Nemo-Instruct-2407 为基座的微调模型仓库，提供完整训练配方：QLoRA SFT（约 17k 策展的低 slop 样例）加 Gutenberg 公版书反 slop DPO，两阶段训练降低 LLM 高频套话与重复。权重、GGUF 量化与样例故事托管在 Hugging Face；repo 内含训练脚本（TRL）、数据清单、评测方法（EQ-Bench Creative Writing v3，slop/重复指标直接从生成文本计算）与复现步骤。训练在单张 NVIDIA A100 上完成；评测提示词经过 minhash 去污染。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- QLoRA SFT + Gutenberg 反 slop DPO 两阶段训练配方，含训练脚本与数据来源清单
- 以 EQ-Bench Creative Writing v3 直接从生成文本计算 slop 与重复指标
- 提供 Q4–Q8 四档 GGUF 量化与推荐采样参数（含 DRY 重复控制）
- 评测提示词对训练数据做 minhash 去污染

## 适用场景

- 复现或迁移这个长篇写作模型的训练流程
- 本地运行 GGUF 量化版生成长篇虚构作品
- 为微调项目参考 slop/重复评测与去污染方法

## 场景标签

`模型评测` `微调` `模型量化` · 领域:评测与运维

## 证据(README 行号)

> L3: **A 12B creative-writing model tuned to write long-form fiction that *doesn't sound like an LLM.***
> L9: This repo holds the training recipe. The weights, quants and sample stories live on Hugging Face:
> L129: Records are ChatML-native (`{"messages":[{role,content}], ...}`); `sft_instruct.py` formats them to Mistral `[INST


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `aee1388a5330` · [字段定义](../../DATASET.md)*
