# leeoisaboy/lora-cosyvoice123-chanting

⭐ 10 · Python · 推送 2026-06-18 · [GitHub](https://github.com/leeoisaboy/lora-cosyvoice123-chanting) · 个人维护 · 中文 README

**中文古诗词吟诵的 CosyVoice 1/2/3 LoRA 微调实验框架**

以同一份吟诵数据、同一套 LoRA 框架横向对比 CosyVoice 1/2/3 三代模型，把论文中的架构差异（VQ/FSQ/Flow/DiT-CFM）落实为可运行的训练、推理与诊断代码，按代际区分 LoRA 注入 pattern 与特征参数，并针对 Cosy3 提供 unistream-only 训练补丁。附吟诵专用客观评估公式（F0-DTW-RMSE、TCC、GDE、VRE/VDE 等）与试听样例。面向做语音合成微调与消融实验的研究者。CER/WER 指标需可靠 ASR 后端，无 ASR 时不伪造结果。

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

- 三代 CosyVoice 接入同一 LoRA 实验框架，逐代适配矩阵形状、特征参数与 LoRA 注入规则
- Cosy3 LLM unistream-only 训练补丁与安全 prompt 配对策略（完整 prompt audio + 匹配 prompt text）
- 吟诵专用客观评估公式：F0-DTW-RMSE、TCC、GDE、VRE/VDE、SS、DTW-LMD、NBE
- Ablation-LLM 与 Ablation-DiT 消融分组，拆分内容稳定性与声学风格迁移

## 适用场景

- 对比 CosyVoice 三代在同一吟诵数据上的微调效果
- 研究 LLM 侧与 DiT-CFM 侧 LoRA 消融差异
- 复现 CosyVoice 吟诵风格的训练与推理链路
- 为非朗读类语音风格设计客观评估指标

## 场景标签

`语音合成` `微调` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5:  面向中文古诗词吟诵的 CosyVoice 1/2/3 LoRA 微调实验框架
> L24: 本项目的价值在于：**同一份吟诵数据、同一套 LoRA 框架，横向比较 CosyVoice 1、CosyVoice 2、CosyVoice 3 三代，并把论文中的架构差异落实成可运行的训练、推理和诊断代码。**
> L34: |CosyVoice 1|`cosy1_weight/`|`FunAudioLLM/CosyVoice-300M`|第一代 300M 基座，项目中的 `Cosy1-LoRA` 在此基础上挂载 LLM/Flow LoRA|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `f8640339c8c3` · [字段定义](../../DATASET.md)*
