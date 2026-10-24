# epimore/gmv

⭐ 210 · Rust · MIT · 推送 2026-10-09 · [GitHub](https://github.com/epimore/gmv) · 个人维护 · 中文 README

**Rust 编写的视音频监控基础设施：接入、流媒体与视觉分析**

GMV 是 Rust 构建的端到端视音频基础设施，分四个模块：Guard（Web 管理、调度、鉴权、HTTP API/MQTT）、Session（GB28181 设备接入、点播回放、PTZ）、Stream（RTP/H.264/H.265 接收，输出 HTTP-FLV/fMP4/HLS/MP4）、Vision（视频转结构化信息）。Guard/Session/Stream 大部分已实现，Vision 部分（ONNX/YOLO/OCR/推理后端、模型管理、训练闭环）处于规划状态。支持边缘/中心/云端部署。面向视频监控与流媒体集成的企业场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- GB28181-2016/2022 设备接入与 SIP 信令（点播、回放、PTZ、语音广播）
- 输出 HTTP-FLV / HTTP-fMP4 / HLS / LL-HLS / MP4 多种流格式
- Control Plane / Work Plane 分离架构，节点注册、调度与健康监控
- Vision 规划支持 ONNX、YOLO/OCR/Pose，ONNX Runtime/OpenVINO/TensorRT/RKNN 后端

## 适用场景

- 接入 GB28181 摄像头并分发多格式直播/回放流
- 构建边缘到云端的视频监控平台
- 后续接入视频结构化分析（识别/跟踪/事件）

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: GMV 是一个使用 **Rust** 构建的智能视音频基础设施，从设备接入、媒体处理、流媒体分发、视觉分析、数据媒体展示，到灵活部署 **边缘端、中心端、云端**，以完成端到端交付。
> L23: - **Vision**：视觉感知、AI 推理、跟踪与事件分析
> L127: 负责将视频和图片转化为可计算、可理解、可持续演进的结构化视觉信息。

## 星数曲线

```mermaid
xychart-beta
    title "epimore/gmv 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 209 --> 211
    line [210, 210]
```

2026-10-18 210 → 2026-10-24 210（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `9848cfee760e` · [字段定义](../../DATASET.md)*
