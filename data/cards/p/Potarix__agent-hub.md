# Potarix/agent-hub

⭐ 19 · HTML · MIT · 推送 2026-05-01 · [GitHub](https://github.com/Potarix/agent-hub) · [官网](https://agent-hub.tools) · 个人维护

**macOS 客户端：在一个原生窗口统一使用多个 AI agent CLI**

Electron 构建的 macOS 11+（Apple Silicon）原生应用，将 Claude Code、Codex、Hermes、OpenClaw 等 AI agent CLI 统一到一个键盘优先的聊天界面。本体不实现 agent，而是通过 stdio 在本地（node-pty）或 SSH 远程拉起各官方 CLI，解析工具调用与模型事件渲染为原生 UI。支持逐线程切换目标主机、细粒度权限（ask/acceptEdits/bypassPermissions）、斜杠命令模糊搜索、逐线程热切换模型、图片粘贴，以及 llama.cpp/vLLM 等 OpenAI 兼容端点（openai-compat provider）。零遥测，API key 存于 OS keychain。提供 .dmg 下载与源码构建两种安装方式，仅支持 macOS，Windows/Linux 未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 包装 claude/codex/hermes/openclaw 官方 CLI，本地（node-pty）或 SSH 远程运行，同 UI 同线程历史
- 逐线程细粒度权限模式与工具调用审批对话框（展示确切调用与参数）
- openai-compat provider 支持任意 OpenAI 兼容端点（llama.cpp、vLLM、Groq、Together）
- 通过 macOS Accessibility API 将 Claude Desktop / Codex Desktop 固定在窗口内容区

## 适用场景

- 在单一窗口中并行使用多个 AI agent CLI 线程
- 把 Mac 作为前端、通过 SSH 在远程主机上运行 agent
- 以可视化方式审批 agent 的工具调用、粘贴图片和拖入文件
- 在不同模型间逐线程热切换（claude-opus、gpt-5.5 等）

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L24: Agent Hub is an **open-source native macOS app** that unifies the AI agent CLIs you already use — **Claude Code** (
> L131: For each thread, Agent Hub spawns the provider's CLI (locally via `node-pty`, or remotely via `ssh`), captures std
> L37: - **Any OpenAI-compatible endpoint.** llama.cpp, vLLM, Groq, Together — use the `openai-compat` provider.

## 星数曲线

```mermaid
xychart-beta
    title "Potarix/agent-hub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bad9b4576d42` · [字段定义](../../DATASET.md)*
