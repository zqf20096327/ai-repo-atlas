# mc7yxyyq96-sketch/hi-code

⭐ 15 · JavaScript · MIT · 推送 2026-07-23 · [GitHub](https://github.com/mc7yxyyq96-sketch/hi-code) · 个人维护 · 中文 README

**本地优先的桌面编码 Agent 工作台，接入任意 OpenAI 兼容模型**

基于 Electron 桌面端与 Ink 终端 TUI 双前端的编码 Agent 工作台：模型通过多步工具调用（read/write/edit、bash、ripgrep 检索等）自主读写文件、执行命令、迭代完成任务，带流式输出、diff 预览与改动前权限确认。支持接入任意 /chat/completions 兼容服务（DeepSeek、Kimi、Qwen、Ollama、vLLM 等），内置多 Agent 团队编排、补丁竞技场、任务中心、MCP 客户端与商店。项目自述处于早期（v0.5.2），以 MIT 开源，另有独立闭源商业版（运行开源版不依赖）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多步工具调用 Agent 循环（单轮最多 50 步），带 diff 预览与权限确认
- Electron 桌面端 + 终端 TUI 双前端
- 多 Agent 团队 / 竞技场 / 任务中心等工程化工作台面板
- MCP 客户端、插件/技能商店与国内友好镜像源

## 适用场景

- 让 AI Agent 在本地仓库自主完成编码任务并审查 diff
- 并行编排多个专家 Agent（架构/编码/评审/测试）协作开发
- 用本地或任意 OpenAI 兼容模型驱动编码助手

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L11: **Hi Code 是一个本地优先的桌面编码 Agent 工作台**，对标 Codex / Claude Code 的使用体验，但面向国内环境从零打造：接入**任意 OpenAI 兼容模型**——Kimi、DeepSeek、通义千
> L13: 它不是一个套壳聊天框，而是一个**真正会干活的 Agent 循环**：模型自己读写文件、执行命令、搜索仓库、反复迭代直到任务完成——全程有流式输出、彩色 diff 预览，以及在改动你机器之前的**权限确认**。
> L32: - **桌面应用（Electron）**：聊天、工具时间线、可视化 diff、Git、模型设置、商店、插件、技能、MCP —— 一体化工作台

## 星数曲线

```mermaid
xychart-beta
    title "mc7yxyyq96-sketch/hi-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `d7b8bbb1ce83` · [字段定义](../../DATASET.md)*
