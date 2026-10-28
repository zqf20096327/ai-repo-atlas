# AI-in-Cardiovascular-Medicine/HolOrama

⭐ 20 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/AI-in-Cardiovascular-Medicine/HolOrama) · [官网](https://holorama.readthedocs.io/en/latest/) · 组织维护

**心脏影像深度学习分割、修改与融合的图形界面平台**

面向 IVUS、OCT 与冠脉 CT 血管造影（CCTA）影像（DICOM/NIfTi）的 GUI 应用：提供逐帧轮廓勾画与测量、IVUS 腔体自动分割（经 nnUZoo，需 PyTorch 源码安装）、自动门控与呼吸运动校正、CCTA 三维体渲染与笔刷/套索分割编辑，以及将 IVUS/OCT 与 CCTA 几何对齐拼接为单一血管树的融合流程，可输出 CFD 就绪网格与 NIfTi/STL/CSV。Windows 提供预构建安装包（不含自动 AI 分割），Linux/macOS/Windows 另提供脚本或源码安装（默认 GPU-ready，CUDA 11.8/12.1 可选 CPU）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- IVUS/OCT 逐帧轮廓勾画、自动门控与呼吸运动校正
- IVUS 腔体自动分割（nnUZoo，源码安装时可用）
- CCTA 3D 体渲染与笔刷/套索多标签分割编辑
- IVUS/OCT 与 CCTA 融合为单一血管树几何，输出 CFD 就绪网格

## 适用场景

- 对 IVUS/OCT 影像做轮廓勾画、门控与定量报告
- 对 CCTA 数据做手动/自动分割并 3D 可视化
- 将腔内影像与 CCTA 融合生成用于 CFD 模拟的血管几何

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L21: - Quantification of Intravascular Ultrasound (IVUS) and Optical Coherence Tomography (OCT)
> L49: The packaged build does **not** include automatic AI segmentation (which requires a full PyTorch/TensorFlow install
> L178: - **Automatic segmentation** of (currently only IVUS) lumen for all frames

## 星数曲线

```mermaid
xychart-beta
    title "AI-in-Cardiovascular-Medicine/HolOrama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `a73d6556d0a0` · [字段定义](../../DATASET.md)*
