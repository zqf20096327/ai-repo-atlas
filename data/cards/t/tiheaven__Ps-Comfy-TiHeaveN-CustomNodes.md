# tiheaven/Ps-Comfy-TiHeaveN-CustomNodes

⭐ 48 · Python · MIT · 推送 2026-01-19 · [GitHub](https://github.com/tiheaven/Ps-Comfy-TiHeaveN-CustomNodes) · 个人维护 · 中文 README

**让 Photoshop 联动 ComfyUI 做局部重绘的节点包与插件**

需与配套 PS 插件共同使用的 ComfyUI 节点包：安装后不产生可视化节点，仅为 Comfy 服务器新增通信路由，使 PS 插件可读取工作流、传参执行并取回结果。核心流程为 PS 勾选选区、传参至 ComfyUI、实时预览 K 采样器、智能对象带蒙版原位贴回；图像以无损 PNG(RGBA) 传输。另支持多图参考、API 工作流生图、显存占用显示、队列中止与状态查询。限制：不支持子图，需 Photoshop ≥23.4.0。

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

- PS 选区→ComfyUI→实时预览→智能对象原位贴回的联动流程
- 选区自动扩展边界，图像以无损 PNG(RGBA) 传输
- 支持多图参考（画布/图层/图层+蒙版）与 API KEY 生图
- 内置简中/繁中/英三语，可自定义语言包

## 适用场景

- 在 Photoshop 内直接调用 ComfyUI 工作流做局部重绘
- 生图过程中在 PS 内实时预览 K 采样器进度
- 通过 API 调用模型生图而无需登录 ComfyUI 网页

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L86: Ps-Comfy-TiHeaveN-CustomNodes (ComfyUI Nodes) must be used in conjunction with Ps-Comfy-TiHeaveN-UXP-Plugin (Photos
> L90: - **ComfyUI Nodes**: After installation, there are no visual nodes. It only adds new communication routes to the Co
> L223: - **ComfyUI 节点**：安装后并无可视化节点，仅为 Comfy服务器 新增通信路由；

## 星数曲线

```mermaid
xychart-beta
    title "tiheaven/Ps-Comfy-TiHeaveN-CustomNodes 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 46 --> 49
    line [47, 48, 48]
```

2026-10-18 47 → 2026-10-27 48（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `039760996ba1` · [字段定义](../../DATASET.md)*
