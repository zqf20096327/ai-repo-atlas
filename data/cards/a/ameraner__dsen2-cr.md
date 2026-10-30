# ameraner/dsen2-cr

⭐ 184 · Python · GPL-3.0 · 推送 2026-01-26 · [GitHub](https://github.com/ameraner/dsen2-cr) · 个人维护

**去除 Sentinel-2 影像云层的深度残差网络模型代码**

DSen2-CR 是发表于 ISPRS Journal 2020 的论文配套仓库：用深度残差神经网络融合 SAR 与光学数据，从有云 Sentinel-2 影像预测无云影像。提供 Python/Keras 模型代码、多种预训练权重下载链接（CARL 损失/L1 损失、有无 SAR 输入）及 SEN12MS-CR 数据集指引，另含 PyTorch 实现文件。通过 conda 环境或含 CUDA 的 Docker 镜像安装，命令行脚本完成训练、断点恢复与预测评估。代码写于 2018-2019 年，作者声明可能存在 bug 且新版依赖或需修改，作者表示无法完全复现测试并欢迎社区提交 PR。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- SAR-光学融合的深度残差网络做云去除预测
- 提供多种预训练 checkpoint（Google Drive 下载）
- 附 PyTorch 模型实现（Code/dsen2cr_pytorch_model.py）
- 提供含 CUDA 的 Dockerfile 与 conda 安装方式

## 适用场景

- 对 Sentinel-2 有云影像做云去除重建
- 复现论文实验或用 SEN12MS-CR 数据集继续研究
- 作为云去除任务的基线模型进行对比训练

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L1: # Cloud removal in Sentinel-2 imagery using a deep residual neural network and SAR-optical data fusion
> L11: This repository contains the code and models for the paper
> L12: > Meraner, A., Ebel, P., Zhu, X. X., & Schmitt, M. (2020). Cloud removal in Sentinel-2 imagery using a deep residua

## 星数曲线

```mermaid
xychart-beta
    title "ameraner/dsen2-cr 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 182 --> 185
    line [183, 184, 184]
```

2026-10-18 183 → 2026-10-30 184（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1abfe4184ef0` · [字段定义](../../DATASET.md)*
