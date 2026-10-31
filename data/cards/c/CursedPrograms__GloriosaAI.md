# CursedPrograms/GloriosaAI

⭐ 18 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/CursedPrograms/GloriosaAI) · [官网](https://cursedprograms.github.io/gloriosa-ai-pr/) · 个人维护

**用 GAN 训练与生成 AI 艺术图像的 Python 工具集**

基于 TensorFlow 的生成对抗网络（GAN）Python 代码库，用于训练模型并生成 AI 艺术图像。以脚本集合形式提供：main.py 菜单入口，trainer.py 训练（可调 Epochs、Batch Size、潜空间维度、学习率调度、随机种子等超参数），modelout.py 从已训练模型输出图像，video_encoder.py 编码视频，image-processor.py 准备训练图像（需 128x128 RGB 格式数据集）。支持 GPU（TensorRT/CUDA）与 CPU 安装路径，附 PyInstaller 编译与 requirements.txt 依赖清单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GAN 训练器支持 Epochs/Batch Size/潜空间维度/学习率调度等超参数配置
- 从已训练模型输出图像（modelout.py）与视频编码（video_encoder.py）
- 图像预处理脚本要求 128x128 RGB 格式训练数据
- 提供 GPU（tensorrt/CUDA）与 CPU 两种安装路径

## 适用场景

- 用自己的图像数据集训练 GAN 生成 AI 艺术图像
- 把训练好的模型用于批量图像生成
- 将生成模型输出编码为视频

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L34: - **trainer.py:** Runs GloriosaAI trainer
> L35: - **modelout.py:** Output images from trained models with GloriosaAI

## 星数曲线

```mermaid
xychart-beta
    title "CursedPrograms/GloriosaAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `1bc78be492af` · [字段定义](../../DATASET.md)*
