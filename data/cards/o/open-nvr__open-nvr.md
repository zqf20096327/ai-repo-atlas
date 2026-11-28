# open-nvr/open-nvr

⭐ 222 · Python · AGPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/open-nvr/open-nvr) · [官网](https://opennvr.org) · 组织维护

**自托管摄像头 NVR 平台：本地运行任意 AI 模型并审计推理**

面向不能把摄像头交给厂商的组织与个人的开源视频基础设施：以 ONVIF/RTSP 接入摄像头，提供录像、实时查看与 WebRTC 流；通过一个开放契约把任意 AI 模型接入为能力（检测、车牌、人脸、姿态、场景描述、开放词汇搜索、语音等），其上提供 14 个一键安装的应用与 App/Adapter 两个 Apache-2.0 SDK。部署仅需 Docker 与 start.sh 脚本；内置默认拒绝的离线模式与本地模型策略、模型权重 SHA-256 指纹与追加写审计日志，支持气隙部署与双网卡隔离的摄像头网络。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过开放契约接入任意模型，适配器可热替换并做指纹追踪
- 默认拒绝的离线模式（DEPLOYMENT_MODE=offline / AI_SOVEREIGNTY=local_only）与出口白名单代理
- 每个模型登记权重 SHA-256 指纹，相关 ID 从告警追溯到具体权重
- 分层检测：Tier-0 低帧率扫描子码流，按需唤醒重型模型

## 适用场景

- 在自有硬件上对摄像头画面做目标检测/车牌识别而不经云
- 政府、医疗等需要气隙部署与可审计推理的场所
- 通过 App Catalog 一键安装入侵、徘徊、占位等应用
- 用 SDK 为自有模型编写适配器接入平台

## 场景标签

`目标检测` `人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L7: OpenNVR is open-source video infrastructure for organisations and people who cannot hand their cameras to a vendor. 
> L115: |🧠|**An AI platform for cameras**|Any model behind a REST or WebSocket endpoint becomes a capability through a pub

## 星数曲线

```mermaid
xychart-beta
    title "open-nvr/open-nvr 星数(近 22 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-19", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 176 --> 226
    line [180, 182, 183, 184, 186, 188, 192, 180, 198, 199, 201, 204, 205, 206, 208, 209, 211, 214, 215, 218, 220, 222]
```

2026-10-26 180 → 2026-11-28 222（+42）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `f2788bd88c4a` · [字段定义](../../DATASET.md)*
