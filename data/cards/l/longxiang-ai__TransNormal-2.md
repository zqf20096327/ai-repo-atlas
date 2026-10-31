# longxiang-ai/TransNormal-2

⭐ 14 · Python · NOASSERTION · 推送 2026-09-10 · [GitHub](https://github.com/longxiang-ai/TransNormal-2) · [官网](https://longxiang-ai.github.io/TransNormal-2/) · 组织维护 · 中文 README

**单步单目法向估计模型：一图一次预测输出表面法向**

论文 TransNormal-2 的官方实现：基于 FLUX.2 的 rectified-flow 模型，从单张 RGB 图像经单次确定性预测步输出表面法向（不透明场景与透明物体两种域），配合几何精化模块 GRM 改善解码边缘细节。提供推理脚本与 Python API，支持单图/文件夹批处理、BF16/FP32、CPU offload；权重发布于 Hugging Face，基于 9B 的 FLUX.2 基础模型（需在 Black Forest Labs 获取访问权限），训练代码尚未发布。作者来自浙江大学。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单步确定性预测，无采样噪声，输出 PNG 可视化与 float32 NumPy 法向数组
- 支持不透明与透明物体两域（--domain opaque/transparent），GRM 默认启用
- 提供 CLI 与 Python API（TransNormal2Pipeline），支持批处理、分辨率限制与 CPU offload

## 适用场景

- 从单张图像生成场景表面法向图用于 3D 感知下游任务
- 透明物体（玻璃等）的法向估计
- 对文件夹图像批量生成法向预测结果

## 场景标签

 · 领域:计算机视觉/3D几何估计

## 证据(README 行号)

> L19: - **One RGB image, one prediction step.** A FLUX.2-based rectified-flow model estimates surface normals for general
> L76: python inference.py --input path/to/image.jpg --output_dir outputs/normal --save_npy
> L113: The method uses a single deterministic prediction step without sampling noise.

## 星数曲线

```mermaid
xychart-beta
    title "longxiang-ai/TransNormal-2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `c950157ef0b0` · [字段定义](../../DATASET.md)*
