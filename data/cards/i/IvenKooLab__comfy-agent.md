# IvenKooLab/comfy-agent

⭐ 30 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/IvenKooLab/comfy-agent) · [官网](https://github.com/IvenKooLab/comfy-agent/releases/latest) · 组织维护 · 中文 README

**ComfyUI 本地桌面工作台：创作、模板、模型管理与短剧批量流水线**

面向本地 ComfyUI 用户的零依赖桌面客户端（约 10MB exe，纯 Python 标准库后端 + 原生 JS 前端）：集成文生图/文生图视频创作（Flux、MiniMax H3）、600+ 官方模板、可视化 SVG 工作流编辑器、支持断点续传的模型管理器、角色 LoRA 绑定、分集短剧批量流水线（剧本→分镜→批量队列→拼接 BGM），并内置 MCP server（stdio + JSON-RPC 2.0）供外部 agent 调用。需本地运行 ComfyUI（默认 127.0.0.1:8188）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 600+ ComfyUI 官方模板预览与一键载入
- 角色 LoRA 绑定与分集短剧批量流水线
- 模型预设套件一键断点续传下载
- 内置零依赖 MCP server，可被 Claude Desktop/Cursor 等调用

## 适用场景

- 用桌面窗口管理本地 ComfyUI 的生成、队列与模型
- 制作分集短剧：剧本到分镜到批量出片
- 通过 MCP 让外部 agent 驱动 ComfyUI 工作流

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L14: One native window that runs your local ComfyUI end to end: prompt-to-image/video creation, a gallery, a visual work
> L36: - 🔌 **MCP Server** — expose ComfyAgent to any MCP host (see below)

## 星数曲线

```mermaid
xychart-beta
    title "IvenKooLab/comfy-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-28 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7561243f27fc` · [字段定义](../../DATASET.md)*
