# DojoCodingLabs/hermit

⭐ 12 · TypeScript · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/DojoCodingLabs/hermit) · [官网](https://joinhermit.com) · 组织维护

**运行在 Android 手机本地的开源 AI agent，隐私不上传**

Hermit 是一个完全在 Android 手机上运行的开源 AI agent：内置 BotPsy-0.8B 4-bit 本地模型（约 530 MB，首次运行从 Hugging Face 下载并校验 SHA-256），支持聊天、记忆、提醒、日历、WhatsApp 回复、邮件、密码库自动填充和 USD₮ 测试网支付。核心机制是为小模型设计的 harness：类型化技能菜单、路由器强制工具调用、TypeScript 策略引擎（cage）裁决每一步，敏感操作需指纹批准，日志签名链式记录。状态为 pre-alpha，仅在一款手机上调优，构建需 Node.js 24、pnpm、JDK 17 与 Android SDK/NDK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 模型、记忆与活动日志全部留在手机上，无账号、无遥测、无服务器
- cage 策略引擎裁决模型提议的操作，发送/支付/登录需指纹逐项批准
- 签名哈希链式活动日志，编辑或缺失即断链
- 同一 BotPsy-0.8B 模型文件经 harness 从 21/40 提升至 39/40 任务完成率

## 适用场景

- 在无网络环境下用语音或文字聊天、设提醒、管日历
- 让本地 agent 代读并起草 WhatsApp 与邮件回复
- 在手机本地加密存储密码与个人记忆，不经第三方

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L13:  The AI agent that lives on your phone, and nowhere else.
> L41:  It answers your WhatsApp, works your inbox, sets reminders, adds events, fills logins from its vault and pays on a
> L15:  The model runs on your Android phone. Your memories stay there, encrypted.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `be7102d3442d` · [字段定义](../../DATASET.md)*
