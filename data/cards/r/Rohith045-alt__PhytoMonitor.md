# Rohith045-alt/PhytoMonitor

⭐ 22 · JavaScript · 推送 2026-09-27 · [GitHub](https://github.com/Rohith045-alt/PhytoMonitor) · [官网](https://rohith045-alt.github.io/PhytoMonitor/) · 个人维护

**上传叶片照片即可预测植物病害的全栈 Web 应用**

Phyto 是一个面向终端用户的全栈 Web 应用：用户上传植物叶片图片，系统通过训练好的 CNN 模型（TensorFlow/Keras）返回预测病害名称与置信度。架构为 React/Vite 前端、Node.js/Express 后端，后端通过 child_process 调用 Python 进程加载 .h5 模型完成推理，结果以 JSON 返回。需自行准备模型文件（backend/ml_models/my_plant_disease_model.h5）且文件不能为空；README 声明项目仅供教育用途。

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

- 上传叶片图片并返回病害类别与置信度分数
- Node.js 后端经 child_process 桥接 Python TensorFlow 模型
- 提供 POST /api/v1/plants/analyze 接口（multipart/form-data）
- React + Vite 前端与 Express 后端分离运行

## 适用场景

- 上传叶片照片快速查看可能的病害类型
- 作为植物病害预测的演示或教学项目
- 通过 API 接口测试模型预测结果

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: Phyto is a full‑stack web application that detects plant diseases from leaf images using a deep learning model. User
> L8: - Detect plant diseases using a trained CNN model
> L20: 4. Python loads TensorFlow model and predicts disease.

## 星数曲线

```mermaid
xychart-beta
    title "Rohith045-alt/PhytoMonitor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `8a6bdaa1a7b8` · [字段定义](../../DATASET.md)*
