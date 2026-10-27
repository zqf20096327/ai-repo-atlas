# wannaphong/android-hostai

⭐ 35 · Kotlin · Apache-2.0 · 推送 2026-09-15 · [GitHub](https://github.com/wannaphong/android-hostai) · [官网](http://github.wannaphong.com/android-hostai/) · 个人维护

**Android 应用：在手机上用 LiteRT-LM 托管 OpenAI 兼容 API 服务器**

原生 Android 应用（Material Design UI），基于 LiteRT-LM 在手机上运行 LLM 推理，并通过前台服务对外提供 OpenAI 兼容的 HTTP API（/v1/chat/completions 等，支持流式、token 统计、多模态图像与音频输入）。支持可选 API Key 认证、CORS、聊天记录持久化存储，内置 Web 聊天界面。加载 .litertlm 模型文件（如 Gemma3-1B、Phi-4-mini、Qwen2.5-1.5B），GPU 加速并带 CPU 回退。README 声明仍处于 alpha 阶段。面向希望在局域网内将 Android 设备作为 LLM 服务端的用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI 兼容端点，含流式与多模态（图像/音频）输入
- 基于 LiteRT-LM 的移动端推理，GPU 加速与 CPU 回退
- 内置 Web 聊天界面与聊天记录持久化存储
- 可选 API Key 认证与 CORS 支持

## 适用场景

- 把旧 Android 手机变成局域网内的 LLM API 服务器
- 用 OpenAI 客户端库（Python/Node.js/curl）直接访问手机上的模型
- 在浏览器中通过 Web 聊天界面与本地模型对话

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: An Android application that uses LiteRT-LM to host an OpenAI-compatible API server, allowing you to run LLM models o
> L9: - 🚀 OpenAI-compatible API endpoints
> L173: - **OpenAIApiServer** - Javalin-based web server with OpenAI-compatible endpoints and SSE streaming support

## 星数曲线

```mermaid
xychart-beta
    title "wannaphong/android-hostai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-27 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `45bf941e84f2` · [字段定义](../../DATASET.md)*
