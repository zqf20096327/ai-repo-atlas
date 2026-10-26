# tony3liu/eido

⭐ 145 · Rust · GPL-3.0 · 推送 2026-10-16 · [GitHub](https://github.com/tony3liu/eido) · [官网](https://cairno.cn/eido/) · 个人维护 · 中文 README

**macOS AI 编码工作台：对话、编辑、审查与浏览器/桌面操作一体**

基于 Zed 编辑器与 pi coding agent 构建的 macOS 桌面应用（0.0.1 首个稳定通道版本），将 AI 对话与代码编辑放在同一工作区：用 @ 引入代码上下文下达任务，agent 调查并提出修改，用户在原生审查界面决定接受或拒绝。提供 Workbench/Code/Split 三种视图、任务历史与恢复、Ask Before Actions 与 Full Access 两种全局权限控制，并捆绑 pi 1.3.0。浏览器代理改编自 browser-use/jev-ultrafast。Browser/Computer Use 为实验特性，桌面后台输入与焦点隔离在部分应用不可靠。要求 macOS 13+、Apple Silicon。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 捆绑官方未修改的 pi 1.3.0，Full Access 支持自主执行与 Code Mode、子代理
- 原生变更审查界面，逐项接受/拒绝文件修改
- Ask Before Actions / Full Access 全局 Agent 访问控制
- 实验性 Browser Use 与 Computer Use（内置桌面驱动）

## 适用场景

- 在真实项目中用自然语言描述任务并让 agent 提出修改
- 在同一工作区内边对话边编辑和审查代码
- 让 agent 检查网页或操作桌面应用（实验性）

## 场景标签

`编码 Agent` `代码审查` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5:  An AI workspace for understanding code, building with an agent,
> L27: This release bundles the official, unmodified **pi 1.3.0**. Full Access uses pi's autonomous execution for enabled 
> L136: Eido builds on the work of **Zed** and **pi**. Zed provides the native editor foundation; pi powers the coding age

## 星数曲线

```mermaid
xychart-beta
    title "tony3liu/eido 星数(近 7 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26"]
    y-axis "stars" 70 --> 151
    line [76, 96, 119, 120, 129, 136, 145]
```

2026-10-18 76 → 2026-10-26 145（+69）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `33d7f7af683c` · [字段定义](../../DATASET.md)*
