# shawnrushefsky/comfyui-mcp

⭐ 18 · TypeScript · MIT · 推送 2026-01-28 · [GitHub](https://github.com/shawnrushefsky/comfyui-mcp) · 个人维护

**让 Claude 等 AI 助手通过 MCP 操控 ComfyUI 生成图像/视频/音频**

连接 AI 助手与 ComfyUI 的 MCP（Model Context Protocol）服务器：Claude、Cursor、Windsurf、Cline 等 MCP 客户端可通过它发现节点、组装与校验工作流、执行生成任务，覆盖图像、视频（SVD/Mochi/LTX 等）、音频模型。提供 70+ 官方示例工作流模板与保存复用机制，支持从 PNG 提取工作流、按模型推荐工作流与参数。ComfyUI 未安装时也可引导安装与下载模型。通过 Docker 镜像或源码构建部署，需本机运行 ComfyUI 实例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 70+ 官方示例工作流（Flux/SDXL/SD3.5/ControlNet/视频/音频）
- 工作流优先架构：节点发现、构建、校验、模板保存复用
- 自动发现 ComfyUI 安装与可用模型，无需手动配置能力
- ComfyUI 未运行时提供安装引导与模型下载工具

## 适用场景

- 在 Claude Desktop 里用自然语言让 AI 生成图像/视频/音频
- 让 AI 助手组装和执行自定义 ComfyUI 工作流
- 管理 ComfyUI 生成队列（查看/取消/中断任务）
- 让 AI 引导完成 ComfyUI 安装与模型下载

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L7: An MCP (Model Context Protocol) server that enables AI assistants like Claude to interact with ComfyUI for generatin
> L24: This MCP server acts as a bridge between AI assistants and ComfyUI, the powerful node-based interface for Stable Di
> L45: All generation happens through `run_workflow`, giving you full control over the ComfyUI workflow. The server provid

## 星数曲线

```mermaid
xychart-beta
    title "shawnrushefsky/comfyui-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `d136a5f2e1df` · [字段定义](../../DATASET.md)*
