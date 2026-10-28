# Damkohler/jlc-comfyui-nodes

⭐ 27 · Python · NOASSERTION · 推送 2026-10-22 · [GitHub](https://github.com/Damkohler/jlc-comfyui-nodes) · 个人维护

**ComfyUI 自定义节点集：非递归多 ControlNet 组合与 Flux 工作流工具**

面向 ComfyUI 的自定义节点集合，核心是非递归 ControlNet 组合方法：将递归嵌套的多 ControlNet 评估改为扁平化组合路径，执行成本随 ControlNet 数量近似线性增长。另提供填充画布的 inpaint/outpaint 节点、ControlNet 预处理器包装、动态 LoRA 加载器（最多 10 槽位）、阶段边界 VRAM 清理、GPU 冷却门、多种前端工具节点。面向 Flux 图像生成、ControlNet 重度工作流与 LoRA 实验，通过 ComfyUI Registry 或 git clone 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 非递归 ControlNet 组合：扁平化路径，成本随 ControlNet 数量近似线性
- 动态 LoRA 加载器：最多 10 个预声明槽位，含块权重变体
- 填充画布节点支持 inpainting 与 outpainting
- GPU 冷却门（定时/NVIDIA 温度/组合模式）与阶段边界 VRAM 清理

## 适用场景

- 在 ComfyUI 中组合多个 ControlNet 而避免递归链的运行时增长
- 搭建 Flux 图像生成与 inpaint/outpaint 工作流
- 在多阶段推理图中管理 LoRA 栈与 VRAM

## 场景标签

`图像生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L12: JLC ComfyUI Nodes is a custom-node collection built around Non-Recursive ControlNet Composition, a method introduce
> L18: Developed by J. L. Córdova, the project is especially focused on Flux-oriented image-generation pipelines, ControlN
> L199: - Flux-based image generation

## 星数曲线

```mermaid
xychart-beta
    title "Damkohler/jlc-comfyui-nodes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `c45e63e7a3a5` · [字段定义](../../DATASET.md)*
