# mobcat40/ComfyUI-PromptChain

⭐ 37 · Python · AGPL-3.0 · 推送 2026-06-30 · [GitHub](https://github.com/mobcat40/ComfyUI-PromptChain) · 个人维护

**ComfyUI 可视化提示词工程与图像迭代节点套件**

ComfyUI 自定义节点包，把提示词框变为结构化工作流：节点内代码编辑器、链式合并模式、wildcards、booru 自动补全与 Tag Builder 可视化标签组装；通过 CivitAI hash 指纹识别 checkpoint 并应用对应预设；内置浏览器 3D 姿态编辑器输出 OpenPose/Depth 控制图与逐角色轮廓遮罩，驱动区域提示词、区域重绘与放大；附带图层编辑器、生成画廊与资源浏览器。安装方式为克隆到 custom_nodes 目录后重启 ComfyUI，可选功能在首次使用时自动安装。README 声明为 Beta 早期公开版本，功能可能变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 节点内代码编辑器与 Chain/Randomize/Switch/Iterate 链式合并模式
- 3D Poser 浏览器姿态编辑，输出 OpenPose/Depth 控制图与逐角色遮罩
- 按 hash 在 CivitAI 指纹识别 checkpoint 并应用预设、就地换模型
- Tag Builder 可视化标签组装与角色库、Photoshop 式图层编辑器

## 适用场景

- 在 ComfyUI 中结构化编写与管理多角色生图提示词
- 用 3D 姿态编辑器控制人物构图并做区域重绘/放大
- 管理和复用保存的提示词片段、生成画廊与输出文件

## 场景标签

`提示工程` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L7: A prompt-authoring and image-iteration suite for ComfyUI. PromptChain turns the raw prompt box into a model-aware, s
> L91: To install, clone into your ComfyUI `custom_nodes` directory and restart ComfyUI:

## 星数曲线

```mermaid
xychart-beta
    title "mobcat40/ComfyUI-PromptChain 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24", "2026-10-25", "2026-10-27"]
    y-axis "stars" 33 --> 38
    line [34, 35, 36, 37, 37]
```

2026-10-18 34 → 2026-10-27 37（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `abc8cba3c629` · [字段定义](../../DATASET.md)*
