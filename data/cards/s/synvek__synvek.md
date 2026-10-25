# synvek/synvek

⭐ 81 · TypeScript · AGPL-3.0 · 推送 2026-06-29 · [GitHub](https://github.com/synvek/synvek) · [官网](https://www.synvek.com) · 个人维护

**本地运行与管理多模态 LLM 的桌面 GUI 应用**

基于 Rust/Tauri/Deno 的桌面应用，本地管理并运行大模型：GUI 内点击下载与运行模型，支持多模型同会话聊天、文生图、视频生成与语音输出，底层调用 llama.cpp、stable-diffusion.cpp、Mistral.rs、Candle 等运行时，无需 Python/Node/Docker/WSL。支持 CUDA/Vulkan/Metal GPU 加速，内嵌 Deno 可用 TypeScript/JavaScript 编写插件与 MCP server。项目自述处于活跃开发期、API 可能破坏性变更。支持 Windows/macOS/Linux(Ubuntu)。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- GUI 内点击下载并运行本地模型，无需命令行工具
- 单一会话中混用多个模型：聊天、图像生成、视频生成、语音输出
- 内嵌 Deno 扩展机制，用 TypeScript/JavaScript 写插件、Function call 与 MCP server
- CUDA/Vulkan/Metal GPU 加速

## 适用场景

- 在桌面上一站式下载、管理和对话本地 LLM
- 同一会话里混用文本、图像、视频、语音多种本地模型
- 本地跑 Stable Diffusion / Flux 系列生成图像而不装 Python 环境

## 场景标签

`聊天机器人` `图像生成` `视频生成` `多模态` · 领域:对话与助手

## 证据(README 行号)

> L3: Synvek is all-in-one GUI application to manage & run & explore LLM with text, image and voice locally.
> L5: It is powered by Rust & Deno & Tauri & llama.cpp/stable-diffusion.cpp/Mistral.rs/Candle. It can run & chat with loca

## 星数曲线

```mermaid
xychart-beta
    title "synvek/synvek 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 80 --> 82
    line [81, 81]
```

2026-10-18 81 → 2026-10-25 81（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `780006b498eb` · [字段定义](../../DATASET.md)*
