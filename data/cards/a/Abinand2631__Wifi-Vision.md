# Abinand2631/Wifi-Vision

⭐ 22 · Python · 推送 2026-07-17 · [GitHub](https://github.com/Abinand2631/Wifi-Vision) · 个人维护

**基于 ESP32 Wi-Fi CSI 的人体姿态与活动识别系统**

使用 3 块 ESP32（1 发射 2 接收）采集 Wi-Fi 信道状态信息（CSI），通过自建的 TEDNet 模型（1D CNN + Transformer 编码器）实时识别站立、坐下、行走、躺卧四类姿态，无需摄像头与穿戴设备。流程含数据采集（配合摄像头标注）、特征提取、模型训练（需 NVIDIA GPU）与 Streamlit 实时推理面板。训练数据为自采的 21,600 帧，属 B.Tech 毕业设计项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ESP32 CSI 无摄像头人体姿态识别，支持 4 类活动分类
- TEDNet：1D CNN + Transformer 编码器 + 动力学门控
- Streamlit 实时推理面板与独立推理脚本
- 自采 21,600 帧数据集训练

## 适用场景

- 病房跌倒检测与无摄像头活动监测
- 智能家居中的存在与姿态感知
- 无视频监控的周界入侵检测

## 场景标签

 · 领域:物联网/感知计算

## 证据(README 行号)

> L3: **Device-free, camera-free human pose estimation and activity recognition using Wi-Fi CSI and deep learning.**
> L16: Wi-Fi Vision detects and classifies human posture in real time by analyzing how a person's body disturbs Wi-Fi radi

## 星数曲线

```mermaid
xychart-beta
    title "Abinand2631/Wifi-Vision 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `801513111cb6` · [字段定义](../../DATASET.md)*
