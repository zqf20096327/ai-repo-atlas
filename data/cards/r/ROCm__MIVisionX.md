# ROCm/MIVisionX

⭐ 218 · C++ · MIT · 推送 2026-10-28 · [GitHub](https://github.com/ROCm/MIVisionX) · [官网](https://rocm.docs.amd.com/projects/MIVisionX/en/latest/) · 组织维护

**AMD 计算机视觉工具包：OpenVX 引擎、RPP 扩展与 RunVX 执行器**

围绕 Khronos OpenVX 1.3.2 规范实现构建的计算机视觉工具包，4.0.0 版含三个组件：AMD OpenVX 引擎、AMD RPP OpenVX 扩展（经 rocAL 做图像/张量增强）与 RunVX 图执行器（执行 GDF 文本描述的 OpenVX 图），支持 CPU、HIP、OpenCL 三种后端。面向在 AMD CPU/GPU/APU 上开发视觉应用的开发者。安装途径为 ROCm 仓库包（ROCm 7.2.x 及以下，仅 HIP 后端）或源码编译（CMake，可 CPU-only 无需 GPU）；macOS 仅支持 CPU 后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenVX 1.3.2 规范的 AMD 实现，含 RPP 扩展与 RunVX 图执行器
- CPU / HIP / OpenCL 三种后端，可 CPU-only 编译无需 GPU
- 支持 Ubuntu/RedHat/SLES/Windows/macOS 多平台构建
- 附 Canny、光流等示例应用与 ctest 验证模块

## 适用场景

- 在 AMD GPU/APU 上以 OpenVX 图加速计算机视觉流水线
- 用 RunVX 命令行执行 GDF 描述的视觉图
- 经 rocAL/RPP 做图像与张量数据增强

## 场景标签

`图像视频处理` `推理引擎` · 领域:感知与多模态

## 证据(README 行号)

> L5: AMD MIVisionX is a computer vision toolkit built around a highly optimized, conformant open-source implementation of
> L18: * RunVX: Command-line utility to execute OpenVX graphs described in GDF text files

## 星数曲线

```mermaid
xychart-beta
    title "ROCm/MIVisionX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 217 --> 219
    line [218, 218]
```

2026-10-18 218 → 2026-10-29 218（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `6415e0d018e1` · [字段定义](../../DATASET.md)*
