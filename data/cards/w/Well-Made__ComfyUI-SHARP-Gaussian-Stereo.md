# Well-Made/ComfyUI-SHARP-Gaussian-Stereo

⭐ 14 · JavaScript · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/Well-Made/ComfyUI-SHARP-Gaussian-Stereo) · 个人维护

**ComfyUI 节点：单图生成高斯泼溅并在立体查看器中检视**

独立的 ComfyUI 自定义节点包，运行 Apple 的 SHARP 单图视图合成模型，将输入照片导出为 .ply 高斯泼溅文件，并内置支持 Parallel/Toe-in 立体与单目模式的交互式查看器，提供焦距、泼溅尺寸、感知深度等控制。节点自动从 Apple 的 Hugging Face 仓库下载约 2.7 GB 权重；权重许可证限定研究用途，排除商业使用。包本身以 GPL-3.0 分发，不含 Python、PyTorch、CUDA 与模型权重，需已有 CUDA GPU 的 ComfyUI 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单张照片推理生成 3D 高斯泼溅并导出 .ply
- 交互式立体查看器：Parallel/Toe-in 双目与单目视图切换
- 查看器侧实时调节泼溅尺寸与感知深度，无需重跑推理
- 自动从官方 apple/Sharp 仓库下载检查点（约 2.7 GB）

## 适用场景

- 把一张照片在 ComfyUI 里转成可交互的 3D 泼溅预览
- 用立体（红蓝/双目）方式查看单图生成的近视角场景
- 在 ComfyUI 工作流中对比不同焦距与精度设置的重建结果

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L9: The package runs Apple's SHARP model on a ComfyUI image and exports the predicted scene as a `.ply` Gaussian Splat. 
> L15: - Standalone implementation: no runtime dependency on `ComfyUI-Sharp`, `ComfyUI-GeometryPack`, `comfy-env`, or `com
> L40: - A working ComfyUI installation with a CUDA-capable GPU and its supported PyTorch build.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `077b5f33fd27` · [字段定义](../../DATASET.md)*
