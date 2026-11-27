# ANDRETRIPOL/OpenGhost

⭐ 307 · JavaScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/ANDRETRIPOL/OpenGhost) · [官网](https://andretripol.github.io/OpenGhost/) · 组织维护

**面向个人用户的桌面 AI agent，可执行任务并以图表可视化讲解**

基于 Electron 的开源桌面 agent，覆盖 Windows、macOS 与 Linux。它运行命令、编辑文件、使用 git、并通过自带的浏览器面板操作网页；回答旁可生成 40 余种可编辑的图表。核心组件均为自研：agent 循环与工具、绘图引擎、浏览器驱动、Markdown 渲染器与界面，仅依赖 Electron 与 Anthropic 官方 SDK。提供例程与定时提醒、多层记忆与对话压缩、技能（Agent Skills 格式）接入、三档权限模式。当前版本为 1.5.8 beta。

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

- 自研绘图引擎，生成 43 种可现场编辑的图表（流程图、曲线、生活场景图等）
- 自带浏览器面板，agent 在用户登录的账号内移动光标、点击、输入
- 例程与提醒：窗口关闭后驻留托盘，定时执行并汇报结果
- 分层记忆与滚动摘要压缩，配合 AGENTS.md 项目指令

## 适用场景

- 让 agent 代为执行多步任务并逐项验证（测试、构建、读回文档）
- 学习时让 AI 用图表讲解概念或训练过程
- 在已登录的网页账号中批量查看与整理信息
- 设置每日例程自动检查并汇报结果

## 场景标签

`AI 助手` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L28: OpenGhost is an open desktop agent for Windows, macOS and Linux. It runs commands, edits files, keeps git and works
> L44: The app stands on two things only: Electron, which gives it a window, and Anthropic's official SDK, which talks to 

## 星数曲线

```mermaid
xychart-beta
    title "ANDRETRIPOL/OpenGhost 星数(近 19 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-14", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-23", "2026-11-26", "2026-11-27"]
    y-axis "stars" 272 --> 310
    line [275, 276, 277, 279, 281, 282, 283, 284, 275, 288, 293, 294, 295, 297, 299, 300, 302, 306, 307]
```

2026-10-25 275 → 2026-11-27 307（+32）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `a348ac54926b` · [字段定义](../../DATASET.md)*
