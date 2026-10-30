# xN1ckuz/Crosswalks-Detection-using-YOLO

⭐ 45 · Jupyter Notebook · GPL-3.0 · 推送 2026-02-08 · [GitHub](https://github.com/xN1ckuz/Crosswalks-Detection-using-YOLO) · 组织维护

**YOLO 人行横道检测项目（巴西利卡塔大学课程）**

大学计算机视觉课程项目：基于 Ultralytics YOLO 框架，在自采集照片数据集（1046 训练/224 验证/224 测试）上重训练 YOLOv8m（300 epochs），检测行人过街横道；自行实现基于 OpenCV 的边界框合并算法，并自写 IoU 测试算法（结果 0.63）。代码以 Jupyter Notebook 形式在 Google Colab 上运行，训练受 Colab GPU 显存限制无法使用更大模型。测试集 Precision 0.96、Recall 0.93。GPL-3.0 许可，YOLO 模型权利归 Ultralytics。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自建 1470+ 张标注数据集并经 Roboflow 增强，重训练 YOLOv8m
- 自实现 OpenCV 边界框合并算法与 IoU 测试算法
- 标注含停止标线负样本以减少误检
- v1.2.0 用 YOLOv5m，v1.4.0 更新为 YOLOv8m

## 适用场景

- 检测街景图像中的人行横道
- 作为课程项目参考 YOLO 训练与评估流程
- 为视障人士出行安全应用提供横道检测组件

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: We introduce a supervised method for detecting pedestrian crosswalks with DCNNs and Python. The project is based on 
> L7: We have created a detector for pedestrian crossings, as more and more often we hear about road accidents with the in

## 星数曲线

```mermaid
xychart-beta
    title "xN1ckuz/Crosswalks-Detection-using-YOLO 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-30 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8ed32eaf59f3` · [字段定义](../../DATASET.md)*
