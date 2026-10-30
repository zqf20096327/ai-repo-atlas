# Thomasbehan/LesNet

⭐ 18 · Python · MPL-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/Thomasbehan/LesNet) · 个人维护

**开源深度学习皮肤病变分类工具，用于皮肤癌分诊研究**

基于深度学习的皮肤病变检测开源项目：以 EfficientNetV2-S 与 DINOv2 骨干构建三分诊模型（良性/可疑/恶性）加细粒度辅助诊断头，融合图像特征与患者元数据，输出经温度校准并由分布外/图像质量门控，不确定时拒判；提供 Pyramid(pserve) Web 应用、在线 Demo、模型下载脚本与 ISIC 数据下载器。训练数据来自 ISIC 档案，M-4s 版本基于 4 万图像样本训练。声明仅限研究/分诊用途，不用于临床诊断。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- EfficientNetV2-S 三分诊头（benign/suspicious/malignant）+ 细粒度诊断头
- DINOv2 系列变体（Small 165MB / Medium 435MB）符合 512MB 推理预算
- 温度校准 + OOD 门控 + 共形预测，不确定输入拒判
- 提供 ISIC 全档案（531,667 图像）断点续传下载器

## 适用场景

- 研究自动化皮肤病变分析方法
- 下载预训练模型在本地运行分诊推理
- 基于 ISIC 数据复现或扩展训练流程

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L9: > LesNet is an open-source project for deep learning-based skin cancer detection. It aims to create a reliable tool 
> L108: An EfficientNetV2-S backbone fuses image features with patient metadata (age/sex/site) into a
> L188: LesNet is not intended for clinical diagnosis or medical use. It is a research tool aimed at fostering development

## 星数曲线

```mermaid
xychart-beta
    title "Thomasbehan/LesNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a86e63f768a1` · [字段定义](../../DATASET.md)*
