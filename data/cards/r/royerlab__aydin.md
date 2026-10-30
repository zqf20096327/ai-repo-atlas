# royerlab/aydin

⭐ 179 · Python · BSD-3-Clause · 推送 2026-02-22 · [GitHub](https://github.com/royerlab/aydin) · [官网](https://royerlab.github.io/aydin/) · 组织维护

**自监督图像去噪工具库，面向显微成像等多维图像用户**

提供数十种图像去噪算法的 Python 工具：经典方法（Butterworth、NLM、小波、BMnD 等）与机器学习方法（Noise2Self-FGR、Noise2Self-CNN），基于 Noise2Self 思想做参数自动调优，无需干净参照图像。支持任意批量/通道维与最多 4 个时空维的 n 维数组图像。交付形态包括 Aydin Studio 图形界面、命令行接口、Python API 与 napari 插件。macOS 需装 libomp，Linux 需 Qt 系统依赖，GPU 加速依赖 CUDA 版 PyTorch（可选）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 经典与机器学习（CNN/梯度提升）两大族去噪算法，参数自动调优
- 处理任意批量/通道维、最多 4 个时空维的 n 维图像
- Studio GUI、CLI、API 与 napari 插件四种使用方式
- 提供 Docker 镜像免本地安装运行

## 适用场景

- 显微图像等 n 维科学图像的去噪预处理
- 在不写代码的图形界面里试验不同去噪算法与参数
- 在远程服务器/集群上通过 CLI 或 Docker 批量去噪

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L9: *Aydin* is a user-friendly, feature-rich, and fast **image denoising tool** that provides
> L10: a number of **self-supervised, auto-tuned, and unsupervised** image denoising algorithms.
> L28: In the Noise2Self paper
> L67:  - Noise2Self-FGR: Noise2Self denoising via Feature Generation and Regression (FGR). We use specially crafted integ

## 星数曲线

```mermaid
xychart-beta
    title "royerlab/aydin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 178 --> 180
    line [179, 179]
```

2026-10-18 179 → 2026-10-30 179（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `53a0690dc84b` · [字段定义](../../DATASET.md)*
