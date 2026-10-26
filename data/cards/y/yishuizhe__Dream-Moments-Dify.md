# yishuizhe/Dream-Moments-Dify

⭐ 55 · Python · NOASSERTION · 推送 2026-10-04 · [GitHub](https://github.com/yishuizhe/Dream-Moments-Dify) · 个人维护 · 中文 README

**面向个人用户的 Windows 微信 4 情感陪伴聊天机器人，接入 Dify/OpenAI 兼容 API**

基于 KouriChat/My-Dream-Moments 的实验项目：通过 wxauto4 或 wechatauto-replica 轮询/读取本机微信数据库接收消息，经 Dify Chat API 或 OpenAI 兼容线路生成回复并发回微信私聊与群聊。支持多线路自动切换与熔断、按成员隔离的本地 SQLite 记忆、群聊总结插件、独立图片 API、情绪 GIF、外部插件加载，以及通过 Operit 或自研 NanaPhone 端用微信控制安卓手机。仅支持 Windows 10/11 与微信 4 客户端，发送消息要求桌面解锁；GPLv3，声明仅供个人学习自用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 微信 4 免费 UI 自动化/数据库轮询适配（wxauto4 与 wechatauto-replica）
- 主线路+3 条 OpenAI 兼容备用线路，限流/超时自动切换与 60 秒熔断
- 私聊/群成员独立身份键的本地 SQLite 记忆，可查看或清除
- 内置 ChatSummary 群聊总结与 plugins 目录外部插件机制
- 通过 Operit/自研 NanaPhone 端经微信控制安卓手机

## 适用场景

- 让 AI 角色在微信私聊和群聊中陪聊并保持多轮上下文
- 在白名单群里 @机器人 触发对话、总结聊天记录
- 通过微信自然语言指令控制自己的安卓手机（电量、打开应用等）
- 配置多条免费 AI 线路自动切换以维持可用性

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L7: 基于 **My-Dream-Moments / KouriChat** 的 Windows 微信 4 私人聊天机器人实验项目。
> L34: - 微信好友和群聊中的文字对话；
> L36: - Dify 应用、Prompt 与模型参数管理；

## 星数曲线

```mermaid
xychart-beta
    title "yishuizhe/Dream-Moments-Dify 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23", "2026-10-26"]
    y-axis "stars" 52 --> 56
    line [53, 54, 55, 55]
```

2026-10-18 53 → 2026-10-26 55（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `f36f441e1804` · [字段定义](../../DATASET.md)*
