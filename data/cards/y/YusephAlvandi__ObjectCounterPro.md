# YusephAlvandi/ObjectCounterPro

⭐ 15 · Python · 推送 2026-06-04 · [GitHub](https://github.com/YusephAlvandi/ObjectCounterPro) · 个人维护

**离线检测并统计图片中物体数量的桌面工具**

基于 Python、OpenCV 与 CustomTkinter 构建的桌面应用：通过 OpenCV DNN 加载预训练 YOLOv3 模型（80 个 COCO 类别），对单张图片或整个文件夹进行物体检测、标注与计数，结果在实时预览中展示并可保存。提供置信度滑杆调节检测灵敏度。全部流程在本地 CPU 运行，无云端调用；使用前需 pip 安装依赖并自行下载放置 yolov3 权重等模型文件。

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

- 单图模式与文件夹批量模式，支持结果保存
- 置信度滑杆控制检测灵敏度（0.2–0.8）
- YOLOv3 经 OpenCV DNN 加载，纯本地 CPU 运行，无 API 调用
- 覆盖 80 个 COCO 物体类别

## 适用场景

- 离线统计单张图片中某类物体的数量
- 批量处理整个文件夹的图片并输出检测结果
- 在无 GPU、不联网的环境下做物体检测

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: An AI-powered object detection tool. Uses YOLOv3 (a deep neural network model trained on 80 object classes). Appropr
> L15: A pre-trained model (YOLOv3) is loaded via OpenCV DNN. The model divides the whole image into a grid and predicts b

## 星数曲线

```mermaid
xychart-beta
    title "YusephAlvandi/ObjectCounterPro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `820e1869e509` · [字段定义](../../DATASET.md)*
