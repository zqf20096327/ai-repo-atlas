# zai-org/Kaleido

⭐ 149 · Python · 推送 2026-03-02 · [GitHub](https://github.com/zai-org/Kaleido) · 组织维护 · 中文 README

**多主体参考图像驱动的视频生成模型（14B）**

由 Zai-org（智谱）联合合肥工业大学、清华大学开源的多主体参考视频生成模型 Kaleido-14B-S2V：从多张参考图像（人物、物体、场景如试穿）与长文本提示生成视频。开放训练与推理代码：推理基于 Diffusers，需 Python 3.10-3.12、pip 安装依赖并从 Hugging Face 下载权重（集成 Wan VAE 与 T5）；支持多 GPU 与序列并行加速。训练基于 CogVideoX 策略，提供 DeepSpeed 与 FSDP2 分布式实现。建议先用 GLM-4.5 等大模型优化提示词。数据管线尚未发布。

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

- 多主体参考图像（人物/物体/试穿等场景）可控视频合成
- 训练与推理代码均开源，附 14B checkpoint（Hugging Face）
- 多 GPU 推理与序列并行加速，FSDP2/DeepSpeed 训练实现

## 适用场景

- 用多张参考图像生成含指定主体的高保真视频
- 复现或二次训练多主体视频生成模型
- 虚拟试穿等以参考图控制视频内容的任务

## 场景标签

 · 领域:视频生成/生成式模型

## 证据(README 行号)

> L3:  KALEIDO: OPEN-SOURCED MULTI-SUBJECT REFERENCE VIDEO GENERATION MODEL
> L23: * 2025.10.22: 🔥 We propose **Kaleido**, a novel multi-subject reference video generation model. Both the **training
> L68: python sample_video.py --base configs/video_model/dit_crossattn_14B_wanvae.yaml configs/sampling sample_wanvae_conc

## 星数曲线

```mermaid
xychart-beta
    title "zai-org/Kaleido 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 148 --> 150
    line [149, 149]
```

2026-10-18 149 → 2026-10-24 149（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `109cdfc60416` · [字段定义](../../DATASET.md)*
