# SimonSaysGiveMeSmile/SoA-Web

⭐ 14 · JavaScript · NOASSERTION · 推送 2026-10-30 · [GitHub](https://github.com/SimonSaysGiveMeSmile/SoA-Web) · [官网](https://soa-web-ten.vercel.app) · 个人维护

**浏览器版远程终端：WebSocket 流式承载服务器端 PTY 会话**

桌面应用 Son of Anton 的 Web 移植版：单个 Node 进程用 node-pty 在服务器上持有 shell 会话，通过 WebSocket 以 JSON 帧协议推送到浏览器 xterm.js 界面。面向自托管的开发者用户，支持共享密码认证、会话持久化与断线回放、Cloudflare Quick Tunnel 手机扫码接入，以及 Vercel 托管 SPA + 自建后端的分离部署。语音唤醒、托盘、自动更新等 Electron 专属功能未移植；无认证模式仅限回环地址。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- node-pty 运行于 Node 服务器，经 WebSocket 供浏览器访问任意 CLI（含 Claude Code）
- 每标签页目录与滚动缓冲落盘，断线重连可恢复
- Cloudflare Quick Tunnel 自动启动并以二维码供手机接入
- Vercel SPA + 隧道自建后端的分离部署方案

## 适用场景

- 在自建服务器上通过浏览器使用终端并运行 Claude Code 等 CLI
- 手机扫码远程接入同一组终端会话
- 以受密码保护的 Web 终端替代桌面终端应用

## 场景标签

 · 领域:开发者工具/远程终端

## 证据(README 行号)

> L27: - **Claude Code, etc.** Any CLI you want to use runs server-side inside the PTY. Install it on the host; your brows
> L5: A browser-native terminal UI that streams real PTY sessions over WebSocket. No Electron, no installer, no auto-updat

## 星数曲线

```mermaid
xychart-beta
    title "SimonSaysGiveMeSmile/SoA-Web 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `dd8b0bed1cf8` · [字段定义](../../DATASET.md)*
