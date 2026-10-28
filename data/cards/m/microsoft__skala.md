# microsoft/skala

⭐ 266 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/microsoft/skala) · [官网](https://aka.ms/dft) · 组织维护

**深度学习 DFT 交换相关泛函，供量子化学计算使用**

Microsoft Research AI for Science 开发的神经网络交换相关（XC）泛函库，从电子密度特征预测交换相关能量，用于密度泛函理论计算。推荐模型 skala-1.1 约 38.5 万参数，含逐原子 packed grid、多层非局域层与对称收缩。通过 Python 包 skala 发布，可经 PySCF（CPU）、GPU4PySCF（GPU）与 ASE 调用；另提供 C++/Fortran/C 集成示例与 GauXC 集成路径。限制：仅支持 Linux 与 Apple Silicon macOS、Python 3.11-3.13；GPU 环境需匹配 CUDA 版本的专用 wheel。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 神经网络 XC 泛函，随 PySCF/GPU4PySCF/ASE 运行 SCF 计算
- 提供 ASE calculator，支持能量、力与几何优化工作流
- 官方模型加载时自动做 SHA-256 完整性校验
- 含 C++(libtorch)/Fortran(FTorch)/GauXC 等编译语言集成示例

## 适用场景

- 在 PySCF 中用 Skala 做分子 SCF 计算
- GPU 上经 GPU4PySCF 运行 Skala DFT 计算
- 用 ASE calculator 做能量/力计算与几何优化

## 场景标签

 · 领域:计算化学/量子化学

## 证据(README 行号)

> L8: Skala is a neural network-based exchange-correlation functional for density functional theory (DFT), developed by Mi
> L10: Trained on a large, diverse dataset — including coupled-cluster atomization energies and public benchmarks — Skala 

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/skala 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 265 --> 267
    line [266, 266]
```

2026-10-18 266 → 2026-10-28 266（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9ef2a8e4ee93` · [字段定义](../../DATASET.md)*
