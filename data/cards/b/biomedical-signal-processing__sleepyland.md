# biomedical-signal-processing/sleepyland

⭐ 52 · AMPL · MIT · 推送 2026-04-16 · [GitHub](https://github.com/biomedical-signal-processing/sleepyland) · [官网](https://youtube.com/playlist?list=PLl7J6NiydmVKJ2SAh7fTKaSK-JoPTgvG-&si=Tw0bxR_4i7JQwbzw) · 组织维护

**睡眠数据分析与自动睡眠分期工具箱，面向研究者与临床医生**

基于 Python 的 Web 应用，对大规模睡眠数据（PSG/EDF）做自动化睡眠分期：内置 YASA、U-Sleep、DeepResNet、SleepTransformer 四种模型，支持单通道（EEG 或 EOG）与多通道配置，可在 NSRR 标准数据集上评测对比模型，也可上传自有 EDF 文件做预测。模型在 NSRR 等公开数据集上经一致流程训练验证。全部分析本地运行（仅 CPU，无 GPU 支持），通过 Docker 部署，浏览器访问 localhost:8887 操作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 4 种睡眠分期模型（YASA/U-Sleep/DeepResNet/SleepTransformer）
- 涵盖 17 个 NSRR 训练数据集与 6 个开放测试数据集的公平评测
- 支持上传自有 EDF 文件本地分析，数据不离开本机
- 提供 UI 交互可视化与 Jupyter Notebook 两种结果探索方式

## 适用场景

- 我需要对睡眠脑电记录做自动睡眠分期
- 我想在标准 NSRR 数据集上公平对比多个分期模型
- 我有自己的 EDF 数据，想在不外传数据的前提下预测睡眠阶段

## 场景标签

`数据分析` `模型评测` · 领域:效率与自动化

## 证据(README 行号)

> L5: **SLEEPYLAND** is a Python-based web application developed for the automated FAIR sleep staging analysis of large sl
> L80: > All the exposed sleep staging models run locally on your CPU (GPU support is not available). As a result, some mo

## 星数曲线

```mermaid
xychart-beta
    title "biomedical-signal-processing/sleepyland 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-29 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `38a7510eab73` · [字段定义](../../DATASET.md)*
