# mbzuai-oryx/LLaVA-pp

⭐ 843 · Python · 推送 2026-09-05 · [GitHub](https://github.com/mbzuai-oryx/LLaVA-pp) · 组织维护

**为 LLaVA 1.5 接入 Phi-3 与 LLaMA-3 的多模态模型训练代码库**

MBZUAI Oryx 团队发布的视觉语言模型扩展工作：将 LLaVA 1.5 的语言底座替换为 Phi-3 Mini Instruct 3.8B 与 LLaMA-3 Instruct 8B，提供预训练（LCS-558K）与微调（LLaVA-Instruct-665K，含 LoRA、全量微调、S2 微调）脚本与模型权重。使用方式为 git clone 后复制模型文件进 LLaVA 代码库并运行 shell 脚本训练；Hugging Face 页面发布模型，另有在线 Demo 与 Google Colab。主要面向多模态大模型研究者复现与训练。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 Phi-3-V 与 LLaMA-3-V 两套预训练/LoRA/全量微调权重
- 基于 LLaVA-Instruct-665K 数据的 LoRA 与 S2 微调训练脚本
- Hugging Face Spaces 在线 Demo 与 Google Colab 会话

## 适用场景

- 复现 LLaVA++ 的多模态模型预训练与微调流程
- 下载已发布的 Phi-3-V / LLaMA-3-V 权重做视觉对话推理
- 在多模态学术基准上评测与对比指令跟随能力

## 场景标签

`多模态` `模型训练` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L23: This repository enhances the capabilities of the LLaVA 1.5 model, incorporating latest LLMs released this weak🔥, Ph
> L37: |LLaVA-Phi-3-mini-4k-instruct-pretrain|Hugging Face|Pretrained on LCS-558K.|
> L44: |LLaVA-Meta-Llama-3-8B-Instruct-pretrain|Hugging Face|Pretrained on LCS-558K.|

## 星数曲线

```mermaid
xychart-beta
    title "mbzuai-oryx/LLaVA-pp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 842 --> 844
    line [843, 843]
```

2026-10-18 843 → 2026-10-26 843（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `516aee65a8e6` · [字段定义](../../DATASET.md)*
