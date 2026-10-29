# nosterdream/hard-hat-detection

⭐ 18 · Python · Apache-2.0 · 推送 2026-09-06 · [GitHub](https://github.com/nosterdream/hard-hat-detection) · 个人维护

**检测图像/视频中人员是否佩戴安全帽的 YOLOv8 模型**

基于 YOLOv8 的安全帽检测项目：对图像和视频中的人员进行识别，判断是否佩戴安全帽，输出带边界框的标注结果——佩戴者框为绿色、未佩戴者为红色。以 Python 代码形式提供，核心类 HardhatTracker 支持 detect_frame/detect_frames 推理与视频帧间插值，另有 PersonTracker 用于人员检测。提供从 Roboflow 下载数据集并用 ultralytics 训练自定义模型的流程，README 提及基于 YOLO11 的新版本项目。要求 Python 3.11、Ultralytics、OpenCV、Torch 2.3.0+cu121 等依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLOv8 检测人员安全帽佩戴情况，绿/红边界框区分佩戴状态
- 支持图像与视频输入，视频模式提供检测结果插值处理
- 提供 Roboflow 数据集下载与 YOLOv8 模型训练流程

## 适用场景

- 工地监控视频中检查人员是否佩戴安全帽
- 对图片批量生成安全帽佩戴标注结果
- 在自有数据集上重新训练安全帽检测模型

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L9: This project focuses on detecting hard hats on individuals in images and videos. Leveraging the power of the YOLOv8 
> L80: hardhat_detection = hardhat_tracker.detect_frame(input_picture_path) # Detects hard hats on the image

## 星数曲线

```mermaid
xychart-beta
    title "nosterdream/hard-hat-detection 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `120362ebedd6` · [字段定义](../../DATASET.md)*
