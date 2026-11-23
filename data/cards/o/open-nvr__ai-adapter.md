# open-nvr/ai-adapter

⭐ 10 · Python · AGPL-3.0 · 推送 2026-11-17 · [GitHub](https://github.com/open-nvr/ai-adapter) · [官网](https://opennvr.org) · 组织维护

**让任意 AI 模型接入 OpenNVR 监控系统的可插拔推理适配层**

OpenNVR 的模型侧集成层：定义 AI Adapter Contract v1 线协议（六个 HTTP 端点加一个 WebSocket），任何实现该协议的模型服务即可注册为 NVR 检测器。仓库包含 PyPI 发布的 Apache-2.0 SDK（约三十行 Python 即可编写适配器）和九个以独立 Docker 镜像发布的参考适配器（YOLOv8、BLIP、InsightFace、Whisper、Piper、ByteTrack 等）。中间件统一提供关联 ID 审计链、模型权重 sha256 指纹漂移检测、local_only 主权策略拒绝声明网络出口的适配器、按摄像头公平排队与 Prometheus 指标。权限采用先声明后审批的 fail-close 模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI Adapter Contract v1：六个 HTTP 端点加 WebSocket 的统一线协议
- SDK 三个类即可编写适配器，发布于 PyPI（Apache-2.0）
- 权限声明/审批生命周期、权重指纹漂移检测与端到端审计
- 九个参考适配器以独立 Docker 镜像发布于 GHCR

## 适用场景

- 给自托管视频监控接入目标检测、人脸识别、车牌识别等模型
- 在气隙/受监管环境中运行本地模型并保留审计证据
- 将自研模型封装为可热插拔的检测器供 NVR 调用

## 场景标签

`目标检测` `人脸识别` `语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L9: The pluggable inference layer for OpenNVR™. Drop any model behind an HTTP or WebSocket endpoint and it becomes a fir
> L22: OpenNVR is the offline-first NVR underneath; this repo is the layer that lets *any* AI model become one of its dete
> L45: The repo is two things in one. The `opennvr_adapter_sdk/` directory is the small Apache-2.0 SDK published to PyPI —


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `6820af1aed9f` · [字段定义](../../DATASET.md)*
