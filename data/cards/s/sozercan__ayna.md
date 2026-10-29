# sozercan/ayna

⭐ 34 · Swift · MIT · 推送 2026-08-15 · [GitHub](https://github.com/sozercan/ayna) · 个人维护

**Apple 平台的原生 agentic AI 聊天客户端（macOS/iOS/watchOS）**

基于 SwiftUI 构建的 Apple 原生多模型聊天客户端：支持 OpenAI、Anthropic、Azure OpenAI 及任何 OpenAI 兼容端点（含本地 Ollama），可同时向多个模型发送同一提示并排比较输出。内置 Apple Intelligence 端侧推理、MCP 工具、图像生成（gpt-image-1）、跨会话记忆与加密本地存储。安装提供 .dmg 下载与 Homebrew cask 两种方式；要求 macOS/iOS/watchOS 26.0 或更新，应用未公证需手动移除隔离属性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模型并行流式对话，逐模型对比输出
- 原生支持 OpenAI/Anthropic/Azure OpenAI 与 OpenAI 兼容端点（含 Ollama）
- Apple Intelligence 端侧推理与 MCP 工具支持
- 会话本地加密存储、API key 存于 Keychain、无遥测

## 适用场景

- 在 Mac/iPhone/Apple Watch 上同时使用多家 AI 模型对话
- 并排比较多个模型对同一提示的回答
- 通过自定义端点连接本地 Ollama 等本地模型
- 用 MCP 工具扩展 AI 的文件系统与命令执行能力

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: A native agentic AI client for macOS, iOS, and watchOS, built with SwiftUI.
> L18: - ☁️ **Multi-Provider**: Native support for OpenAI, Anthropic, and Azure OpenAI. Also works with any OpenAI-compati

## 星数曲线

```mermaid
xychart-beta
    title "sozercan/ayna 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-29 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6231d3ea8165` · [字段定义](../../DATASET.md)*
