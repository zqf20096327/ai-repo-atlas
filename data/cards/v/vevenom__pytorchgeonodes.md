# vevenom/pytorchgeonodes

⭐ 53 · Python · NOASSERTION · 推送 2025-11-23 · [GitHub](https://github.com/vevenom/pytorchgeonodes) · [官网](https://vevenom.github.io/pytorchgeonodes/) · 组织维护

**将 Blender 几何节点模型转为可微分 PyTorch 代码的 3D 重建库**

PyTorch 库，把 Blender Geometry Nodes 设计的程序化形状模型转译为可微分的 PyTorch/PyTorch3D 代码，用于 3D 物体重建。提供坐标下降、梯度下降与遗传算法拟合形状参数，支持合成场景与 ScanNet/SCANnotate 数据集实验，并集成 Gaussian Splatting（procedural_gs 分支）。设计自定义形状程序需使用 Blender 4.0，且仅支持部分节点类型。配套论文发表于 CVPR 2025。以 conda 环境配置加 Python 脚本方式运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动将 Blender Geometry Nodes 程序转译为可微分 PyTorch 代码
- 提供梯度下降、坐标下降与遗传算法拟合形状参数
- 支持 ScanNet/SCANnotate 场景的重建实验
- procedural_gs 分支集成 Gaussian Splatting

## 适用场景

- 从 ScanNet 场景点云重建可编辑的程序化 3D 形状
- 在 Blender 中设计形状程序并用梯度/遗传算法拟合参数
- 将程序化形状表示与 Gaussian Splatting 结合做场景编辑

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10: **PyTorchGeoNodes** enables differentiable procedural graphs in PyTorch that reimplement functionalities of Geometr
> L14: We provide algorithms for fitting parameters of PyTorchGeoNodes programs / procedural models, designed in Blender, 
> L162: @article{stekovic2025pytorchgeonodes,

## 星数曲线

```mermaid
xychart-beta
    title "vevenom/pytorchgeonodes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-25 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9faad6b6134a` · [字段定义](../../DATASET.md)*
