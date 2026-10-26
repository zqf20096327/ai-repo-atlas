# vslinx/ComfyUI-vslinx-nodes

⭐ 27 · Python · GPL-3.0 · 推送 2026-10-07 · [GitHub](https://github.com/vslinx/ComfyUI-vslinx-nodes) · 个人维护

**面向 ComfyUI 工作流的自定义节点集合：图像加载、分支控制与实用工具**

ComfyUI 插件形式的节点合集：图像方面提供多选批量/列表加载、输出目录最后生成图加载（自动刷新、MaskEditor 支持）、带筛选交互的 Better Image Preview、暂停工作流人工挑选图像的 Image Filter、按任意倍率模型放大（nearest/bilinear/area/Lanczos）、复古调色板像素画转换、分批 VAE 解码以降低峰值显存；控制流方面提供布尔 AND/OR/Flip、按布尔或镜像他节点状态 bypass/mute 下游节点、五值打包 pipe、书签跳转等；另含模型/LoRA 悬停预览与 Return type mismatch 修复设置。通过 ComfyUI-Manager 或 git clone 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多图选择加载（batch/list）与输出目录最后生成图加载（自动刷新）
- Image Filter 暂停工作流人工筛选图像批次，支持超时策略
- 布尔逻辑与 bypass/mute 状态镜像节点实现条件分支
- 分批/分块 VAE 解码降低峰值显存；模型悬停预览（.safetensors/.ckpt/.pt/.gguf）

## 适用场景

- 在 ComfyUI 工作流中批量加载并人工筛选图像
- 用布尔与 bypass/mute 节点组织复杂分支流程
- 为模型/LoRA 下拉列表添加悬停预览图

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L1: # ComfyUI-vslinx-nodes
> L2: Custom ComfyUI nodes to streamline workflows: load multiple images via a multi-select dialog as a batch or list, or 
> L57: #### (Impact-Pack) Multiline Wildcard Text

## 星数曲线

```mermaid
xychart-beta
    title "vslinx/ComfyUI-vslinx-nodes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0a12b913c4b9` · [字段定义](../../DATASET.md)*
