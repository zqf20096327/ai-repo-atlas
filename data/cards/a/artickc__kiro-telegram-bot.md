# artickc/kiro-telegram-bot

⭐ 22 · TypeScript · MIT · 推送 2026-09-29 · [GitHub](https://github.com/artickc/kiro-telegram-bot) · [官网](https://github.com/artickc/kiro-telegram-bot#readme) · 个人维护

**通过 Telegram 远程控制 Kiro CLI 的 ACP 桥接客户端**

基于 Agent Client Protocol (ACP) 的 Telegram 桥接应用：把本机已安装的 Kiro CLI 编码代理接入 Telegram，支持切换项目、恢复与附加到正在运行的会话、流式回复带统一 diff、排队后续消息、定时任务、多图与语音输入（经 OpenAI/Whisper 兼容端点转录）、多账号切换与聊天内重新认证。可安装为 Windows/Linux/macOS 用户级 24/7 后台服务，提供 npm 安装、一键安装脚本与 Docker 镜像（内置 Kiro CLI）。前置条件为已安装并认证的 Kiro CLI 与 Node.js 20+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 经 ACP 恢复/附加/终止 Kiro 会话，只读实时旁观运行中会话
- 定时任务（once/daily/weekly/monthly/interval）结果回传聊天
- 多 Kiro 账号保存、一键切换与放弃后自动轮换重试
- 安装为跨平台用户级后台服务（计划任务/systemd/launchd）

## 适用场景

- 在外面用手机让家里的 Kiro 代理读写代码、跑命令
- 旁观或接管 PC 上正在进行的编码会话
- 设置定时提示词任务让代理定期执行并回传结果

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: A professional Telegram bridge for the **Agent Client Protocol (ACP)** that
> L14: turns Kiro CLI into a mobile, always-on AI pair programmer. Send a message from
> L131: - **Kiro CLI** installed and authenticated — run `kiro-cli chat` once to confirm.

## 星数曲线

```mermaid
xychart-beta
    title "artickc/kiro-telegram-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `968a6fa6596a` · [字段定义](../../DATASET.md)*
