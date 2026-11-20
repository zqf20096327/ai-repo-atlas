# SirryChen/SpeechMedAssist

⭐ 10 · Python · Apache-2.0 · 推送 2026-04-23 · [GitHub](https://github.com/SirryChen/SpeechMedAssist) · 组织维护 · 中文 README

**开源医疗语音大模型：语音多轮问诊咨询**

SpeechMedAssist 是面向语音多轮医疗问诊的 SpeechLM，可原生分析症状、主动追问并给出诊疗建议，接受 ACL 2026 论文录用。仓库开放训练、推理与评估全流程：数据构建流水线（Filter/Rewrite/Get Patient Info/Synthesize）四阶段、三阶段 torchrun 训练脚本、终端交互式 demo，以及单轮问答（CMB/CMExam/MedSafety）与多轮对话（LLM 虚拟病人、可配语音输入输出）评估代码。模型基于 LLaMA-Omni2 构建，权重与数据集可从 Hugging Face 下载。

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

- 语音端到端多轮医疗问诊模型，权重、数据、训练/推理/评估代码全部开源
- 四阶段数据构建流水线，并提供可直接下载的 SpeechMedDataset
- 三阶段训练脚本（torchrun 多 GPU）与终端交互 demo
- 评估覆盖单轮问答、多轮对话（LLM 虚拟病人）与野生场景

## 适用场景

- 搭建语音驱动的医疗问诊对话模型
- 复现论文训练与评估流程
- 用其数据集与评估脚本测试其他医疗对话模型

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L5: SpeechMedAssist is a SpeechLM designed for speech-based multi-turn medical consultation, which can natively analyze 
> L93: ### 4.Train

## 星数曲线

```mermaid
xychart-beta
    title "SirryChen/SpeechMedAssist 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `76d471f32710` · [字段定义](../../DATASET.md)*
