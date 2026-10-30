# bharat2808/codex-universal-proxy

⭐ 18 · JavaScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/bharat2808/codex-universal-proxy) · [官网](https://www.npmjs.com/package/codex-ollama-proxy) · 个人维护

**让 Codex 使用任意 OpenAI 兼容模型的本地代理**

本地运行的代理服务：将 Codex 的 Responses API 流量转译为各供应商兼容的函数调用格式，再把响应转回 Codex 期望的格式，从而让 Codex 接入 Ollama、OpenRouter、Anthropic、Google、NVIDIA、DeepSeek 等供应商及任意 OpenAI 兼容端点，同时保留 Codex 插件、MCP 工具、tool_search 与 apply_patch。通过 npm 全局安装，提供 preset 配置、跨平台后台服务（launchd/systemd/Task Scheduler）、图像生成与本地语音（Whisper/Kokoro，均随包分发）能力。项目自称非官方且实验性，Codex 工具格式可能随版本变化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 转译 Codex 工具格式为供应商兼容函数调用并转回
- 内置十余个供应商 profile 与自定义 OpenAI 兼容端点支持
- preset 机制保存端点/模型/API key/适配器配置并按名启动
- 自带 FFmpeg、Whisper、Kokoro 的本地语音管线，无需系统依赖

## 适用场景

- 用本地 Ollama 模型驱动 Codex 编码助手
- 切换 OpenRouter 等聚合供应商访问多种模型
- 为 Codex 配置独立的文本模型与图像生成模型
- 在 Codex 中使用本地语音对话并按需转交编码任务

## 场景标签

`模型网关` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L13: The proxy runs locally, translates Codex-specific tool formats into provider-compatible function calls, and convert
> L21: * Google AI Studio and Vertex AI
> L33: Custom providers are also supported when they expose an OpenAI-compatible Responses API or

## 星数曲线

```mermaid
xychart-beta
    title "bharat2808/codex-universal-proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `68bc4205e8de` · [字段定义](../../DATASET.md)*
