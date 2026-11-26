# Giton22/kyllene

⭐ 331 · Kotlin · MIT · 推送 2026-11-25 · [GitHub](https://github.com/Giton22/kyllene) · [官网](https://kyllene.app) · 个人维护

**自托管 Hermes Agent 的原生 Android 客户端**

连接用户已在服务器/homelab/VPS/Tailnet 上运行的 hermes dashboard，直接与 gateway 通信，无独立服务端与账号。功能覆盖流式对话（Markdown/代码/TeX/推理过程）、工具调用审批、子代理与后台进程监控、会话管理、定时任务、MCP/技能开关、成本与 token 统计、语音通话与听写、Wear OS/Pebble 手表端。需 Android 8.0+，通过 GitHub Release 下载 APK 安装，需可访问的 dashboard 凭据登录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 工具调用审批、sudo 与密码提示可从系统通知内联处理
- 流式回复支持 Markdown、语法高亮、TeX、推理与工具活动展示
- 可选端到端加密推送，不依赖 Google 服务
- 聊天离线加密副本，gateway 不可达时仍可读

## 适用场景

- 在手机上审批和跟进自托管 agent 的操作
- 通过手表或语音与家中服务器上的 agent 对话
- 管理多个 bot、房间与定时任务

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: **A native Android client for Hermes Agent.**
> L18: Kyllene connects to the `hermes dashboard` you already run on a server, homelab, VPS or Tailnet, the
> L19: same way Hermes Desktop's "Remote gateway" connection does. There is no Kyllene server and no account:

## 星数曲线

```mermaid
xychart-beta
    title "Giton22/kyllene 星数(近 18 点)"
    x-axis ["2026-10-31", "2026-11-01", "2026-11-02", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 198 --> 343
    line [210, 215, 224, 264, 271, 275, 281, 282, 287, 289, 293, 300, 301, 305, 307, 308, 314, 331]
```

2026-10-31 210 → 2026-11-26 331（+121）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `a78de9eeeb92` · [字段定义](../../DATASET.md)*
