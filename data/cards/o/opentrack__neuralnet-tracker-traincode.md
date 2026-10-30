# opentrack/neuralnet-tracker-traincode

⭐ 43 · Jupyter Notebook · NOASSERTION · 推送 2026-09-28 · [GitHub](https://github.com/opentrack/neuralnet-tracker-traincode) · 组织维护

**OpenTrack 头部姿态追踪神经网络的训练与评估代码**

为 OpenTrack 的 NeuralNet 追踪插件训练神经网络：包含定位网络（从摄像头画面中找出人脸并生成边界框）与姿态估计网络（分析裁剪后的人脸图像）。提供数据集预处理脚本（300W-LP、AFLW2000-3D、Biwi、Face Synthetics 等）、训练脚本、ONNX 导出与基准评估流程，标签以 HDF5 格式存储。对应论文 OpNet（数据增强用于头部姿态估计），paper 分支为论文快照，其 checkpoint 与当前代码不兼容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 定位网络+姿态估计网络两阶段架构，支持普通摄像头头部追踪
- 提供 AFLW2000-3D 与 Biwi 基准的预处理和评估脚本
- ONNX 导出脚本可将模型部署到 OpenTrack Neuralnet 插件
- 附带的 3D 标注 WFLW/LaPa 大姿态扩展数据集（Google Drive）

## 适用场景

- 复现 OpenTrack 头部追踪插件的神经网络模型
- 在 AFLW2000-3D/Biwi 基准上评估头部姿态估计模型
- 导出 ONNX 模型并部署到 OpenTrack 使用

## 场景标签

`人脸识别` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L8: This repository contains the code to train the neural nets for the NeuralNet tracker plugin of Opentrack. It allows 
> L12: The tracker plugin is based on deep learning, i.e. neural network models optimized using data to perform their task

## 星数曲线

```mermaid
xychart-beta
    title "opentrack/neuralnet-tracker-traincode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-30 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f567bd45a378` · [字段定义](../../DATASET.md)*
