# TorchIO-project/torchio

⭐ 2,450 · Python · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/TorchIO-project/torchio) · [官网](https://docs.torchio.org/) · 组织维护

**面向 PyTorch 的 3D 医学图像读取/预处理/增强 Python 库**

TorchIO 是基于 PyTorch 的 Python 库，为深度学习应用提供 3D 医学图像的读取、预处理、采样、增强与写出工具，包含强度与空间变换。除常规计算机视觉操作（如随机仿射变换）外，提供领域特定变换，如模拟 MRI 磁场不均匀性强度伪影与 k-space 运动伪影；支持基于 patch 的训练队列。项目受 NiftyNet 启发（该库已停止维护），最初由 EPSRC/UKRI、UCL 等机构支持，有发表于 Computer Methods and Programs in Biomedicine 的论文可引用。安装说明与教程见文档站与 Google Colab。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3D 医学图像的读取、预处理、采样、增强与写出
- 包含 MRI 领域特定伪影模拟（偏置场、k-space 运动伪影等）
- 基于队列的 patch 采样训练机制

## 适用场景

- PyTorch 医学影像深度学习流程的数据加载与增强
- MRI/CT 训练数据模拟真实采集伪影
- patch-based 3D 图像训练采样

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L131: TorchIO is a Python package containing a set of tools to efficiently
> L132: read, preprocess, sample, augment, and write 3D medical images in deep learning applications

## 星数曲线

```mermaid
xychart-beta
    title "TorchIO-project/torchio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 2449 --> 2452
    line [2451, 2450]
```

2026-10-18 2,451 → 2026-10-24 2,450（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `dfa3572fa132` · [字段定义](../../DATASET.md)*
