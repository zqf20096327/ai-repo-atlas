# CCMu04/DSHDesktop

⭐ 18 · JavaScript · MIT · 推送 2026-09-03 · [GitHub](https://github.com/CCMu04/DSHDesktop) · [官网](https://github.com/CCMu04/DSHDesktop/releases) · 个人维护 · 中文 README

**DeepSeek Harness 官方 Web UI 的 Windows 非官方桌面封装**

基于 Electron 的 Windows 桌面壳：启动官方 DSH Web 服务并加载到桌面窗口，不修改官方源码，界面与对应版本 DSH 保持一致。安装包内置匹配版本的 DSH、官方 Node.js 运行时与 pnpm，默认共用 ~/.dsh 目录使设置、会话与插件互通。提供 9 个内置插件扩展工作台、文件/Git 面板、右键菜单、完成提醒、托盘命令等桌面功能，并内置 Git Bash 按需下载与极简模式预设。仅监听本机回环端口，Web 服务本地运行。

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

- 直接加载官方 dsh web，零前端分叉，跟随 npm 上最新 DSH 版本
- 共用 ~/.dsh，设置、凭据、会话、Profiles 与插件与原生 DSH 互通
- 9 个内置插件：工作台、文件/Git 面板、右键菜单、完成提醒、托盘、检查更新等
- Git Bash 按需下载便携版，带写围栏的极简模式预设

## 适用场景

- 把 DSH 的 Web 界面停靠为双击运行的 Windows 桌面程序
- 在桌面端继续使用原生 DSH 的已有会话与插件
- 通过浮动工作台面板查看文件与 Git 状态

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: > 面向 Windows 的非官方 DeepSeek Harness 桌面客户端。不修改官方源码，直接运行并呈现官方 Web UI。
> L138: 桌面壳启动官方 DSH Web 服务并加载到隔离的 Electron 窗口。后端运行在安装包内置的官方 Node.js 运行时（DSH 的原生目录选择器依赖的 koffi 绑定与 node-pty 输出在 Electron-as

## 星数曲线

```mermaid
xychart-beta
    title "CCMu04/DSHDesktop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `d19a91b6402f` · [字段定义](../../DATASET.md)*
