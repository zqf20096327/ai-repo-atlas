# Jellman86/YetAnother-WhosAtMyFeeder

⭐ 60 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/Jellman86/YetAnother-WhosAtMyFeeder) · 个人维护

**给家庭观鸟者：用本地模型识别 Frigate 摄像头中的鸟类**

面向 Frigate NVR 用户的鸟类识别应用：读取 Frigate 事件，用本地 TensorFlow Lite 类模型（默认 RoPE ViT-B14）在 CPU、Intel GPU/NPU 或 NVIDIA GPU 上分类鸟种，保存照片与到访历史，可匹配 BirdNET-Go 鸣叫声记录，并提供可分享的只读视图。以 Docker Compose 单体容器部署，需要 Frigate 开启鸟类检测与 MQTT、一个消息代理；树莓派仅有尽力而为的 ARM64 指南且未经维护者实机验证。模型兼容性验证只证明可运行并与 CPU 基线一致，不衡量物种准确率。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地模型识别鸟种，支持 CPU/Intel GPU/NPU/NVIDIA GPU
- 保存照片、到访历史并可匹配 BirdNET-Go 鸣叫记录
- 手动修正物种、数鸟、标注收藏与留存控制
- 可分享的只读访客视图与隐私边界设置

## 适用场景

- 自动记录喂鸟器摄像头前的鸟种与到访历史
- 复核识别证据并手动纠正物种标注
- 向家人朋友分享只读观鸟看板

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L10: YA-WAMF identifies birds in Frigate NVR events using local models.
> L22: - **Identify locally:** choose a model and validate it on your CPU, Intel GPU/NPU or NVIDIA GPU.

## 星数曲线

```mermaid
xychart-beta
    title "Jellman86/YetAnother-WhosAtMyFeeder 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 58 --> 61
    line [59, 60, 60]
```

2026-10-18 59 → 2026-10-24 60（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c22f76bb7f29` · [字段定义](../../DATASET.md)*
