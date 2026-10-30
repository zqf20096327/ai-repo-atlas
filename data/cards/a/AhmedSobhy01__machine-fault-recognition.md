# AhmedSobhy01/machine-fault-recognition

⭐ 16 · Python · MIT · 推送 2026-05-08 · [GitHub](https://github.com/AhmedSobhy01/machine-fault-recognition) · 个人维护

**音频机器故障分类模型：从录音判断设备正常或故障**

基于 PyTorch 的轻量 CNN（SmallCNNFactored，0.24M 参数），对三种工业机器（M1/M2/M3）的录音做 6 类监督分类（机器类型×健康状态），用于预测性维护场景的声学状态监测。特征采用 PCEN + log-mel；针对多 section 录音结构做聚类发现与 section 不相交划分以避免泄漏；训练时使用 Frequency-MixStyle 与辅助因式分解头。提供从特征缓存、划分、训练到推理的脚本化管线，CPU 推理为每条几十毫秒量级，推理支持 Docker 与 Python 两种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 类音频分类：3 种机器 × 正常/异常
- 0.24M 参数 CNN，CPU 推理约几十毫秒/条
- PCEN log-mel 特征 + section 不相交划分防泄漏
- Docker 镜像与脚本化管线（特征缓存→划分→训练→推理）

## 适用场景

- 工厂设备旁录音判断机器是否故障，辅助预测性维护
- 研究者复现 DCASE Task 2 风格的机器状态监测实验
- 在边缘设备上部署轻量声学故障检测

## 场景标签

 · 领域:工业状态监测/音频机器学习

## 证据(README 行号)

> L3: > Audio-based classification of machine health states across three machine types - a lightweight CNN that hears whet
> L21: **Task.** A supervised **6-way classification** over `{machine type} × {health state}`: three industrial machines (

## 星数曲线

```mermaid
xychart-beta
    title "AhmedSobhy01/machine-fault-recognition 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `90175e89b459` · [字段定义](../../DATASET.md)*
