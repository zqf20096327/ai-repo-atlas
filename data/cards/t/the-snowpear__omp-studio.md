# the-snowpear/omp-studio

⭐ 221 · TypeScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/the-snowpear/omp-studio) · 组织维护 · 中文 README

**oh-my-pi AI 编码 Agent 的跨平台桌面 GUI 工作台**

基于 Electron 与 React 的桌面应用，为 oh-my-pi（omp）编码 Agent 提供图形外壳与可编排工作台：多会话并行对话、子 Agent 管理、审批流、Git/Worktree、终端、托管浏览器、Computer Use、MCP/Skills 配置与 SSH/WSL 工作区集中在一处，通过类型化 Studio Bridge 直连 Runtime，不解析 TUI 文本。窗口支持拖拽浮动、吸附分屏与钉为独立系统窗口。模型与登录沿用 OMP 的 models.yml/omp login，仓库不内置供应商密钥。提供 Windows/macOS/Linux 安装包，也可从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话与工具可拖拽浮动、吸附分屏或钉成独立系统窗口，布局重启后恢复
- 通过类型化 Studio Bridge 调用 Runtime，Renderer 拿不到 token 与进程句柄
- Agent Hub 集中查看主/子 Agent 状态、Token 用量与花费，支持按子代理设置账号策略
- 统一模型配置页管理 Anthropic、OpenAI、OpenRouter、本地 LM Studio 等供应商

## 适用场景

- 在图形界面同时运行多场编码 Agent 对话并分屏管理
- 审批 Agent 的计划与命令，查看每次文件变化与 Git 提交
- 通过 SSH 或 WSL 2 在远程/其他系统环境中运行 Agent
- 接入本地 LM Studio 等供应商在本地运行编码 Agent

## 场景标签

`GUI 自动化` `编码 Agent` · 领域:效率与自动化

## 证据(README 行号)

> L24: **OMP Studio** 是 oh-my-pi（`omp`）AI Coding Agent 的跨平台桌面 GUI 与可视化工作台（支持 Windows、macOS 与 Linux）。它基于 Electron 与 React，将
> L133: Anthropic、OpenAI、OpenRouter、本地 LM Studio 等供应商在同一页管理开关、端点和 <code>modelProviderOrder</code>；在角色页为 <code>@default</co


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `a369cef9391d` · [字段定义](../../DATASET.md)*
