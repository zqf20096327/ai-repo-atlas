# enkei0x/espai

⭐ 19 · C++ · MIT · 推送 2026-02-23 · [GitHub](https://github.com/enkei0x/espai) · 个人维护

**面向 ESP32/Arduino 的统一 AI API 客户端库**

C++17 编写的 Arduino/PlatformIO 库，让 ESP32 系列开发板通过单一统一接口接入 OpenAI、Anthropic Claude、Google Gemini、Ollama 及任意 OpenAI 兼容 API。提供 SSE 流式输出、统一 schema 的工具调用（function calling）、多轮对话历史与自动裁剪、FreeRTOS 异步非阻塞请求、指数退避自动重试，并内嵌根 CA 证书做 TLS 校验。针对受限内存优化，可用宏关闭未用 provider 节省 flash。给嵌入式/IoT 开发者构建语音助手、智能设备等 AI 应用使用。

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

- 单一统一接口接入 OpenAI/Claude/Gemini/Ollama 及 OpenAI 兼容 API
- 流式输出、工具调用、多轮对话历史（自动裁剪）
- FreeRTOS 异步非阻塞请求与指数退避自动重试
- 内嵌根 CA 证书的 TLS 校验，451+ 原生单元测试

## 适用场景

- 在 ESP32 智能硬件上接入 GPT/Claude/Gemini 做对话交互
- 通过 Ollama 在本地离线运行 LLM，无需 API key
- IoT 语音助手、AI 小工具等嵌入式 AI 项目开发

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L14: ESPAI is a lightweight, easy-to-use Arduino library that lets you integrate OpenAI, Anthropic, Google Gemini and Ol
> L30: - 🔄 **Multiple Providers** — OpenAI, Anthropic (Claude), Google Gemini, Ollama and any OpenAI-compatible API throug

## 星数曲线

```mermaid
xychart-beta
    title "enkei0x/espai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-29 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2eef1596af15` · [字段定义](../../DATASET.md)*
