# securade/hub

⭐ 293 · Python · AGPL-3.0 · 推送 2026-10-10 · [GitHub](https://github.com/securade/hub) · [官网](https://securadeai.com) · 组织维护

**接驳现有 CCTV 的边缘计算机视觉平台，做安全事件检测**

面向工业安全场景的生成式 AI 边缘视觉平台：连接 D-link、Tapo、TP-Link、Axis、HikVision 等摄像头，通过自然语言描述零样本训练/微调模型并部署到边缘设备，实现 PPE 合规检测（安全帽/背心/口罩）、近距离告警、禁区监控、人脸遮挡保护、Telegram 实时通知与分析面板。支持插件系统扩展图像处理能力（内置 YOLOv7 目标检测、OpenCV 边缘检测）。安装为 git clone + pip，CPU 可跑；GPU/Jetson 路径需自装 Jetpack、CUDA、cuDNN、Torch 等，要求至少 8GB 内存的 Jetson 设备。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零样本学习：用自然语言描述训练模型，无需人工标注
- PPE 检测、近距离告警、禁区监控等实时安全事件识别
- 兼容 D-link/Tapo/TP-Link/Axis/HikVision 多品牌摄像头
- 插件系统支持扩展检测能力，本地边缘处理不依赖云端

## 适用场景

- 工地/工厂接入现有 CCTV 做工人安全帽背心等合规检测
- 监控工人与机械车辆的安全距离并实时告警
- 配置禁区并在闯入时通过 Telegram 收到通知

## 场景标签

`目标检测` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L3: Securade.ai HUB is a generative AI based edge platform for computer vision that connects to existing CCTV cameras an
> L4: It uses natural language text and generative AI to automatically train and fine-tune state-of-the-art computer visio

## 星数曲线

```mermaid
xychart-beta
    title "securade/hub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 292 --> 294
    line [293, 293]
```

2026-10-18 293 → 2026-10-23 293（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6899cd6a8b25` · [字段定义](../../DATASET.md)*
