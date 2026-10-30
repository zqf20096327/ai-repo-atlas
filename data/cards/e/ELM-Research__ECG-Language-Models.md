# ELM-Research/ECG-Language-Models

⭐ 20 · Python · MIT · 推送 2026-09-08 · [GitHub](https://github.com/ELM-Research/ECG-Language-Models) · 组织维护

**面向研究者的 ECG-语言模型训练与评测框架**

ECG-语言模型（ELM）的训练与评测研究框架：支持 Llava 式投影架构、encoder-free 与 ECG-Byte 符号化等多种 ELM 变体，可接入 HuggingFace 上的 Llama/Gemma/Qwen 系列 LLM 与 MERL/ST-Mem 等 ECG 编码器及 Siglip2/ViT/CLIP 视觉编码器。提供 pretrain/SFT/RL 三阶段训练流程与评测、对话脚本，通过 HuggingFace 数据集统一加载 ECG-QA 等数据，支持多卡分布式训练。需先用 ECG-Preprocess 准备数据；BPE 表示需编译 Rust tokenizer。仓库自述状态为 Beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 Llava 式、encoder-free（base/patch/conv_elf）与 ECG-Byte 多类 ELM 架构
- pretrain/SFT/RL（SAPO）三阶段训练，统一 main_trainer.py 入口
- 统一加载 HuggingFace ECG 数据集（ECG-QA、ECG-Instruct、ECG-Bench 等）
- 提供评测脚本与加载单个 .npy 的对话脚本

## 适用场景

- 训练和评测自己的 ECG-语言模型
- 比较不同 ECG 表示（signal/symbolic/rgb）与编码器组合
- 基于 ECG 做问答与研究实验

## 场景标签

`多模态` `模型训练` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L6: A research framework for finetuning and evaluating ECG-language models (ELMs). Supports multiple architectures, trai
> L116: ### Llava
> L184: We support three training phases via the `--train_phase` flag. Each phase reuses the same `main_trainer.py` entry 

## 星数曲线

```mermaid
xychart-beta
    title "ELM-Research/ECG-Language-Models 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e67aabad45d0` · [字段定义](../../DATASET.md)*
