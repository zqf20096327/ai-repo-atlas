# DASDAE/das-anomaly

⭐ 31 · Python · NOASSERTION · 推送 2025-12-10 · [GitHub](https://github.com/DASDAE/das-anomaly) · 组织维护

**分布式声波传感（DAS）数据的无监督异常检测 Python 包**

面向分布式声波传感（DAS）数据的开源 Python 包，基于卷积自编码器做无监督异常检测。工作流：用 DASCore 创建数据 spool，生成 RGB 功率谱密度（PSD）图像，在无异常样本上训练自编码器，以 MSE 与密度分数阈值检测异常并输出时间戳与结果文件。支持 MPI 多进程分布式读数据与绘图，训练可在 CPU 或 GPU 上进行（GPU 需自行安装 GPU 版 TensorFlow）。由 Colorado School of Mines 团队开发，README 声明仍在开发中、需谨慎使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 卷积自编码器对 PSD 图像做无监督异常检测
- 基于 DASCore 读取 DAS 数据并生成空间 PSD 图像
- MPI 可分布式读取数据与绘图，支持 CPU/GPU 训练
- 以 MSE 与密度分数双阈值判定异常，输出时间戳与结果

## 适用场景

- 对地震、仪器噪声、人为扰动等 DAS 事件做异常检测
- 处理数百 GB 至 TB 级 DAS 数据目录并建立索引查询
- 科研场景中训练并验证自编码器检测模型

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L8: _das-anomaly_ is an open-source Python package for unsupervised anomaly detection in distributed acoustic sensing (D
> L59: The package implements a convolutional autoencoder designed to compress and reconstruct power spectral density (PSD

## 星数曲线

```mermaid
xychart-beta
    title "DASDAE/das-anomaly 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-27 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `794a929f1774` · [字段定义](../../DATASET.md)*
