# kanglcn/moraine

⭐ 44 · Python · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/kanglcn/moraine) · [官网](https://kanglcn.github.io/moraine/) · 个人维护

**GPU 加速的 InSAR 后处理函数库，面向熟练用户**

Python 库，提供 SAR 影像配准与地理编码之后的 InSAR 后处理功能：PS/DS 识别、相干矩阵估计、相位链接、深度学习滤波（n2f 系列）与解缠等。不做固定工作流，以函数集合形式提供，数据为 NumPy/CuPy/Zarr 数组，多函数以 GPU 或 OpenMP 实现，可分块处理超出内存的数据并支持多 GPU。强依赖 CuPy 与 CUDA，仅能在 NVIDIA GPU 设备上运行；API 处于密集开发期，可能随时变更。提供 CLI 与 TOML 流水线（断点续跑），并附 AGENTS.md 供编码 agent 驱动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- PS/DS 识别、相干矩阵估计、相位链接等 InSAR 后处理函数集合
- GPU/OpenMP 实现，Zarr 分块处理，数据可大于内存并支持多 GPU
- CLI 与 TOML 流水线，按参数与输入变化跳过已完成步骤
- 深度学习滤波（n2f/n2fs3d/n2ft），需另装 PyTorch 并下载训练模型

## 适用场景

- 对 GAMMA 等输出的时序 SAR 数据做 PS/DS 处理与解缠
- 按需组合函数构建自己的 InSAR 处理流程
- 通过自然语言让 Claude Code 等 AI agent 驱动整条处理链

## 场景标签

 · 领域:遥感/地学数据处理

## 证据(README 行号)

> L6: This package provide functions for InSAR post-processing which refers as
> L8: include PS/DS identification, coherence matrix estimation, phase linking
> L48: advanced PS/DS identification, phase linking and deep-learning-based

## 星数曲线

```mermaid
xychart-beta
    title "kanglcn/moraine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-31 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8a88d0315bab` · [字段定义](../../DATASET.md)*
