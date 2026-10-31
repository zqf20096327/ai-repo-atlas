# Chaganti-Reddy/Tennis-Analysis-YOLOV8

⭐ 21 · Jupyter Notebook · MIT · 推送 2026-04-07 · [GitHub](https://github.com/Chaganti-Reddy/Tennis-Analysis-YOLOV8) · 个人维护

**用 YOLO 与 CNN 分析网球视频：检测球员与球并测速计数**

对输入网球视频进行分析的 Python 项目：使用 YOLO v8 检测球员，微调后的 YOLO 检测网球，CNN 提取球场关键点，在此基础上测量球员速度、击球速度并统计击球次数，结果视频保存到 output_videos 目录。面向球员表现分析、教练反馈与裁判判罚辅助场景。安装方式为克隆源码仓库，按 README 列出的 python3.8、ultralytics、pytorch、pandas、numpy、opencv 依赖清单配置后运行 main.py。数据集来自 Roboflow。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLO v8 球员检测与微调 YOLO 网球检测
- CNN 提取球场关键点
- 球员速度、击球速度测量与击球计数

## 适用场景

- 分析网球比赛视频量化球员表现
- 教练依据测速与击球数据给出反馈
- 为裁判判罚提供辅助参考

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3:  This project analyzes Tennis players in a video to measure their speed, ball shot speed and number of shots. This p
> L13: - **Player Detection**: Detects players in the video using YOLO Models.
> L41: - YOLO v8 for player detection

## 星数曲线

```mermaid
xychart-beta
    title "Chaganti-Reddy/Tennis-Analysis-YOLOV8 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e04826ed9014` · [字段定义](../../DATASET.md)*
