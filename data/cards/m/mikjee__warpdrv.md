# mikjee/warpdrv

⭐ 141 · TypeScript · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/mikjee/warpdrv) · 个人维护

**本地 LLM 服务器管理与聊天工具箱：管理 llama.cpp 后端并对话**

Tauri 桌面应用（Rust 壳 + Node.js 服务端 + React 前端），用于启动和管理 llama-server 实例，支持全参数控制、KV 缓存检查点、推测解码与自定义编译后端；提供 OpenAI 兼容代理端点供其他聊天应用接入，内置聊天 UI、Whisper STT / Kokoro TTS 语音模式、内置 MCP 服务器与 RAG 工作区。自带 llama-server 二进制，可从 Hugging Face 浏览下载 GGUF 模型。面向本地 AI 使用者与 llama.cpp 调试者，当前为 Alpha 版，macOS 需自行编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 带任意自定义 llama.cpp 构建的 llama-server 实例管理与参数控制
- OpenAI 兼容代理端点，支持别名路由与鉴权
- Whisper STT + Kokoro TTS 语音对话模式
- 内置 MCP 服务器、RAG 工作区与子代理并行任务

## 适用场景

- 在一处启动并切换多个本地模型后端，测试不同 llama.cpp 构建
- 通过 OpenAI 兼容代理让现有聊天/编码工具接入本地模型
- 用带语音输入输出与工具调用的界面直接与本地模型对话

## 场景标签

`AI 助手` `RAG` `模型网关` `语音 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L33: **warpdrv** is a desktop toolkit for using local LLMs.
> L70: **Server management.** Launch llama-server instances with full parameter control, including cache checkpointing, sp
> L72: **Proxy.** An OpenAI-compatible endpoint proxy lets any chat app talk to your running servers. Server aliases route

## 星数曲线

```mermaid
xychart-beta
    title "mikjee/warpdrv 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 140 --> 142
    line [141, 141]
```

2026-10-18 141 → 2026-10-29 141（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6ee921b0a1c9` · [字段定义](../../DATASET.md)*
