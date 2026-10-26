# RioShiina47/comfy-webui

⭐ 116 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/RioShiina47/comfy-webui) · [官网](https://huggingface.co/spaces/RioShiina/ImageGen) · 个人维护

**把 ComfyUI 工作流封装为 Gradio UI、语义 API 与 MCP 工具的平台**

基于 Gradio 构建的 ComfyUI 前端与 Workflow-as-a-Service 平台，通过动态工作流组装 API 与 ComfyUI 后端解耦通信。图像生成采用矩阵式动态工作流机制（任务维度×模型维度），支持 LoRA/ControlNet/IP-Adapter 等链式注入，并覆盖视频、音频、3D 生成与跨模态编辑。面向开发者与 AI Agent，将多节点工作流暴露为高层语义 API 与 MCP 工具（含 8 个 ImageGen 工具与全模态工具集），降低 LLM 直接编排节点的复杂度。项目自述处于活跃开发期，模型库主要用于测试；设计面向可信局域网，公开互联网暴露需自行加固。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 矩阵式动态工作流：任务维度与模型维度自由组合，支持数十种基础生成模式
- 高层语义 API/MCP 将多节点工作流封装为可调用函数，供 LLM 与 Agent 接入
- 图像生成 8 个语义工具与渐进式探索管线（发现任务→筛选架构→执行→异步轮询）
- 覆盖图像、视频（MiniMax-H3/LTX-2.5/Wan 等）、音频（Music-3）、3D（Hunyuan3D-2/TRELLIS）与跨模态编辑

## 适用场景

- 在统一界面中组合多模型与多注入链完成图像/视频/3D 生成
- 让支持 MCP 的 LLM 或 AI Agent 直接调用复杂工作流做自动化生成
- 把 ComfyUI 工作流封装为高层 API 供外部系统集成

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L44:  - The platform exposes complex multi-node workflows as standardized high-level functions via Gradio native APIs an
> L45:  - Any LLM or AI Agent supporting the MCP protocol can directly interface with the service for end-to-end full-moda
> L50:  - **Intent-Driven Orchestration:** Frees AI agents from being "node wirers", allowing them to focus purely on high

## 星数曲线

```mermaid
xychart-beta
    title "RioShiina47/comfy-webui 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 114 --> 121
    line [120, 115, 116]
```

2026-10-18 120 → 2026-10-26 116（-4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `c37a14484e0b` · [字段定义](../../DATASET.md)*
