# ggml-org/Llama-macOS

⭐ 1,659 · Swift · MIT · 推送 2026-10-20 · [GitHub](https://github.com/ggml-org/Llama-macOS) · [官网](https://llama.app) · 组织维护

**macOS 菜单栏应用：本地运行 LLM 并提供 OpenAI 风格 API**

面向 macOS 用户的本地 LLM 运行应用：基于 llama.cpp 在本机启动服务器（http://localhost:9931/v1），自动配置模型参数并按需加载/卸载以节省内存。支持安装任意 Hugging Face GGUF 模型、推荐适配硬件的模型，模型存于 Hugging Face 缓存与 llama.cpp 共享。内置 WebUI 聊天，可接入编码代理、编辑器等应用，支持通过 models.user.ini 自定义 llama serve 参数，以及 Tailscale/局域网网络访问选项。仅限 macOS，通过 brew cask 或 Releases 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本机运行 LLM 并暴露 OpenAI 风格 API（localhost:9931/v1）
- 基于 llama.cpp，模型存于 Hugging Face 缓存，与 llama.cpp 共享
- 按硬件自动配置模型参数，模型按需加载、空闲时卸载
- models.user.ini 自定义 llama serve 参数与网络访问（Tailscale/局域网）

## 适用场景

- 在 Mac 上本地运行 LLM 并通过 API 供其他应用调用
- 通过内置 WebUI 与本地模型对话
- 让编码代理、编辑器等工具接入本地模型服务

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L19: When you start Llama, it runs a local server at `http://localhost:9931/v1`.
> L21: If you have llama.cpp installed, Llama uses it. Otherwise, it installs a prebuilt binary for your Mac. Models you'v
> L23: You can chat with any model in the built-in WebUI, connect other apps (coding agents, chat UIs, editors), or use th

## 星数曲线

```mermaid
xychart-beta
    title "ggml-org/Llama-macOS 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 1637 --> 1661
    line [1639, 1658, 1659]
```

2026-10-18 1,639 → 2026-10-22 1,659（+20）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `cad60ce5e215` · [字段定义](../../DATASET.md)*
