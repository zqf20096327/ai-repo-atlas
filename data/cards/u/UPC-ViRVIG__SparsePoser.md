# UPC-ViRVIG/SparsePoser

⭐ 51 · C# · MIT · 推送 2026-06-06 · [GitHub](https://github.com/UPC-ViRVIG/SparsePoser) · [官网](https://upc-virvig.github.io/SparsePoser) · 组织维护

**稀疏传感器实时全身动作重建方法（TOG 论文官方代码）**

ACM TOG 论文 SparsePoser 的官方实现：用 PyTorch 网络从稀疏追踪数据（头、双手、双脚等末端）实时重建全身动作。项目分两部分：python 目录为网络实现，SparsePoserUnity 为 Unity 工程，二者通过 TCP 通信。支持 BVH 文件离线评估、Unity 模拟器交互、VR 实时演示（需 HMD、两个 VIVE 手柄与三个 VIVE Tracker 3.0）及模型训练。训练数据为 Xsens Awinda 录制的 1GB 以上动作捕捉数据集。限制：仅测试过 Python 3.9 与 Unity 2021.2.13f1；用户体型与骨架差异过大时系统可能失败。

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

- 从稀疏末端追踪数据实时重建全身动作
- Python(PyTorch) 网络与 Unity 通过 TCP 通信
- 提供 BVH 离线评估、模拟器与 VR 三种运行方式
- 附带训练流程与 1GB 以上 Xsens 动捕数据集

## 适用场景

- VR 应用中用少量追踪器实时驱动全身虚拟形象
- 研究人员复现论文并训练自己的动作重建模型
- 对 BVH 动捕文件做全身动作合成与评估

## 场景标签

 · 领域:计算机图形学/人体动作重建

## 证据(README 行号)

> L16: This repository contains the implementation of the method shown in the paper *SparsePoser: Real-time Full-body Moti
> L26: The project is structured into two primary directories: `SparsePoserUnity`, which contains the Unity project, and `

## 星数曲线

```mermaid
xychart-beta
    title "UPC-ViRVIG/SparsePoser 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-29 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `e4d6729e14c7` · [字段定义](../../DATASET.md)*
