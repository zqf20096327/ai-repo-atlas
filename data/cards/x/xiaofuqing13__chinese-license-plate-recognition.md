# xiaofuqing13/chinese-license-plate-recognition

⭐ 14 · Python · 推送 2026-03-01 · [GitHub](https://github.com/xiaofuqing13/chinese-license-plate-recognition) · 个人维护 · 中文 README

**面向中文车牌的两阶段检测识别系统：YOLOv5定位+PlateNet识别**

针对国内蓝牌、绿牌（新能源）、黄牌、双层与摩托车牌等类型的两阶段车牌识别系统：先用 YOLOv5 检测并矫正车牌区域，再用自定义 CNN PlateNet 逐字符识别（含中文省份简称），支持双层车牌自动拆分合并。输入支持图片、视频与摄像头实时流，推理后端支持 PyTorch、ONNX、OpenVINO，并提供 CCPD 数据集预处理脚本与训练入口。以 Python 源码形式提供，pip 安装依赖后运行脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLOv5 车牌定位 + PlateNet 字符识别的两阶段流程
- 支持蓝牌/绿牌/双层/摩托车牌及中文省份简称
- 图片/视频/摄像头三种输入模式
- PyTorch/ONNX/OpenVINO 多推理后端与模型导出

## 适用场景

- 停车场出入口车牌自动识别
- 道路卡口抓拍与车辆出入管理
- 车牌 OCR 技术研究与学习

## 场景标签

`OCR` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L10: - **方案**：分两步走——先用 YOLOv5 检测图片中的车牌位置并矫正，再用专门训练的字符识别模型逐字识别车牌号码
> L16: - **字符识别**：自定义 PlateNet 识别车牌字符（含中文省份简称）

## 星数曲线

```mermaid
xychart-beta
    title "xiaofuqing13/chinese-license-plate-recognition 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `85ed1895780b` · [字段定义](../../DATASET.md)*
