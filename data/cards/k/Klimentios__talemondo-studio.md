# Klimentios/talemondo-studio

⭐ 3 · Python · NOASSERTION · 推送 2026-11-08 · [GitHub](https://github.com/Klimentios/talemondo-studio) · [官网](https://github.com/Klimentios/Klimentios/blob/main/writing/talemondo-studio.md) · 个人维护

**面向创作者的本地 AI 电影制作工作台（MiniMax H3）**

TaleMondo Studio 是运行在 Mac 上的 AI 视频制作工作区，覆盖创意简报、世界观、角色参考库、场景与镜头规划、GPU 渲染队列、成片审看与剪辑导出。文档化生成路径是通过 ComfyUI 在 NVIDIA GPU 上运行 MiniMax H3；可导入自定义 ComfyUI 图作为表单、REST 端点和 MCP agent 工具（供 Claude Code、Codex 调用）。安装脚本会配置 Python、ffmpeg 与本地服务。渲染需 96 GB VRAM GPU 与 256 GB 内存；代码采用 PolyForm Noncommercial 许可，商用需作者书面许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 参考库→故事世界→场景镜头→GPU 队列→审看→剪辑的一体化制作流程
- 导入 ComfyUI 图生成可复用表单、REST 端点与 MCP agent 工具
- 结构化镜头导演：景别、运镜、灯光、色彩等预设编译进 ComfyUI 图
- 英/俄双语界面与剪辑导出（Premiere Pro、DaVinci Resolve、Final Cut Pro）

## 适用场景

- 在我的 Mac 上规划分镜并在 GPU 服务器上批量生成视频
- 用 Claude Code 等 agent 跨阶段驱动镜头起草与渲染排队
- 用角色替换和世界更换工作流改编已有视频素材
- 把生成的片段导出到专业剪辑软件成片

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L5: **TaleMondo Studio is an AI film production studio for MiniMax H3.** It brings the creative brief, franchise world, 
> L7: The documented generation route runs H3 through ComfyUI on your NVIDIA GPU. Studio also imports custom ComfyUI graph
> L53: - **Render and review:** Queue generation on your GPU, inspect the resulting MP4, compare takes, and approve or rej


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `37882a2fad41` · [字段定义](../../DATASET.md)*
