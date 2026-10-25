# ImDarkTom/LlamaPen

⭐ 451 · Vue · AGPL-3.0 · 推送 2026-09-09 · [GitHub](https://github.com/ImDarkTom/LlamaPen) · [官网](https://llamapen.app) · 个人维护

**本地 LLM 提供方的免安装 Web 聊天界面**

面向在自有硬件上运行模型的用户，提供基于浏览器的聊天 GUI，兼容 Ollama（默认预配置）、llama.cpp、LM Studio、Jan、vLLM 及任意 OpenAI 兼容服务，支持一键预设与手动添加多个提供方并切换。聊天记录存储在浏览器本地（IndexedDB/Dexie 技术栈），离线可用并支持 PWA。功能包括 Markdown/思考过程/LaTeX 渲染、自定义工具调用、内置模型与下载管理。可免安装使用，本地运行提供 Docker 镜像或 Bun 源码方式；曾提供的 LlamaPen Cloud 云服务已停止。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 兼容 Ollama/llama.cpp/LM Studio/Jan/vLLM 及任意 OpenAI 兼容服务
- 聊天记录本地存储于浏览器，离线与 PWA 支持
- 渲染 Markdown、思考文本与 LaTeX 数学，支持自定义工具调用
- 内置模型与下载管理器

## 适用场景

- 给本地 Ollama 等模型找一个免安装的聊天界面
- 在桌面和移动浏览器中访问自托管 LLM 服务
- 同时配置多个模型提供方并随时切换

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: A no-install needed GUI for Ollama and other local LLM providers.
> L11: - 🧩 Works with Ollama, llama.cpp, LM Studio, Jan, vLLM, and any OpenAI-compatible server.
> L27: LlamaPen is built for models running on your own hardware. Ollama is pre-configured, and one-click presets are incl

## 星数曲线

```mermaid
xychart-beta
    title "ImDarkTom/LlamaPen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 450 --> 452
    line [451, 451]
```

2026-10-18 451 → 2026-10-25 451（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `2002ae3193c3` · [字段定义](../../DATASET.md)*
