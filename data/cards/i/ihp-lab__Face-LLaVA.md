# ihp-lab/Face-LLaVA

⭐ 19 · Python · NOASSERTION · 推送 2026-03-19 · [GitHub](https://github.com/ihp-lab/Face-LLaVA) · [官网](https://face-llava.github.io/) · 组织维护

**面向人脸的多模态大模型：表情与属性识别、年龄估计等**

WACV 2026 论文 Face-LLaVA 的官方代码库：基于指令微调的多模态大语言模型，支持人脸表情识别、面部属性检测、动作单元检测、年龄估计与深度伪造检测等任务，并可生成自然语言描述用于推理。方法上构建了 FaceInstruct-1M 人脸指令数据集，并提出基于人脸区域引导交叉注意力的视觉编码器。模型权重与数据集发布在 Hugging Face。安装需 Python 3.10、PyTorch 与 CUDA 环境，提供训练脚本与推理代码，推理前需用 crop_face.py 裁剪人脸。代码基于 USC Research license。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持表情识别、属性检测、动作单元检测、年龄估计等多任务
- FaceInstruct-1M 人脸指令微调数据集（已发布于 Hugging Face）
- 人脸区域引导交叉注意力的视觉编码器
- 提供训练脚本、推理代码与模型权重

## 适用场景

- 对人脸图像/视频做表情与属性分析
- 复现论文实验或用自建数据训练人脸 MLLM
- 获取带自然语言推理的人脸理解输出

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L26: This is the official codebase of the **WACV 2026 Round 1** Early Accept paper (6.4% acceptance rate) - Face-LLaVA: 
> L30: The human face plays a central role in social communication, necessitating the use of performant computer vision to

## 星数曲线

```mermaid
xychart-beta
    title "ihp-lab/Face-LLaVA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d25ebec8a3cd` · [字段定义](../../DATASET.md)*
