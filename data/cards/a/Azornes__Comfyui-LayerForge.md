# Azornes/Comfyui-LayerForge

⭐ 352 · JavaScript · MIT · 推送 2026-08-21 · [GitHub](https://github.com/Azornes/Comfyui-LayerForge) · 个人维护

**ComfyUI 的类 Photoshop 分层画布编辑节点，服务合成与重绘工作流**

ComfyUI 自定义节点，在浏览器中提供多层画布编辑器：图层的增删、排序、移动、缩放、旋转，画笔遮罩编辑，12 种混合模式与透明度，撤销/重做分离历史，画布状态持久化到 IndexedDB。支持多边形套索选区用于 inpainting/outpainting，自动从 ComfyUI 输出目录导入生成图并裁剪到选区。可选抠图功能经 ComfyUI 原生 BiRefNet 加载器或本地 BRIA RMBG 2.0（Transformers 后端）生成前景蒙版。输出标准 IMAGE 与 MASK 供下游节点使用，需在 ComfyUI 环境内安装。

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

- 多层画布编辑：图层变换、12 种混合模式、独立遮罩与撤销历史
- 多边形套索选区工作流，自动导入并裁剪生成的 inpaint 图像
- 画布状态存于浏览器 IndexedDB，刷新页面后保留
- 可选抠图：BiRefNet 原生加载器或本地 BRIA RMBG 2.0

## 适用场景

- 在 ComfyUI 中做复杂的多层图像合成
- 用多边形选区定义 inpainting/outpainting 区域
- 为图层生成背景移除蒙版做抠图

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3:  LayerForge is a ComfyUI node for compositing images with multiple layers, masks, blend modes, and transformations. 
> L42: - **IMAGE:** The flattened composite from the visible layer stack.
> L182: LayerForge outputs standard ComfyUI `IMAGE` and `MASK` values. Connect the node to models and nodes that accept th

## 星数曲线

```mermaid
xychart-beta
    title "Azornes/Comfyui-LayerForge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 350 --> 353
    line [351, 352, 352]
```

2026-10-18 351 → 2026-10-30 352（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `a309daa7d716` · [字段定义](../../DATASET.md)*
