# gurudin/anycoding

⭐ 18 · Java · Apache-2.0 · 推送 2026-04-21 · [GitHub](https://github.com/gurudin/anycoding) · [官网](https://gurudin.github.io/anycoding/) · 个人维护 · 中文 README

**用 Android 手机远程接管电脑上 AI 编程代理会话的工具**

开源工具包：将 Mac/Linux/Windows 终端中的 Claude Code、OpenAI Codex 等 pty 型 AI 编程代理会话实时镜像到原生 Android 应用，手机与桌面挂接同一 pty 进程，断线后自动回放 256KB 缓冲。网络模式二选一：托管云中继（含 30 天试用，中继为闭源托管服务、不在仓库内）或 cloudflared 自托管直连模式（无需账户）。Android 端使用 Termux TerminalView 渲染完整 VT100 终端。面向使用 AI 编程代理的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 手机与桌面挂接同一 pty 进程，关闭桌面窗口不杀会话
- 托管云中继与 cloudflared 自托管直连两种模式可选
- Termux TerminalView 原生渲染：truecolor、CJK 宽字符、alt screen
- 多标签多项目并行，多台 PC 绑定切换

## 适用场景

- 通勤路上用手机继续电脑上的 AI 编程代理会话
- 不配置端口转发/LAN 的情况下从手机连接多项目代理
- 通过直连模式让敏感代码不经第三方中继服务器

## 场景标签

 · 领域:开发者工具/移动终端

## 证据(README 行号)

> L21: **AnyCoding** is an open-source toolkit that mirrors your terminal AI coding session — Claude Code, OpenAI Codex, o
> L82: - **Multi-agent support** — `any-coding claude [args]` / `any-coding codex [args]` with transparent argument passth

## 星数曲线

```mermaid
xychart-beta
    title "gurudin/anycoding 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `8bf1b4afc0a9` · [字段定义](../../DATASET.md)*
