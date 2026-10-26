# levilyf/droidclaw

⭐ 57 · JavaScript · MIT · 推送 2026-07-03 · [GitHub](https://github.com/levilyf/droidclaw) · 个人维护

**运行在 Android Termux 中的个人 AI agent，自然语言操控手机**

在 Termux 中运行的本地优先个人 AI agent：通过无障碍服务伴生 APK 实现免 root 的手机控制（读通知、点按、输入、滑动、控制音量亮度等），每 60 秒截屏送视觉模型做持续观察，后台守护进程每 8 分钟运行内部独白并可主动经 Telegram 发消息。记忆层面提供 KIRA_MIND 统一数据库、情感加权记忆与六档响应路由。支持任意 OpenAI 兼容 API（含 NVIDIA NIM、OpenRouter、本地 Ollama），一条 curl 脚本安装，要求 Android 手机 + Termux + API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 免 root 的 Accessibility Service 手机控制（通知读取、点按输入、传感器读取等）
- 每 60 秒截屏送视觉模型的持续设备观察（GROUND）
- 24/7 后台守护进程与定时内部独白，可主动 Telegram 推送
- 支持任意 OpenAI 兼容 API，包括本地 Ollama

## 适用场景

- 在 Android 手机上用自然语言让 AI 代为操作应用
- 让长期驻留的 agent 记住偏好并主动提醒
- 在无 root 设备上做手机自动化

## 场景标签

`GUI 自动化` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L22: Kira is a personal AI agent that lives on your Android phone. Not in the cloud. Not on someone else's server. On yo
> L103: A companion APK that gives Kira Accessibility Service access.
> L144: Kira works with **any OpenAI-compatible API**. You're not locked in.

## 星数曲线

```mermaid
xychart-beta
    title "levilyf/droidclaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 55 --> 58
    line [56, 57, 57]
```

2026-10-18 56 → 2026-10-26 57（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7709857a63fa` · [字段定义](../../DATASET.md)*
