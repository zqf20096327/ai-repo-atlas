# rustyneuron01/AI-Generated-Content-Detection

⭐ 90 · Python · MIT · 推送 2026-03-13 · [GitHub](https://github.com/rustyneuron01/AI-Generated-Content-Detection) · 个人维护

**多模态 AI 生成内容检测：图像/视频/音频真假分类的训练与评测工具**

面向内容真伪鉴别的训练与评测工具集：针对图像、视频、音频三种模态分别提供检测模型（图像用 DINOv3+LoRA，视频用 DINOv2 时序头或 ReStraV 轨迹几何特征，音频用 BreathNet），输出 real/fake 二分类 logits。统一基准套件 GASBench 在相同数据集与指标上运行所有模型，指标为 MCC 与 Brier 的加权几何均值以强调校准；使用公开数据集训练、隐藏 holdout 数据集评估泛化。模型以 safetensors 目录格式提交，支持 git clone 加 install.sh 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图像/视频/音频三模态独立检测模型，统一 safetensors 提交格式
- GASBench 统一基准：MCC+Brier 加权组合指标，强调概率校准
- LoRA 微调、LayerNorm-only 调优、ReStraV 冻结骨干+轨迹几何等泛化手段
- 公开/holdout 数据集分离设计以避免数据集记忆

## 适用场景

- 训练并评测图像/视频/音频的真伪分类模型
- 在自有检测模型上运行统一基准对比指标
- 做 AI 生成内容鉴别与媒体安全相关研究

## 场景标签

`模型评测` `微调` · 领域:评测与运维

## 证据(README 行号)

> L3: Multi-modal detection of real vs. AI-generated content across **image**, **video**, and **audio**. This repository c
> L7: The project trains and evaluates detection models that answer: *Is this image, video, or audio real (human-captured)
> L44: |**Audio**|BreathNet|Audio-specific model for real vs. synthetic speech/audio.|

## 星数曲线

```mermaid
xychart-beta
    title "rustyneuron01/AI-Generated-Content-Detection 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 88 --> 91
    line [89, 90, 90]
```

2026-10-18 89 → 2026-10-28 90（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e56fbad204bb` · [字段定义](../../DATASET.md)*
