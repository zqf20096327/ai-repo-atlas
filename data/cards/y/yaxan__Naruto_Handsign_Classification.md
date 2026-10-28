# yaxan/Naruto_Handsign_Classification

⭐ 39 · Python · 推送 2026-10-13 · [GitHub](https://github.com/yaxan/Naruto_Handsign_Classification) · 个人维护

**识别火影忍者结印手势的迁移学习图像分类项目**

基于深度学习与计算机视觉的手势识别项目：用网络摄像头经 OpenCV 手工采集并增强数据，在 MobileNetV2、ResNet50、VGG16、InceptionV3 四种架构上做迁移学习训练，其中 VGG16 在静态测试集达到 93.60% 准确率，实时演示最低 83.33%；Dog 与 Serpent 两类识别稳定性较低。README 列出 Python 3.7.7、TensorFlow 2.8.0 等依赖版本，未给出安装或运行命令。作者自述此项目为其大学早期作品，并称如今 LLM 可轻易完成同类任务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 对 12 类火影结印手势做图像分类
- 四种 CNN 架构迁移学习对比，VGG16 静态测试准确率 93.60%
- OpenCV 网络摄像头采集数据并做翻转/旋转增强
- 支持网络摄像头实时分类演示

## 适用场景

- 想复现或学习迁移学习手势分类的学生与爱好者
- 用摄像头实时识别动漫风格结印手势做演示
- 比较常见 CNN 架构在小数据集上的表现

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: This is a project based on the anime Naruto by Masashi Kishimoto. In the show, the ninjas weave various hand-signs c
> L15: We experimented on MobileNetV2, ResNet50, VGG16, and InceptionV3 architectures due to their prominence in image cla

## 星数曲线

```mermaid
xychart-beta
    title "yaxan/Naruto_Handsign_Classification 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-28 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `aba0b8744b86` · [字段定义](../../DATASET.md)*
