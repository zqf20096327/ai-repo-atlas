# OortCloudGroup/VLStream-Cloud

⭐ 10 · Java · MIT · 推送 2026-11-20 · [GitHub](https://github.com/OortCloudGroup/VLStream-Cloud) · [官网](https://vlstream.oortcloudsmart.com:2443/bus/vls-ui/login) · 组织维护 · 中文 README

**企业视频物联网平台：设备接入、智能分析与算法全生命周期管理**

基于 Spring Boot 多模块后端与 Vue 3 控制台的开源视频物联网平台，功能覆盖设备注册与 PTZ 控制、多协议播放（GB28181/ONVIF/RTSP）、智能分析任务与事件治理、算法仓库与训练任务、模型经 MQTT 下发至 Hi3519DV500 设备部署，并集成 Flowable 工作流、Sa-Token RBAC 权限、对象存储与 XXL-Job 调度。训练采用单物理 GPU 独占队列的 Docker 容器调度。面向化工、水务、工地、社区等企业视频场景，提供在线演示环境与 Compose 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 设备管理：注册、分组、健康监测、PTZ 控制与流发现，支持 GB28181/ONVIF/RTSP
- 算法生命周期：算法仓库、训练任务、标注、模型管理与 Hi3519DV500 OM 转换下发
- 单节点 GPU 训练调度器：单卡独占队列，Docker 容器运行训练任务
- 企业级配套：Flowable 工作流、Sa-Token RBAC、MinIO 对象存储与告警监控

## 适用场景

- 接入并统一管理园区/工地/厂区的摄像头与视频流
- 对视频流运行智能分析算法并治理告警事件
- 训练检测模型并部署到 Hi3519DV500 边缘设备
- 搭建带权限与审批流程的企业视频运维平台

## 场景标签

`工作流自动化` `模型训练` · 领域:效率与自动化

## 证据(README 行号)

> L34: VLStream Cloud is an open-source Video IoT platform for device and stream
> L53: |Intelligent Analysis|Analysis requests, real-time task monitoring, result management, and event governance|
> L54: |Algorithm Lifecycle|Algorithm warehouse, training tasks, annotations, model management, Hi3519DV500 OM conversion,

## 星数曲线

```mermaid
xychart-beta
    title "OortCloudGroup/VLStream-Cloud 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-22 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `6981ba30f55b` · [字段定义](../../DATASET.md)*
