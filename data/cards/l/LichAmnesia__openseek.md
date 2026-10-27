# LichAmnesia/openseek

⭐ 209 · TypeScript · MIT · 推送 2026-08-04 · [GitHub](https://github.com/LichAmnesia/openseek) · [官网](https://openseek.dev/) · 个人维护 · 中文 README

**开源 TUI 编程 agent：多提供商路由、MCP/LSP、三种自治模式**

基于 Bun 的终端 AI 编程助手，内置 28 个提供商（OpenAI 兼容、Anthropic 协议、Google、本地 Ollama 等）并支持 BYOK。提供 50+ 工具与 100+ slash 命令，Plan/Agent/YOLO 三种模式对应只读规划、确认执行与完全自治；集成 MCP 客户端（stdio/SSE/websocket）与 LSP 内联诊断，另有 headless HTTP/SSE 运行时 API 供 IDE 与 CI 使用，并带每模型实时花费跟踪。运行要求 Bun ≥ 1.3（必需），macOS/Linux，Windows 需 WSL2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 28 个内置提供商，覆盖 OpenAI 兼容/Anthropic 协议/Google/本地（Ollama、自定义）
- Plan / Agent / YOLO 三级自治模式
- MCP 客户端（stdio/SSE/websocket）与 LSP 内联诊断（tsserver、rust-analyzer 等）
- headless HTTP/SSE 运行时 API（openseek serve --http）与实时费用计量

## 适用场景

- 在终端用自然语言驱动代码编辑、shell 与搜索等 50+ 工具
- 从只读规划到完全自治分阶段控制 agent 行为
- 通过自有 API key 接入多家模型提供商并跟踪花费
- 作为 headless 服务接入 IDE 或 CI 流程

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: ### Open-source TUI coding agent — multi-provider, MCP, LSP, Plan/Agent/YOLO modes
> L24: Modern AI coding tools — Claude Code, Codex, Cursor — are great but closed-source and lock you to specific provider
> L26: - **28 built-in providers** — OpenAI-compat (Mikan, DeepSeek, OpenRouter, Groq, Fireworks, NVIDIA NIM, Together, Ce

## 星数曲线

```mermaid
xychart-beta
    title "LichAmnesia/openseek 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 208 --> 210
    line [209, 209]
```

2026-10-18 209 → 2026-10-27 209（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1a895bc575c1` · [字段定义](../../DATASET.md)*
