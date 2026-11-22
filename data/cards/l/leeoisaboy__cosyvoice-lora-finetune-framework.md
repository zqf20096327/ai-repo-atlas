# leeoisaboy/cosyvoice-lora-finetune-framework

⭐ 14 · Python · 推送 2026-01-05 · [GitHub](https://github.com/leeoisaboy/cosyvoice-lora-finetune-framework) · [官网](https://www.bilibili.com/video/BV1Sti7B9ENN/) · 个人维护 · 中文 README

**CosyVoice LoRA 微调框架：少量音频定制音色实现无 Prompt 语音合成**

基于 CosyVoice 的 LoRA 微调框架，提供 LLM 与 Flow 模块联合训练流程：LLM 学习韵律节奏、Flow 学习音色特征，实现推理时无需参考音频的无 Prompt 语音合成。项目以调试纪实形式记录权重命名对齐、激活函数、位置编码 scale 参数三类 Loss 问题，以及语义泄漏的四关断路测试诊断方法与 LLM 过拟合阈值停止策略。附联合训练脚本、显存优化配置（8GB）与调试纪实视频。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM+Flow 联合训练，推理无需参考音频
- 四关断路测试定位语义泄漏根因
- 8GB 显存的联合训练优化配置
- LLM Loss 1.5-2.5 阈值停止防止过拟合

## 适用场景

- 用 10-50 条音频微调 CosyVoice 定制特定说话人音色
- 排查 CosyVoice 微调中 Loss 不下降与语义泄漏问题
- 低显存环境下进行 TTS 模型 LoRA 微调

## 场景标签

`语音合成` `微调` · 领域:内容生成

## 证据(README 行号)

> L50: **我的目标很简单**：用少量数据（10-50条音频，总共几分钟）微调 CosyVoice，让模型学会特定说话人的音色，用于"古诗吟诵"场景。
> L266: 这需要同时微调两个模块：
> L407: ### 联合训练（推荐）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `f8a30704390b` · [字段定义](../../DATASET.md)*
