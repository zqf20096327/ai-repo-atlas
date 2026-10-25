# wwu-mmll/deepmriprep

⭐ 63 · Python · MIT · 推送 2025-11-28 · [GitHub](https://github.com/wwu-mmll/deepmriprep) · [官网](https://github.com/wwu-mmll/deepmriprep) · 组织维护

**神经网络驱动的 T1 MRI 预处理工具：秒级完成 VBM/RBM 全流程**

面向神经影像研究者的 T1 加权 MRI 预处理工具，用神经网络完成体素形态学分析（VBM）全流程：脑提取、仿射配准、组织分割、非线性配准与平滑，GPU 上每幅约 10 秒；另支持图谱配准用于基于区域的形态学分析（RBM），提供 20 余个图谱。以 pip 安装的 Python 包提供，含 GUI、CLI 与 Python API 三种使用方式，读取 BIDS 目录输出组织体积、概率图与图谱区域体积等，并配套 QC 报告（affine_loss/warp_mse 百分位）。声明与 fMRIPrep/sMRIPrep/NiPreps 无关。

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

- 神经网络完成脑提取、配准、组织分割、平滑全流程，GPU 约 10 秒/幅
- 支持 20 余个脑图谱配准及分区体积输出（RBM）
- GUI / CLI / Python API 三种使用方式，输入 BIDS 目录
- 基于与 10,000+ OpenNeuro MRI 对比的 QC 指标（affine_loss/warp_mse 百分位）

## 适用场景

- 对 T1 MRI 数据跑 VBM 预处理，快速得到灰质/白质体积与调制平滑图
- 做基于脑图谱的区域形态学分析（RBM）
- 用 QC 报告排查配准异常的影像数据

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L7: deepmriprep runs **all preprocessing steps** needed for **Voxel-based Morphometry** (VBM) of T1w MR images:
> L15: Using neural networks, it only takes **~10 seconds** on a GPU (~100 seconds without a GPU) per image 🔥
> L24: For GPU-acceleration (NVIDIA needed), PyTorch should be installed first via the proper install command 🔥

## 星数曲线

```mermaid
xychart-beta
    title "wwu-mmll/deepmriprep 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 61 --> 64
    line [62, 63, 63]
```

2026-10-18 62 → 2026-10-25 63（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7682633c0410` · [字段定义](../../DATASET.md)*
