# JiSenHua/ComfyUI-TD

⭐ 168 · Python · AGPL-3.0 · 推送 2026-08-20 · [GitHub](https://github.com/JiSenHua/ComfyUI-TD) · 个人维护 · 中文 README

**将 ComfyUI 生成内容实时串流到 TouchDesigner 的自定义节点**

ComfyUI 自定义节点集合，通过 WebSocket 将 ComfyUI 生成的图像、视频、点云（传统 PLY / Gaussian Splatting PLY）、音频与文本实时发送到 TouchDesigner，需配合 ComfyUI2TD.tox 组件（v_5.1.x 及以上）使用。提供 Hunyuan3D_V2、Tripo3D、TripoSR、3DPack、3DGS 等模型的 GLB/PLY 转点云并生成 CHOP 组件的传输节点，各节点依赖对应的第三方 ComfyUI 节点。部分节点部分功能（旧版 Tripo API 配置）已声明弃用；提供中文 README 与 Bilibili 视频教程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 经 WebSocket 将图像/视频/点云/音频从 ComfyUI 实时发送到 TouchDesigner
- 支持 Hunyuan3D_V2、Tripo3D、TripoSR、3DPack、3DGS 等模型的 GLB/PLY 转点云
- 需配套 ComfyUI2TD.tox 组件（v_5.1.x+），v_5.1.x 起预设工作流不再依赖 ComfyUI-Tooling-Nodes
- 提供 ComfyUI-Manager、手动解压、git clone、组件注入共 4 种安装方式

## 适用场景

- 在 TouchDesigner 中实时接收 ComfyUI 生成的图像与视频做视觉演出
- 把文本/图像生成的 3D 模型转为点云导入 TouchDesigner
- 在 TouchDesigner 中解析 Gaussian Splatting PLY 数据

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: **ComfyUI-TD** is a **ComfyUI to TouchDesigner** custom node for **real-time streaming** of generated data.
> L5: It supports sending **images**, **videos**, **point clouds** (**traditional PLY** / **Gaussian Splatting PLY**), and

## 星数曲线

```mermaid
xychart-beta
    title "JiSenHua/ComfyUI-TD 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 166 --> 169
    line [167, 168, 168]
```

2026-10-18 167 → 2026-10-28 168（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `00ba6b39e313` · [字段定义](../../DATASET.md)*
