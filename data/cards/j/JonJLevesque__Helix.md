# JonJLevesque/Helix

⭐ 63 · TypeScript · NOASSERTION · 推送 2026-09-28 · [GitHub](https://github.com/JonJLevesque/Helix) · 个人维护

**给 Mac 用户的个人 AI 框架：让 Claude 控制系统、记记忆、定时干活**

基于 Claude Code 的本地个人 AI 框架：通过 fork 仓库并运行安装脚本，向 Claude 注入 4 个 MCP 插件——helix-mac（控制应用、日历、浏览器标签）、helix-memory（跨会话记忆）、helix-agents（定时任务）、helix-telegram（手机遥控）。另有本地语音模式（Whisper 转文字 + Kokoro 朗读）、定时 Loops 自动任务和用 CLAUDE.md 定义人格。全部运行在本机，仅支持 macOS 14+，需在 Terminal 中操作，仅使用官方 claude 命令，不接入其他 AI 服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 个 MCP 插件接入 Mac 系统控制、持久记忆、定时任务与 Telegram 遥控
- 本地语音模式：Whisper 语音识别 + Kokoro 语音合成，无云端依赖
- Loops 定时任务：每次唤醒执行单一动作并记录状态
- 全部请求走用户自己的官方 Claude 账号与 claude 命令，数据留在本机

## 适用场景

- 让 Claude 代为打开应用、查日历、管理浏览器标签
- 通过语音或 Telegram 远程指挥个人 AI 代理
- 配置早报、内容起草等定时自动任务
- 给 AI 代理设定名字与人格并保持跨会话记忆

## 场景标签

`AI 助手` `语音 Agent` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L13: Helix is not a chat app. It's a framework that turns Claude into a personal AI that actually *does things* — opens 
> L19: Helix gives Claude four new superpowers by installing "plugins" (called MCP servers) that connect Claude directly t

## 星数曲线

```mermaid
xychart-beta
    title "JonJLevesque/Helix 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-25 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `fd7352726842` · [字段定义](../../DATASET.md)*
