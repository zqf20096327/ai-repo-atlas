# insight-platform/Savant

⭐ 863 · Python · Apache-2.0 · 推送 2026-09-23 · [GitHub](https://github.com/insight-platform/Savant) · [官网](https://savant-ai.io) · 组织维护

**面向开发者的实时视频分析与计算机视觉流水线框架**

构建于 Nvidia DeepStream 之上的开源高层框架，用于在数据中心与边缘设备上开发实时流式多媒体 AI 应用。流水线由声明式 YAML 块与 Python 函数组成，支持检测、分类、分割、跟踪及自定义前后处理。要求 Nvidia 硬件（Jetson 或 Turing/Ampere/Ada/Hopper/Blackwell GPU），流水线以 Docker 容器运行，集成 OpenTelemetry 与 Prometheus 监控，提供 Python Client SDK、多种源/汇适配器、Development Server 热重载工具，并支持 PyTorch、CuPy、OpenCV CUDA 集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 DeepStream 的声明式 YAML + Python 流水线构建
- 边缘（Jetson）与数据中心 GPU 同一代码运行
- 集成 OpenTelemetry/Prometheus 监控与 Python Client SDK
- 支持 PyTorch、CuPy GPU 后处理与 OpenCV CUDA 操作

## 适用场景

- 搭建实时视频目标检测/跟踪/分割流水线
- 构建边缘-数据中心混合的视频分析应用
- 接入 RTSP/USB/Kinesis 等多源视频并输出结构化结果

## 场景标签

`图像视频处理` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L11: Savant is an open-source, high-level framework for building real-time, streaming, highly efficient multimedia AI
> L15: Savant is built on DeepStream and provides a high-level abstraction layer for building inference pipelines. It is

## 星数曲线

```mermaid
xychart-beta
    title "insight-platform/Savant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 862 --> 864
    line [863, 863]
```

2026-10-18 863 → 2026-10-23 863（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `6f85c6dbd35b` · [字段定义](../../DATASET.md)*
