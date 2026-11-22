# thourihan/DeepfakeDetection

⭐ 10 · Python · MIT · 推送 2026-09-15 · [GitHub](https://github.com/thourihan/DeepfakeDetection) · 个人维护

**用 CNN/ViT 轻量模型检测深度伪造图像的项目**

基于 timm 集成 EfficientNet、FasterViT 与 EfficientFormerV2-S1 三种骨干，对图像做 deepfake/real 二分类，输出置信度。提供训练与批量评测脚本（orchestrator.py 经 YAML 配置驱动），带 Grad-CAM 热力图可视化与混淆矩阵、ROC 曲线输出，另有 Gradio 网页界面上传单张图像查看预测。面向研究者与开发者，附研究论文链接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- timm 集成三种骨干（EfficientNet/FasterViT/EfficientFormerV2-S1）
- Grad-CAM 热力图解释模型判定区域
- YAML 配置驱动的训练/推理/网页 UI 三个入口
- 支持多分类 ImageFolder 数据集

## 适用场景

- 训练自己的 deepfake 检测模型并对比多种骨干
- 对单张图像做真伪检测并查看热力图解释
- 批量评测并输出混淆矩阵与 ROC 曲线

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L11: This project detects deepfake images using modern CNN/ViT-family backbones. We use EfficientNet, FasterViT, and Eff
> L17: - **Gradio Interface:** Simple web UI for uploading images and viewing model predictions.

## 星数曲线

```mermaid
xychart-beta
    title "thourihan/DeepfakeDetection 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-22"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-20 10 → 2026-11-22 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `ae6cafcdf3bc` · [字段定义](../../DATASET.md)*
