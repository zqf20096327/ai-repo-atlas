# mrmendoza-dev/offline-chatbot

⭐ 15 · TypeScript · MIT · 推送 2026-03-18 · [GitHub](https://github.com/mrmendoza-dev/offline-chatbot) · [官网](https://offline-chatbot.netlify.app/) · 个人维护

**离线本地 AI 聊天界面：Ollama/WebLLM 双后端免费私用**

本地运行的 ChatGPT 风格聊天界面，支持两种模型后端：Ollama（服务器端本地推理，Express.js 后端封装 Ollama API）与 WebLLM（浏览器内直接加载模型，首次使用时下载）。初始配置后完全离线运行，支持流式输出、多模型切换、上传 TXT/代码/PDF 讨论及视觉模型图片分析。前端为 React 19 + TypeScript + Vite，以 git clone + npm 安装运行，支持 PWA 安装为桌面应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ollama 与 WebLLM 双后端，初始配置后完全离线
- 文件上传分析（TXT/CSV/PDF/代码）与视觉模型图片分析
- 应用内屏幕截图功能
- PWA 支持：可安装为桌面应用

## 适用场景

- 无网络环境下本地与开源 LLM 对话
- 用本机模型讨论上传的文档、代码与图片
- 以桌面应用形式离线使用私有 AI 聊天

## 场景标签

`聊天机器人` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L2: This project is created with the goal of providing a local AI chatbot interface that works offline, and is completel
> L3: Chat with AI models locally using either **Ollama** (server-based) or **WebLLM** (browser-based) without requiring i
> L13: - **Dual Provider System**: Choose between Ollama (powerful server models) or WebLLM (instant browser models)

## 星数曲线

```mermaid
xychart-beta
    title "mrmendoza-dev/offline-chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8aea53648492` · [字段定义](../../DATASET.md)*
