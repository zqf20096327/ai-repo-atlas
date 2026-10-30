# Dalageo/paperclip-inspection

⭐ 18 · Jupyter Notebook · AGPL-3.0 · 推送 2026-04-23 · [GitHub](https://github.com/Dalageo/paperclip-inspection) · 个人维护

**深度学习+计算机视觉的回形针缺陷检测与测量项目**

基于 YOLOv11-OBB（Ultralytics 预训练模型微调）与 OpenCV 的回形针质量检测流水线：先通过 ArUco 标记（50x50mm）建立像素到厘米的尺度换算，再检测并分类回形针，对正常回形针提取尺寸归类（三档）与角度估计，实时在视频画面上显示结果。附带 80 张图像（247 个回形针，127 正常/120 缺陷）数据集与 23 秒测试视频，以 Jupyter Notebook 形式提供复现流程，需要 Python 3.12.7、PyTorch 2.5.1、CUDA 12.4 环境。换用自有相机复现需同规格回形针，否则可用提供视频测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLOv11-OBB 旋转框检测，处理任意朝向的回形针
- ArUco 标记实现像素到厘米的物理测量换算
- 正常回形针的尺寸三档分类与角度估计，实时视频输出
- 含 80 图 247 个标注回形针的数据集与测试视频

## 适用场景

- 制造质检场景的缺陷检测参考实现
- 学习旋转框目标检测与物理测量的结合
- 复用流水线改造为其他物体的自动检测系统

## 场景标签

`目标检测` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L15: In this project, a combination of object detection and computer vision methods was utilized to inspect paper clips 
> L19: The pipeline for this project begins by detecting the Aruco marker to establish the scale for real-world measuremen

## 星数曲线

```mermaid
xychart-beta
    title "Dalageo/paperclip-inspection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `fbb9c3f480c3` · [字段定义](../../DATASET.md)*
