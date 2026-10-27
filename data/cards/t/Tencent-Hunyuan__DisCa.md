# Tencent-Hunyuan/DisCa

⭐ 26 · Python · 推送 2026-04-15 · [GitHub](https://github.com/Tencent-Hunyuan/DisCa) · 组织维护 · 中文 README

**给视频扩散模型研究者的推理加速方法：可蒸馏兼容的可学习特征缓存**

CVPR 2026 论文 DisCa 的官方代码，由上海交大 EPIC Lab 与腾讯混元合作发布。面向视频扩散 Transformer 的推理加速：用轻量可学习预测器（小于 DiT 总量 4%）替代免训练启发式特征缓存，多步复用缓存实现快速推理；并提出保守的 Restricted MeanFlow 蒸馏方案。实验基于 HunyuanVideo-1.0（T2V）与 HunyuanVideo-1.5（I2V），提供推理 shell 脚本，环境遵循官方 HunyuanVideo 配置。README 声明仍存在帧间抖动与压缩率提升空间。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 轻量可学习预测器替代免训练特征缓存启发式（小于 DiT 总量 4%）
- Restricted MeanFlow 保守蒸馏方案
- 提供 HunyuanVideo-1.0 T2V 与 HunyuanVideo-1.5 I2V 两组推理脚本

## 适用场景

- 复现论文中的视频扩散模型加速实验
- 在 HunyuanVideo 上运行加速后的文生视频/图生视频推理
- 基于 Predictor 训练代码研究进一步压缩

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L1: # *DisCa*: Accelerating Video Diffusion Transformers with *Dis*tillation-Compatible Learnable Feature *Ca*ching
> L23: > ** Abstract:** *While diffusion models have achieved great success in the field of video generation, this progres
> L25: This paper novelly introduces a **distillation-compatible learnable** feature caching mechanism for the first time.

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-Hunyuan/DisCa 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-27 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b3bed4db4fcf` · [字段定义](../../DATASET.md)*
