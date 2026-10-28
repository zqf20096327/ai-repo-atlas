# pungme/superagent-desktop

⭐ 33 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/pungme/superagent-desktop) · [官网](https://superagent.computer) · 个人维护

**macOS 桌面工作台：为 Claude Code/Codex 等编码代理提供运行环境**

Electron/macOS 桌面应用，作为 Claude Code、Codex 与 Antigravity 编码代理的宿主工作台：每个对话在项目副本上运行，提供代理可驱动的真实浏览器窗格、串流进窗口的 iOS Simulator、可分屏的持久聊天（最多八窗）、iPhone 配对远程应答（端到端加密经中继）、定时例程、看板与上下文用量显示等。全部本地运行，使用用户已有订阅，无中间服务器，自身不含模型。macOS Apple Silicon 供下载，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 同时支持 Claude Code、Codex、Antigravity，可按对话切换
- 代理驱动的真实浏览器窗格与 iOS Simulator 串流（约每秒一帧）
- iPhone 配对远程应答，端到端加密，中继不存储内容
- 每对话独立项目副本与分支；支持最多八窗分屏

## 适用场景

- 在 Mac 上给编码代理一个带浏览器和模拟器的可视化工作环境
- 离开桌面时通过 iPhone 继续跟进代理对话并回答其提问
- 用定时例程让代理按计划检查网站或持续迭代

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7:  A Mac app where your coding agent lives: a real browser it drives, an iPhone in the window, chats that survive rest
> L34: — Claude Code, Codex or Antigravity, switchable per chat. No middleman server, no API key, no
> L35: AI of its own — and the whole app is open source, so you can read exactly how it

## 星数曲线

```mermaid
xychart-beta
    title "pungme/superagent-desktop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-28 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `8b49eef94ced` · [字段定义](../../DATASET.md)*
