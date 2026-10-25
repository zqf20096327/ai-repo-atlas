# Correr-Zhou/OmniShow

⭐ 474 · Python · Apache-2.0 · 推送 2026-07-29 · [GitHub](https://github.com/Correr-Zhou/OmniShow) · [官网](https://correr-zhou.github.io/OmniShow/) · 组织维护 · 中文 README

**人-物交互视频生成模型：统一文本/参考图/音频/姿态多模态条件**

OmniShow 是 ICML 2026 论文的官方代码库，面向人-物交互视频生成（HOIVG）：单一模型支持 R2V/RA2V/RP2V/RAP2V 四类任务，以文本、人物与物体参考图、音频、姿态序列为条件生成视频，基于 Wan2.1 DiT 骨干。机制包括统一通道级条件注入、门控局部上下文注意力实现音画同步、先分后合的训练策略。提供训练与推理脚本、示例数据集及 HOIVG-Bench 基准（135 样本）与评测代码；因内部政策限制未放出训练好的 checkpoint，用户需自行下载骨干权重并训练。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单模型统一 R2V/RA2V/RP2V/RAP2V 四类生成任务
- 基于 Wan2.1-I2V-14B DiT 骨干，提供训练与推理代码
- 附带 HOIVG-Bench 基准（135 样本）及评测代码
- CSV 驱动的自定义数据集格式，支持 480p/720p

## 适用场景

- 按人物与物体参考图、音频、姿态生成定制视频
- 复现论文方法或在自己的 HOIVG 数据上训练模型
- 用 HOIVG-Bench 评测多模态条件下的视频生成模型

## 场景标签

`视频生成` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3:  OmniShow: Unifying Multimodal Conditions for Human-Object Interaction Video Generation
> L35: We propose **OmniShow**, a video generation model that unifies text, reference image, audio, and pose conditions fo

## 星数曲线

```mermaid
xychart-beta
    title "Correr-Zhou/OmniShow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 473 --> 475
    line [474, 474]
```

2026-10-18 474 → 2026-10-25 474（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `3b438bd2fe2e` · [字段定义](../../DATASET.md)*
