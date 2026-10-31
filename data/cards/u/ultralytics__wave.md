# ultralytics/wave

⭐ 86 · Python · AGPL-3.0 · 推送 2026-08-28 · [GitHub](https://github.com/ultralytics/wave) · [官网](https://ultralytics.com) · 组织维护

**用深度学习读出全波形 ToF 粒子探测器信号的代码库**

Ultralytics WAVE（WAveform Vector Exploitation）提供用深度学习对全波形飞行时间粒子探测器进行信号读出与重构的代码，面向粒子物理研究人员。同时提供 PyTorch 与 TensorFlow 实现（后者基于 TensorFlow 1.x API），支持在 Google Cloud Platform 上运行实验脚本，训练脚本可自动下载示例数据文件。安装方式为从仓库 requirements.txt 用 pip 安装依赖（numpy/scipy/torch/tensorflow 等），论文发表于 arXiv。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PyTorch 与 TensorFlow 双实现（TF 版基于 1.x API）
- 训练脚本自动下载 wavedata25ns.mat 示例数据
- 提供 GCP 部署脚本 gcp/wave_pytorch_gcp.py
- plotly 可选增强可视化

## 适用场景

- 全波形 ToF 探测器信号的深度学习读出与重构
- 粒子物理实验中的波形数据处理研究
- 在 Google Cloud 上运行 WAVE 训练实验

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L7: Here, we introduce **WA**veform **V**ector **E**xploitation (WAVE), a novel approach leveraging Deep Learning to rea
> L16: The primary goal of this project is to develop and share advanced Machine Learning techniques applicable to full-wa

## 星数曲线

```mermaid
xychart-beta
    title "ultralytics/wave 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 84 --> 87
    line [85, 86, 86]
```

2026-10-18 85 → 2026-10-31 86（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `9737750322f2` · [字段定义](../../DATASET.md)*
