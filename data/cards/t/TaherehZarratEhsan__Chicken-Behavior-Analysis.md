# TaherehZarratEhsan/Chicken-Behavior-Analysis

⭐ — · [GitHub]() · 组织维护

**用计算机视觉检测跟踪鸡只并分析行为的深度学习框架**

面向拥挤禽舍环境的鸡只行为分析框架，由两名成员开发并获 2022 年 ICCKE 计算机视觉工业竞赛二等奖。流程为三段：用 YOLOv4 训练鸡只检测模型（数据集与标注以 YOLO 格式随仓库提供）；基于质心计算为每只鸡分配唯一 ID 并生成跟踪视频；基于轨迹评估行为，输出聚集异常、不活跃（疑似病鸡）检测与距离测量结果。以 Jupyter Notebook（检测与跟踪两个文件）形式提供，需自行调整目录路径并保存训练模型。Apache 2.0 许可，附 arXiv 论文可引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLOv4 鸡只检测，支持自有数据集（LabelImg 标注）
- 质心跟踪：为每只鸡分配唯一 ID 并生成跟踪视频
- 基于轨迹的行为分析：聚集异常、不活跃/疑似病鸡检测、距离测量

## 适用场景

- 密集禽舍环境下检测并跟踪个体鸡只
- 发现鸡群聚集异常或不活跃的疑似病鸡
- 基于跟踪轨迹测量鸡只间距离与行为评估

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L10: For chicken detection, train the YOLOv4 network using the dataset provided in the 'img' and 'Annotation' folders, f
> L14: In the 'Broiler_Tracking.ipynb' file, the saved model is used to track chickens through centroid computations, assi

## 星数曲线

```mermaid
xychart-beta
    title "TaherehZarratEhsan/Chicken-Behavior-Analysis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a86ffbe2096a` · [字段定义](../../DATASET.md)*
