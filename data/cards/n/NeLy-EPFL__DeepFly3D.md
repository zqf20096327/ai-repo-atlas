# NeLy-EPFL/DeepFly3D

⭐ 102 · Jupyter Notebook · LGPL-3.0 · 推送 2026-08-11 · [GitHub](https://github.com/NeLy-EPFL/DeepFly3D) · 组织维护

**针对 tethered 果蝇的多视角无标记 3D 姿态估计流水线与 GUI**

基于 PyTorch 与 PyQt5 的果蝇 2D-3D 姿态估计工具：读取 7 相机排列的图像或视频，自动完成 2D 姿态预测、免标定板的几何约束标定与三角化，输出 2D/3D 关键点、标定参数与置信度到 df3d_result.pkl。提供 df3d-cli 命令行与 Python 接口，附带 GUI 用于人工修正 2D 估计误差。仅测试于 Ubuntu 和 macOS，2D 预测需 CUDA 驱动。方法发表于 eLife，相关工作见 ICCV 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 免标定板，用 pictorial structures 几何约束自动校正误差
- CLI 一条命令完成 2D 姿态估计、标定与三角化
- GUI 手动修正 2D 估计，结果并入最终输出
- 输出含 2D/3D 关键点、相机标定参数与 heatmap 置信度

## 适用场景

- 对 tethered 果蝇的多相机图像批量做 3D 姿态估计
- 用 GUI 人工校正自动估计中的错误关键点
- 复现或引用论文中的果蝇运动捕捉流水线

## 场景标签

 · 领域:计算神经科学/动物行为

## 证据(README 行号)

> L8: DeepFly3D is a PyTorch and PyQT5 implementation of 2D-3D tethered Drosophila pose estimation. It aims to provide an 
> L10: DeepFly3D does not require a calibration pattern, it enforces geometric constraints using pictorial structures, whi

## 星数曲线

```mermaid
xychart-beta
    title "NeLy-EPFL/DeepFly3D 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 101 --> 103
    line [102, 102]
```

2026-10-18 102 → 2026-10-27 102（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d1580949ffbe` · [字段定义](../../DATASET.md)*
