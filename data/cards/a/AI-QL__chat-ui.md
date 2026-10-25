# AI-QL/chat-ui

⭐ 97 · HTML · Apache-2.0 · 推送 2026-08-19 · [GitHub](https://github.com/AI-QL/chat-ui) · [官网](https://chat.aiql.com) · 组织维护

**单 HTML 文件的多模态聊天机器人前端界面**

用一个 HTML 文件构建完整聊天机器人前端界面，供开发者快速搭建和测试聊天界面。支持 OpenAI 格式请求，兼容 HuggingFace TGI、vLLM 等后端，自动适配 OpenAI、Cloudflare AI 与纯文本多种响应格式；支持自定义后端端点、图像多模态输入、聊天记录下载、中断与重复生成、Markdown 显示、i18n，并可作为 MCP 渲染器通过 IPC 与桌面后端主进程交互。提供在线 demo、本地打开、Python/Cloudflare Pages/Docker/HuggingFace/K8s 等多种部署方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 HTML 文件实现完整聊天前端，OpenAI 格式请求兼容 TGI/vLLM 等后端
- 自动适配 OpenAI、Cloudflare AI 与纯文本多种响应格式
- 支持 MCP：作为渲染器经 IPC 与桌面后端主进程交互
- 多模态图像输入、聊天记录下载、中断/重复生成、i18n

## 适用场景

- 为任意 OpenAI 格式后端快速配一个通用聊天前端
- 测试后端推理能力（中断生成、重复生成、下载记录）
- 以 Docker/Cloudflare Pages/K8s sidecar 等方式自部署聊天界面

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L8: This repository aims to construct the entire front-end UI using a single HTML file, aiming for a minimalist approach
> L18: - Support various `backend endpoints through custom configurations`, providing any project with a universal fronten

## 星数曲线

```mermaid
xychart-beta
    title "AI-QL/chat-ui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-25 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `07e7db835967` · [字段定义](../../DATASET.md)*
