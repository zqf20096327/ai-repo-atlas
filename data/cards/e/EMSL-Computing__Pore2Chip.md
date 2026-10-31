# EMSL-Computing/Pore2Chip

⭐ 14 · Python · MIT · 推送 2026-09-23 · [GitHub](https://github.com/EMSL-Computing/Pore2Chip) · [官网](https://www.emsl.pnnl.gov/science/instruments-resources/terraforms-pore2chip) · 组织维护

**土壤 XCT 图像分析并生成微流控芯片设计的 Python 库**

面向研究者的 Python 模块：读取土壤 X 射线 CT 图像，基于 PoreSpy/OpenPNM 提取孔隙与喉道尺寸分布、连通数及 feret 直径等结构指标，进而生成代表性 2D 微模型设计，可导出 SVG/DXF/VTK 文件，并给出经 Inkscape/FreeCAD 转换为 STL 用于增材制造或激光蚀刻加工 lab-on-a-chip 的工作流。提供 pip 安装、conda 环境、Docker 镜像（含 Jupyter）与 EMSL Tahoma 集群使用说明。AI/ML 部分（PINNs 物理仿真等）为在研功能，当前核心为图像分析与几何生成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 XCT 图像提取孔隙/喉道尺寸分布与连通数
- 生成代表性 2D 微模型设计并导出 SVG/DXF/VTK
- 提供 SVG→STL 增材制造与激光蚀刻加工工作流
- 支持 pip/conda/Docker（含 Jupyter）多种安装运行方式

## 适用场景

- 分析土壤 CT 图像的孔隙结构特征
- 将孔隙网络转化为可加工的微流控芯片设计
- 为 ModEx 工作流生成微模型实验蓝图

## 场景标签

`图像视频处理` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L4: Pore2Chip is a Python module designed to streamline the process of analyzing X-ray computed tomography (XCT) images 
> L184: * Physics-informed machine learning needed for flow, thermal, and reactive-transport modeling (e.g., advanced phys

## 星数曲线

```mermaid
xychart-beta
    title "EMSL-Computing/Pore2Chip 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `b33cc5c46945` · [字段定义](../../DATASET.md)*
