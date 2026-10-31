# panzeyu2013/dsh-chamber

⭐ 14 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/panzeyu2013/dsh-chamber) · [官网](https://github.com/panzeyu2013/dsh-chamber/releases) · 个人维护 · 中文 README

**dsh（DeepSeek Harness）的桌面连接管理器：本地与远程实例统一管理**

macOS 原生桌面应用，用 Swift/AppKit 壳承载 Node sidecar 业务，页面 100% 复用 dsh 官方前端源码。核心职责是连接管理：本地 dsh 实例自动启动与守护；远程服务器经 SSH 隧道（自动建隧道、管理远端 systemd）或认证 Gateway 接入；多实例在同一窗口的 dsh 原生侧边栏按来源分组导航。另提供运行时版本热重载、Git Worktree 生命周期管理、桌面通知、托盘常驻与 Sparkle 应用内更新。服务器端 Gateway 经一键脚本部署，凭据以 0600 文件或系统密钥链保存。当前版本 0.4.x。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 远程实例经 SSH 隧道接入，应用自动建隧道并管理远端 systemd
- 认证 Gateway 提供公网统一入口，一键脚本部署
- 多实例同窗共存，统一 dsh 原生侧边栏按来源分组
- macOS Swift/AppKit 原生壳，官方前端源码复用

## 适用场景

- 在一个窗口里同时管理本机与多台服务器上的 dsh 实例
- 通过认证 Gateway 把 dsh 以带认证的形态放到公网供团队使用
- 在侧边栏闭环创建 Git worktree → workspace → session

## 场景标签

 · 领域:开发者工具/AI agent 运行管理

## 证据(README 行号)

> L8: dsh（DeepSeek Harness）的桌面连接管理器：把本机与任意多台服务器的dsh实例收进一个原生窗口——本地打开即用，远程经SSH隧道或认证Gateway一键接入，全部来源共用同一条dsh原生侧边栏与官方前端。
> L22: - **远程是一等来源** —— 本地实例只是第一个来源：远程服务器经SSH隧道接入（应用自动建隧道并管理远端systemd），公网/团队场景经认证Gateway接入；两者与本地实例在同一条dsh原生侧边栏里平等列出。
> L91: - macOS Swift原生壳 — AppKit窗口+WKWebView；菜单/托盘/通知/角标/深链/文件对话框/隐藏恢复与应用内更新（Sparkle）均为原生实现；壳内不承载业务，页面100%复用官方前端

## 星数曲线

```mermaid
xychart-beta
    title "panzeyu2013/dsh-chamber 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `fb471da396c0` · [字段定义](../../DATASET.md)*
