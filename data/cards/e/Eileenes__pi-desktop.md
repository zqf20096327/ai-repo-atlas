# Eileenes/pi-desktop

⭐ 27 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/Eileenes/pi-desktop) · [官网](https://eileenes.github.io/pi-desktop/) · 个人维护 · 中文 README

**基于 Pi 的 Electron 桌面编程代理客户端**

基于 Pi 的独立 Electron 桌面客户端，在一个窗口中集成项目浏览、与模型流式对话、文件预览、Git 变更/Worktree 管理、内嵌终端（xterm.js + node-pty）以及 Skills/Plugins 的搜索安装启停。代理运行时使用 npm 发布的 @earendil-works/pi-coding-agent，无需本地 Pi 源码。应用不附带模型账号或 API 额度，模型由用户自行配置供应商与认证。提供三级会话权限模式、工作区信任与进程隔离等安全机制；macOS/Windows/Linux 提供安装包。

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

- 内嵌终端（xterm.js + node-pty）与 Git/Worktree 管理
- Skills 与 Plugins 的搜索、安装、启停与更新
- 三级权限模式（ask/autoEdit/full）与工作区信任机制
- 应用内检查、下载并应用更新（AppImage）

## 适用场景

- 在一个桌面窗口中打开本地项目并让 AI 代理执行编程任务
- 逐项审批代理的工具调用，控制其操作范围
- 通过界面管理模型供应商、Skills 与 Plugins

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: 基于 Pi 的独立 Electron 桌面客户端：打开本地项目，与模型对话，查看文件、运行工具、管理 Git 与终端。
> L24: 桌面界面提供中英文、明暗主题、自定义 CSS、系统托盘与窗口状态恢复。代理运行时使用 npm 发布的 `@earendil-works/pi-coding-agent`，无需克隆或映射本地 Pi 源码。
> L131: Development requires Node.js 22.19.0 or later. Run `npm ci` and `npm run start`; use `npm run check` for build/typ


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `36da94936e43` · [字段定义](../../DATASET.md)*
