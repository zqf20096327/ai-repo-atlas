# abelchrispin5-glitch/Keras-Forge-CNN-Studio

⭐ 56 · HTML · 推送 2026-10-28 · [GitHub](https://github.com/abelchrispin5-glitch/Keras-Forge-CNN-Studio) · 组织维护 · 中文 README

**跨语言 CNN 图像分类器构建工作台（Python Keras + C#）**

面向图像分类 CNN 流水线开发的跨语言工作台：以声明式 blueprint 项目文件为单一来源，Python 侧（Forge）将其编译为 Keras 模型并执行训练，C# 侧（Bridge）提供强类型包装、异步训练会话管理与 .NET 接口，配合 Studio 网页界面展示训练遥测与指标。支持数据增强编排、迁移学习预设、混合精度、多格式导出（HDF5/SavedModel/ONNX）与插件扩展，界面支持含简体中文在内的五种语言。README 仅提供 Download 入口，未给出具体安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明式 blueprint 编译为 Keras 模型，Python 训练与 C# 推理两侧同步生成
- C# Bridge 提供强类型描述符、异步训练会话与 SignalR 指标流
- 一键导出 HDF5 / SavedModel / ONNX 及 JSON 描述符
- 每轮指标带时间戳存储，可对比多次训练运行

## 适用场景

- 用 Keras 构建 CNN 分类器并在 .NET 服务中调用
- 让数据科学家与应用开发者在同一模型定义上协作
- 管理可复现的超参数实验与模型导出

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L16: **VisionForge Studio** is a workspace for assembling convolutional neural network (CNN) pipelines for image classif
> L71: 2. **Forge Layer (Python)** — translates blueprints into Keras model definitions, runs training, and emits artifact
> L72: 3. **Bridge Layer (C#)** — hosts the Python runtime or connects to a training daemon, exposes strongly-typed wrappe

## 星数曲线

```mermaid
xychart-beta
    title "abelchrispin5-glitch/Keras-Forge-CNN-Studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-29 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `bfb877ff165a` · [字段定义](../../DATASET.md)*
