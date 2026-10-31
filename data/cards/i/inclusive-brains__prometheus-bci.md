# inclusive-brains/prometheus-bci

⭐ 14 · Python · 推送 2026-06-03 · [GitHub](https://github.com/inclusive-brains/prometheus-bci) · 组织维护

**面向辅助神经科技的多模态 BCI 平台：EEG/PPG/ECG/摄像数据实时采集分析**

基于 Timeflux 构建的多模态数据采集与分析平台，读取 Emotiv、OpenBCI、BITalino、EmotiBit 等设备及摄像头数据，进行滤波与特征提取，计算压力、注意力、认知负荷等指标，支持运动想象与眨眼检测训练、面部表情识别（MediaPipe + DeepFace）及外骨骼/机械臂控制。项目源于帮助残障人士传递奥运火炬的场景。提供 Makefile 安装、Docker 模拟模式（无需硬件）与 Web 实时监控界面；硬件直通 Docker 模式仅限 Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 EEG/PPG/ECG/摄像头多设备接入（Emotiv、OpenBCI、BITalino、EmotiBit 等）
- EEG 频段、HRV、压力/注意力/认知负荷等实时指标计算
- 运动想象与眨眼检测训练范式，含 Riemannian 几何分类
- 集成 EEG 与面部信号的外骨骼/机械臂控制

## 适用场景

- 搭建脑机接口研究与认知实验（N-back、运动想象训练）
- 辅助技术场景下用面部表情或脑电控制机械臂
- 实时监控多模态生理信号并计算认知指标

## 场景标签

 · 领域:神经科学/脑机接口

## 证据(README 行号)

> L11: Prometheus BCI is an advanced platform for the collection and analysis of multimodal data, designed to support appl
> L54:  *Multimodal metrics, N-back cognitive tasks, mental command classification (Riemannian geometry, CSP and non-linea
> L258: |Camera|Any webcam (via MediaPipe + DeepFace)|

## 星数曲线

```mermaid
xychart-beta
    title "inclusive-brains/prometheus-bci 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `c45b727beef4` · [字段定义](../../DATASET.md)*
