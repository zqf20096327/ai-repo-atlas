# robertklee/COCO-Human-Pose

⭐ 50 · Python · MIT · 推送 2026-10-05 · [GitHub](https://github.com/robertklee/COCO-Human-Pose) · 个人维护

**从零训练堆叠沙漏网络做 COCO 单人人体姿态估计**

在 COCO 2017 Keypoints 数据集上从零训练 stacked hourglass 网络的源码仓库，预测单帧 RGB 图像上最多 17 个人体关键点。采用热图法与运动学骨架模型，训练时过滤少于 5 个关键点标注、按检测框裁剪转单人样本。部署在 Streamlit Cloud 的在线应用支持上传照片，自动用 OpenCV DNN 检测并裁剪人物后推理；限制：多人时仅标注最居中者，对严重遮挡/重叠人物效果受限。训练需下载约 30GB 数据集、45GB 磁盘空间。

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

- stacked hourglass 网络从零训练，预测 17 个 2D 人体关键点
- 在线部署应用：自动检测裁剪人物并输出关键点与热图
- 训练数据过滤 0-4 关键点标注，按包围盒裁剪复用多人图像
- 可视化逐层热图展示网络逐步精化的关键点判别

## 适用场景

- 我想在 COCO 数据集上从零训练一个人体姿态估计模型
- 上传照片在线试用人体的关键点检测效果
- 学习沙漏网络的热图输出与中间监督机制

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repository contains the source code for training a deep neural network to perform human pose estimation from sc
> L119: Our group created a stacked hourglass network that was trained on the Common Objects in Context (COCO) dataset. Ou
> L127: HPE systems can be categorized into 2D vs 3D and single-person vs multi-person. To improve the feasibility of our 

## 星数曲线

```mermaid
xychart-beta
    title "robertklee/COCO-Human-Pose 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-25 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `11e5994744db` · [字段定义](../../DATASET.md)*
