# copick/copick

⭐ 35 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/copick/copick) · [官网](https://copick.github.io/) · 组织维护

**冷冻电子断层扫描(cryoET)数据集的存储无关 Python API 库**

提供面向 cryoET 数据集的跨平台、无服务端数据访问 API：通过 fsspec 系列库抽象本地/共享文件系统、SSH 与云端存储，使用 multiscale OME-Zarr 格式并行访问图像数据；无需专门服务器或数据库。支持在 ChimeraX 与 Napari 中可视化与整理数据，并带插件系统可注册 inference/training 等分组 CLI 命令。面向 cryoET 结构生物学与机器学习流程的开发者，以 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 fsspec 的存储抽象：本地/SSH/S3/SMB 同一 API 访问
- 无服务器、无数据库，指向数据即可用
- multiscale OME-Zarr 云就绪图像访问
- 插件系统可注册 inference/training/evaluation 等 CLI 命令

## 适用场景

- 在共享存储或云端统一访问 cryoET 断层扫描数据
- 在 ChimeraX/Napari 中可视化与标注 cryoET 数据
- 为 cryoET 机器学习训练与推理流程提供数据读取层

## 场景标签

 · 领域:结构生物学/科学数据基础设施

## 证据(README 行号)

> L11: **copick** is a cross-platform, storage-agnostic and server-less dataset API for cryoET datasets. Access to the dat
> L122: Copick supports a plugin system that allows external Python packages to register CLI commands. Commands can be add

## 星数曲线

```mermaid
xychart-beta
    title "copick/copick 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-31 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `b19da2f8bab7` · [字段定义](../../DATASET.md)*
