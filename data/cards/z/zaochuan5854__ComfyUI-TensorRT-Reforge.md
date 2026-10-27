# zaochuan5854/ComfyUI-TensorRT-Reforge

⭐ 26 · Python · MIT · 推送 2026-07-17 · [GitHub](https://github.com/zaochuan5854/ComfyUI-TensorRT-Reforge) · [官网](https://qiita.com/zaochuan5854/items/f7b625bb9df5f4742b61) · 个人维护

**面向 ComfyUI 的 TensorRT 引擎导出与加载节点**

ComfyUI 的自定义节点，将扩散模型导出为 TensorRT 引擎并在 ComfyUI 中加载运行，提供 NVIDIA GPU 上的推理加速。源自 ComfyUI_TensorRT 项目的重构版本，支持 Anima、Flux、SD3/SD3.5、SDXL、SD1.5、AuraFlow、SVD 等模型架构；通过 Dynamo ONNX 导出与动态 Opset 管理提升导出成功率，利用 NVIDIA Refit 实现接近即时的 LoRA 权重切换（实验性）。要求 CUDA 12.x 环境（推荐 12.8），不支持 CUDA 11 与 13.x。以 git clone 源码方式安装到 custom_nodes 目录并 pip 安装依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 Anima/Flux/SD3/SD3.5/SDXL/SD1.5/AuraFlow/SVD 架构的 TensorRT 引擎导出与加载
- 基于 NVIDIA Refit 的 LoRA 近即时权重切换（实验性）
- Dynamo ONNX 导出与动态 Opset 管理（18 vs 25）
- LoRA 需在导出时启用并生成 .bundle 元数据文件

## 适用场景

- 在 ComfyUI 工作流中用 TensorRT 加速 Stable Diffusion 类模型推理
- 导出引擎后快速切换不同 LoRA 而无需重建引擎
- 为新架构扩散模型（如 Anima、Flux）生成 TensorRT 引擎

## 场景标签

`图像生成` `推理引擎` · 领域:内容生成

## 证据(README 行号)

> L2: A modernized, robust, and highly extensible TensorRT engine exporter and loader for ComfyUI.
> L33: 1. Clone this repository into your `ComfyUI/custom_nodes` directory:

## 星数曲线

```mermaid
xychart-beta
    title "zaochuan5854/ComfyUI-TensorRT-Reforge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c557337f18fd` · [字段定义](../../DATASET.md)*
