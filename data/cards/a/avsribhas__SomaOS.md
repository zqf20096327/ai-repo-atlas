# avsribhas/SomaOS

⭐ 14 · Rust · MIT · 推送 2026-05-23 · [GitHub](https://github.com/avsribhas/SomaOS) · 个人维护

**AI 与人类同为一级用户的 AI 原生操作系统**

基于 Rust 与 Buildroot 构建的 Linux 操作系统镜像，含自研 DRM/KMS 合成器、macOS 风格桌面、浮动窗口与 Dock。核心机制：桌面 Agent 模式下 AI 通过 IPC 接管桌面（开/关窗口、输入、操控浏览器），40+ 内建能力跨 13 个模块，支持多 LLM 提供商热切换、HITL 人工审批门、私有模式、工作流学习与自我改进循环（agent 提议新能力、人审批）。限制：当前为 v2.0，面向 x86_64/ARM64，视觉能力依赖 Ollama qwen2.5-vl:7b。

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

- 桌面 Agent 模式：AI 经 IPC 操控窗口/输入/浏览器，人可随时经 HITL 中断
- agent daemon 含 40+ 内建能力（13 模块），支持用户自定义能力热加载
- soma-substrate 实现 6 项 orientation-aligned AI 安全属性（状态快照、动作分级、一致性校验）
- 自研 DRM/KMS 合成器直渲 GPU 帧缓冲，无需 X11/Wayland

## 适用场景

- 让 AI agent 与人共享同一桌面并行操作应用
- 观察 agent 桌面操作并通过 HITL 审批高风险动作
- 在私有模式下使用 agent 而不记录会话学习数据

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5:  An AI-Native Operating System Built from the Ground Up for Autonomous Agents
> L40: - A **desktop agent mode** — the AI can take full control of the desktop (open/close/focus windows, type text, driv
> L52: - **Multi-provider LLM** (Ollama, Anthropic, OpenAI, Gemini) with native tool calling; provider and model hot-swapp

## 星数曲线

```mermaid
xychart-beta
    title "avsribhas/SomaOS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c94d68bbd36c` · [字段定义](../../DATASET.md)*
