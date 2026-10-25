# uav4geo/GeoDeep

⭐ 516 · Python · AGPL-3.0 · 推送 2026-05-13 · [GitHub](https://github.com/uav4geo/GeoDeep) · 组织维护

**对地理空间栅格做目标检测与语义分割的 Python 库**

轻量级 Python 库，读取 GeoTIFF 栅格，用预置或自训 ONNX 模型执行目标检测与语义分割，输出 GeoJSON 边界框/多边形或地理参考掩膜；仅依赖 rasterio 与 onnxruntime，可在 CPU 上运行，无需 GPU。预置 10 个检测模型（cars/trees/planes 等）与 2 个分割模型（buildings/roads），发布于 Hugging Face；提供 yolo2geodeep 命令将 YOLO 权重转换为可用模型，支持 YOLO 5-9 与 Retinanet。训练自有模型需 GPU 与较大内存，部分预置模型标注为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预置 10 个检测模型与 2 个分割模型（ONNX，发布于 Hugging Face）
- 仅依赖 rasterio 与 onnxruntime，可在 CPU 上运行推理
- 提供 CLI 与 Python API，输出 GeoJSON 边界框/多边形或地理参考掩膜
- yolo2geodeep 工具支持将 YOLO 5-9 与 Retinanet 权重转换接入

## 适用场景

- 对航拍/卫星正射影像批量检测车辆、树木、飞机等目标
- 从遥感影像提取建筑物轮廓或道路掩膜
- 将自己训练的 YOLO 检测模型转换后用于 GeoTIFF 推理

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: A fast, easy to use, lightweight Python library for AI object detection and semantic segmentation in geospatial rast
> L33: This will create a GeoJSON file with the bounding boxes, confidence scores and class labels of all cars detected in
> L41: Areas that correspond to buildings will be saved as a GeoJSON file containing the polygons that approximate the bui

## 星数曲线

```mermaid
xychart-beta
    title "uav4geo/GeoDeep 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 512 --> 515
    line [513, 514, 514]
```

2026-10-18 513 → 2026-10-25 514（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `7a3c1a25675b` · [字段定义](../../DATASET.md)*
