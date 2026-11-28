# JayDev-27/Hikari

⭐ 5 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/JayDev-27/Hikari) · [官网](https://hikari-companion.vercel.app/) · 个人维护

**macOS 桌面上的本地优先动漫 AI 伴侣，支持印地语/英语口型同步**

以透明桌面形象形式运行的本地优先动漫伴侣应用：Iki/Live2D/VRM 三种渲染器支持的角色立在所有窗口之上，支持英语、印地语与 Hinglish 的对话与音素级口型同步，语音、记忆与大脑设计为在本机运行，Provider key 存于 macOS Keychain，对 Mac 的操作需经确认对话框并记录到 Activity 日志。当前处于早期开发阶段，桌面应用从源码运行并含脚本化口型同步演示；生产级语音、长期记忆、声音训练与 Mac 自动化仍在开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Iki/Live2D/VRM 三类角色渲染器，可导入 .vrm 模型（VRM 0.x 与 1.0）
- 印地语/英语/Hinglish 混说，音素到口型的口型同步映射
- 本地优先设计：Provider key 存 macOS Keychain，语音与记忆在本机运行
- Mac 操作需确认对话框并落入 Activity 日志

## 适用场景

- 在 Mac 桌面养一个会说印地语/英语的动漫角色日常陪伴
- 导入自己的 Live2D 或 VRM 模型做桌面角色
- 本地记忆浏览、修正与遗忘的个人化对话体验

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: **A local-first anime companion for your Mac's desktop.**
> L25: > Hikari is in early development. The desktop app runs from source and includes a scripted lip-sync demo. The produ
> L154:     B <-->|Local WebSocket| D["Python core<br/>In development"]


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `f382d9246c31` · [字段定义](../../DATASET.md)*
