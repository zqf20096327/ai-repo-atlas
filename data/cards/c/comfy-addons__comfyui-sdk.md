# comfy-addons/comfyui-sdk

⭐ 267 · TypeScript · MIT · 推送 2026-04-09 · [GitHub](https://github.com/comfy-addons/comfyui-sdk) · 个人维护

**面向开发者的 ComfyUI API TypeScript SDK 与工作流 CLI**

TypeScript 编写的 ComfyUI API 交互 SDK：提供 ComfyApi 客户端、流式 PromptBuilder 工作流构建器、ComfyPool 多实例管理与 WebSocket 实时进度跟踪，支持 Basic/Bearer/自定义认证及自定义 WebSocket 实现（含 HTTP 轮询回退）。附带 CLI 工具 cfli，可从终端直接执行 workflow JSON、覆盖输入参数、下载产出图片，并能根据服务器节点定义 codegen 生成类型化 WorkflowBuilder。面向需要以编程方式接入 ComfyUI 生成管线的前端/Node 开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ComfyApi 客户端覆盖队列、历史、模型列表、上传、用户数据等 ComfyUI API 方法
- cfli CLI 可从终端执行 workflow 并覆盖输入参数、下载产出图片
- cfli codegen 从服务器节点定义生成类型化 WorkflowBuilder
- ComfyPool 多实例管理与可配置队列策略

## 适用场景

- 在 Node/前端项目中程序化构建并执行 ComfyUI 生成工作流
- 用 CLI 快速批处理 workflow JSON 并下载产出图片
- 管理多个 ComfyUI 实例池并做任务分发

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L8: A robust and meticulously crafted TypeScript SDK 🚀 for seamless interaction with the ComfyUI API. This SDK significa
> L32: bun add @saintno/comfyui-sdk

## 星数曲线

```mermaid
xychart-beta
    title "comfy-addons/comfyui-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 266 --> 268
    line [267, 267]
```

2026-10-18 267 → 2026-10-31 267（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `fce2852b7ccf` · [字段定义](../../DATASET.md)*
