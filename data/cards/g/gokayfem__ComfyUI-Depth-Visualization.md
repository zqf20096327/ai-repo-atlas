# gokayfem/ComfyUI-Depth-Visualization

⭐ 75 · Python · GPL-3.0 · 推送 2026-08-01 · [GitHub](https://github.com/gokayfem/ComfyUI-Depth-Visualization) · 个人维护

**ComfyUI 深度图处理/诊断/3D 导出与可视化节点套件**

ComfyUI 自定义节点集合：对任意深度图做归一化、修复、着色、法线生成、范围掩码与统计分析，导出 PLY 点云与 glTF GLB 网格，生成视差运动帧，并在浏览器中提供 GPU 加速的位移网格实时预览（轨道/平移/缩放、PNG 截图、GLB/GLTF/OBJ 导出）。附带无需模型即可运行的示例工作流，可用真实深度估计器替换。Python 3.10+，Linux/Windows/macOS CI 测试；条件与导出节点在 CPU 张量上确定性运行，查看器用浏览器 WebGL，不依赖 CUDA/ROCm/MPS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 个深度处理节点（归一化/修复/着色/法线/掩码/统计）
- PLY 点云与零依赖 glTF 2.0 GLB 网格导出
- 浏览器 WebGL 位移网格实时预览，本地固定 Three.js r185 资源、无运行时网络请求
- 示例工作流以图像亮度替代深度，无模型即可运行

## 适用场景

- 在 ComfyUI 中清洗与诊断深度估计器的输出
- 将深度图转换为点云、网格或视差动画帧
- 在图内实时预览深度位移网格并导出几何

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: A complete offline depth-conditioning, diagnostics, 3D export, and parallax toolkit for ComfyUI. It cleans and norma
> L33: Install with ComfyUI Manager, or clone manually:
> L41: Restart ComfyUI. Nodes are under `visualization/3D` and `depth/toolkit`.

## 星数曲线

```mermaid
xychart-beta
    title "gokayfem/ComfyUI-Depth-Visualization 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 73 --> 76
    line [74, 75, 75]
```

2026-10-18 74 → 2026-10-28 75（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `038caad61b87` · [字段定义](../../DATASET.md)*
