# zwaetschge/plum-code-webui

⭐ 28 · TypeScript · MIT · 推送 2026-10-03 · [GitHub](https://github.com/zwaetschge/plum-code-webui) · 个人维护

**自托管的多 CLI 编码 agent Web 控制台（含原生 Android 客户端）**

面向使用 Codex、OpenCode、Pi、Kimi Code 与 Claude Code CLI 的开发者的自托管控制中心：单个 Docker 部署内提供流式聊天、工具审批与执行追踪、多会话管理、文件浏览与 Monaco 编辑器、Git/GitHub 集成、按 provider 的 token 用量与分析账本，以及 ComfyUI 图像生成等内置 MCP 服务器（android-builder、godot、blender）。另提供 Kotlin/Jetpack Compose 原生 Android 客户端（支持平板与 Wear OS，可从手表审批工具调用）。默认 provider 为 Codex，Claude Code 保留为 legacy 选项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一接入 5 种编码 CLI（Codex/OpenCode/Pi/Kimi Code/Claude Code），按会话切换 provider
- 工具执行时间线、context 用量指示、token/spend 分析账本
- 内置 MCP 服务器：ComfyUI 图像生成、Android 构建、Godot、Blender
- 原生 Android 客户端（手机/平板/Wear OS），离线消息队列与手表端审批

## 适用场景

- 在浏览器或手机上统一管理多个编码 agent 的会话与审批
- 自托管一个带用量分析与 git/GitHub 集成的编码工作台
- 团队通过邮箱白名单和角色管理共享一个编码 agent 界面

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Self-hosted control center for Codex, OpenCode, Pi, Kimi Code, and Claude Code — with **two first-class clients**: a
> L72: - **Codex** (OpenAI) - **default provider**, per-turn `codex exec` process model with auto-respawn, chunk-level str

## 星数曲线

```mermaid
xychart-beta
    title "zwaetschge/plum-code-webui 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-28 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `aadb6878e19c` · [字段定义](../../DATASET.md)*
