# collabdoor/road-anomaly-detection

⭐ 25 · Jupyter Notebook · Apache-2.0 · 推送 2026-01-19 · [GitHub](https://github.com/collabdoor/road-anomaly-detection) · [官网](https://road-anomaly-detection.streamlit.app/) · 组织维护

**用自训练 YOLOv8 模型检测路面裂缝、坑洼与颠簸**

道路异常检测项目：基于自定义数据集从零训练 YOLOv8m 模型（120 轮、约 27.8 小时），可检测裂缝、严重裂缝、坑洼、减速带及车辆行人等 7 类目标，测试集整体 mAP@0.5 为 0.745，单张推理约 12 ms；另引入基于 CRDDC2022 数据集的预训练 YOLOv8s 作为第二模型，可双模型并行检测。提供 Streamlit 演示应用（支持图片、视频与摄像头实时检测、置信度阈值调节），Flask 应用仍在开发中。本地运行需参照仓库根目录的 setup 说明文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自训练 YOLOv8m 检测裂缝、坑洼、减速带等 7 类目标，测试 mAP@0.5 为 0.745
- 双模型架构：可选 Model 1、Model 2 或同时使用，各自独立置信度阈值
- Streamlit 应用支持上传图片、视频与摄像头实时检测
- 含数据集构建文档与混淆矩阵、PR 曲线等评估可视化

## 适用场景

- 上传行车视频或接摄像头检测路面裂缝与坑洼
- 对比两个 YOLOv8 模型在道路损伤检测上的表现
- 了解自定义道路异常数据集的构建与训练流程

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: Our Road Anomaly Detection project. We've been working on using computer vision, specifically YOLOv8 models, to auto
> L33: * **Model Architecture:** YOLOv8m

## 星数曲线

```mermaid
xychart-beta
    title "collabdoor/road-anomaly-detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `734bca89838d` · [字段定义](../../DATASET.md)*
