# BelalC/sign2text

⭐ 164 · Jupyter Notebook · 推送 2026-07-06 · [GitHub](https://github.com/BelalC/sign2text) · 个人维护

**实时识别 ASL 手语字母（A-Z）并转成文本的视觉模型项目**

基于迁移学习的美国手语（ASL）手指拼写字母识别系统：以 ImageNet 预训练网络（VGG16/ResNet50/MobileNet 等）做瓶颈特征提取，在其上训练自定义分类块，对 26 个字母分类。实时演示由 live_demo.py 完成：OpenCV 读取摄像头帧，裁剪 ROI、方垫、VGG 归一化后逐帧推理，置信度超 50% 时显示 top-3 预测。提供代码与权重、预处理后的 Massey 数据集子集，需 Python 3.10+ 与 TensorFlow 等依赖。2017 年 Data Science Retreat 作品集项目，作者声明欢迎协作。CPU 单帧约 250ms，GPU 性能提升明显。

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

- 迁移学习（VGG16/ResNet50/MobileNet 等）+ 自定义分类块识别 26 个 ASL 字母
- live_demo.py 实时摄像头识别，显示 top-3 预测，50% 置信度过滤低质量帧
- 提供预处理后的 Massey 数据集子集与训练脚本
- 瓶颈特征提取方式训练，基础模型仅需前向一次

## 适用场景

- 通过摄像头实时把 ASL 手指拼写字母转成文本
- 学习迁移学习与实时视觉分类的实现流程
- 作为手语识别方向的入门/作品集参考项目

## 场景标签

`目标检测` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L4: The project focuses on translating American Sign Language (ASL) fingerspelled alphabet (26 letters). I utilised tran
> L18: The live_demo.py script loads a pre-trained model (VGG16/ResNet50/MobileNet) with a custom classification block, an

## 星数曲线

```mermaid
xychart-beta
    title "BelalC/sign2text 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 163 --> 165
    line [164, 164]
```

2026-10-18 164 → 2026-10-22 164（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c108c4347d74` · [字段定义](../../DATASET.md)*
