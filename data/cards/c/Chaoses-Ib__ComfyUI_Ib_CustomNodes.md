# Chaoses-Ib/ComfyUI_Ib_CustomNodes

⭐ 59 · Python · MIT · 推送 2026-08-16 · [GitHub](https://github.com/Chaoses-Ib/ComfyUI_Ib_CustomNodes) · 个人维护

**ComfyUI 自定义节点集：按路径加载图像与 PIL 图像转换**

面向 ComfyUI 用户的自定义节点集合，包含三个节点：Load Image From Path 从源路径而非上传目录加载图像，支持绝对路径及相对 input/output/temp 目录的路径格式，避免输入目录产生重复文件，可在源文件变更后重新加载；其增强版增加图像预览、文件浏览器与 path 输出；另提供 PIL.Image 与 ComfyUI 图像格式互转的三个节点，主要配合 ComfyScript 的 real mode 使用。通过 ComfyUI-Manager 的 Custom Nodes Manager 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按源路径加载图像，避免上传复制产生的重复文件
- 支持绝对路径与 input/output/temp 相对路径格式
- 增强版含图像预览、文件浏览器与 path 输出
- 提供 PIL.Image 与 ComfyUI Image/Mask 格式互转节点

## 适用场景

- 配合 Photoshop Quick Export 快速对编辑后的图像做 img2img/inpaint
- 在 ComfyScript real mode 中使用 PIL 图像对象
- 从输出目录直接回读生成结果继续处理

## 场景标签

 · 领域:图像生成工具链

## 证据(README 行号)

> L1: # ComfyUI_Ib_CustomNodes
> L59: Mainly for use with ComfyScript's real mode.

## 星数曲线

```mermaid
xychart-beta
    title "Chaoses-Ib/ComfyUI_Ib_CustomNodes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-29 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f77548483859` · [字段定义](../../DATASET.md)*
