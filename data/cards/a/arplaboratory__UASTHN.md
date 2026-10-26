# arplaboratory/UASTHN

⭐ 27 · Jupyter Notebook · MIT · 推送 2026-02-28 · [GitHub](https://github.com/arplaboratory/UASTHN) · [官网](https://xjh19971.github.io/UASTHN/) · 组织维护

**无人机热成像-卫星图像地理定位的不确定性感知单应估计模型**

ICRA 2025 论文官方代码库，出自 NYU arplaboratory。提出 UASTHN 方法：在无人机热成像与卫星影像之间做不确定性感知的深度单应估计，实现跨模态地理定位。提供 conda 环境配置、从 Hugging Face 自动下载模型的单对图像推理脚本、基于修改版 Boson-nighttime 数据集（122 GB，六次夜间飞行采集）的训练与评测脚本，以及 CropTTA 预训练模型。训练脚本面向 slurm sbatch 提交，也可直接 bash 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 不确定性感知的深度单应估计用于 UAV 热成像-卫星地理定位
- 推理脚本自动从 Hugging Face 下载模型并运行示例
- 提供 122 GB 修改版 Boson-nighttime 数据集与预训练模型（CropTTA）
- 含 anyloc 与 STGL 图像匹配基线的训练评测脚本

## 适用场景

- 复现论文中的 UAV 热成像地理定位实验
- 基于预训练模型对自己的热成像-卫星图像对做推理
- 在自建数据集上训练或评测单应估计地理定位模型

## 场景标签

 · 领域:机器人/遥感·地理定位

## 证据(README 行号)

> L8: This is the official repository for UASTHN: Uncertainty-Aware Deep Homography Estimation for UAV Satellite-Thermal G
> L29: To quickly get started with UASTHN, we provide a `UASTHN_demo.py` script. This demo automatically downloads the mod
> L64: ## Image-matching Baselines

## 星数曲线

```mermaid
xychart-beta
    title "arplaboratory/UASTHN 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-26 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5ca462579a56` · [字段定义](../../DATASET.md)*
