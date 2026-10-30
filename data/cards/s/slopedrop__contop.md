# slopedrop/contop

⭐ 17 · Python · MIT · 推送 2026-04-09 · [GitHub](https://github.com/slopedrop/contop) · [官网](https://www.contop.app) · 个人维护

**用手机语音/文字远程 AI 控制桌面电脑的应用**

由手机端 App 与桌面端（Tauri + Python FastAPI 服务）组成的远程桌面控制系统：手机扫码经 WebRTC P2P 与 Cloudflare Tunnel 配对后，可手动触控远程屏幕，也可下达语音或文字指令，由桌面上的自主 Agent 观察屏幕、执行 CLI、GUI 自动化、浏览器控制等 30+ 工具并实时回传进度。支持多模型接入（Gemini/OpenAI/Anthropic/OpenRouter 或 Claude Pro 等订阅代理），提供 Docker 沙箱、双重安全评估与审计日志。iOS 端尚未公开。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 自主 Agent 具备 30+ 执行工具与 9 种视觉后端路由
- QR 码配对的 WebRTC P2P 连接，无需端口转发/VPN/SSH
- 安全机制：双重工具评估、危险操作确认、Docker 沙箱、JSONL 审计日志
- 订阅模式可复用 Claude Pro/Max、ChatGPT Plus 等订阅替代 API key

## 适用场景

- 出门在外用手机操控家里或办公室的电脑完成操作
- 让 AI 代为执行桌面上的表单填写、浏览器自动化等任务
- 通过手机实时查看并干预远程任务的执行过程

## 场景标签

`GUI 自动化` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L27: Contop turns your phone into an AI remote control for any desktop. Speak or type a command on your mobile, and an a
> L89:  Manual control - direct touch control of the remote desktop
> L109: ### Autonomous AI Agent

## 星数曲线

```mermaid
xychart-beta
    title "slopedrop/contop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `9bbbf2fe7cc2` · [字段定义](../../DATASET.md)*
