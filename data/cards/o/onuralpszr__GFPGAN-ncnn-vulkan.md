# onuralpszr/GFPGAN-ncnn-vulkan

⭐ 54 · C++ · GPL-3.0 · 推送 2026-06-24 · [GitHub](https://github.com/onuralpszr/GFPGAN-ncnn-vulkan) · 个人维护

**GFPGAN 人脸修复算法的 NCNN-Vulkan C++ 实现**

基于 GFPGAN 方法的人脸修复算法的 NCNN/Vulkan 实现，包含代码与预训练模型，面向移动设备与硬件加速场景，目标为修复监控画面、老照片、社交头像等低质量人脸图像。以 C++17 编写，需 CMake、Vulkan SDK、OpenCV、ncnn、libwebp 等依赖从源码编译构建。目前支持 GFPGANCleanv1-NoCE-C2 模型，pth→onnx→ncnn 转换与着色模型仍在 TODO 列表，项目自述为 WIP 状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- NCNN + Vulkan 后端的 GFPGAN 人脸修复实现
- 提供预训练模型文件（v0.0.1，Releases 下载）
- 面向移动设备优化的 C++17 代码与 CMake 构建流程

## 适用场景

- 在无 Python 环境的设备上运行人脸修复
- 修复老照片或低质量监控画面中的人脸
- 研究模型向 NCNN/Vulkan 部署的转换流程

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L15: Ncnn with Vulkan implementation of **GFPGAN aims at developing Practical Algorithms for Real-world Face Restoration
> L19: The goal of this project is to develop practical algorithms that can restore the appearance of damaged or low-quali

## 星数曲线

```mermaid
xychart-beta
    title "onuralpszr/GFPGAN-ncnn-vulkan 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 52 --> 55
    line [53, 54]
```

2026-10-18 53 → 2026-10-24 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4e965be95937` · [字段定义](../../DATASET.md)*
