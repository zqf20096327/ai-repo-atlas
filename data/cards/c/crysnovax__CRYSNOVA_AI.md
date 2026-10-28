# crysnovax/CRYSNOVA_AI

⭐ 43 · JavaScript · 推送 2026-10-22 · [GitHub](https://github.com/crysnovax/CRYSNOVA_AI) · [官网](https://web.crysnovax.link/) · 个人维护

**基于 Node.js/Baileys 的 WhatsApp 个人号自用多功能机器人**

运行在用户个人 WhatsApp 账号上的 self-bot，基于 Node.js 与 Baileys（fork 版 plogme）构建，通过命令前缀响应消息。功能覆盖多模型 AI（GPT-4.5/DeepSeek/Gemini、图像生成、Whisper 语音转录、OCR）、媒体编辑、下载器（YouTube/TikTok/Spotify 等）、群管理（反垃圾/反链接/警告踢人）、音频特效与工具集，共 250+ 命令。支持动态插件系统（放 .js 文件即生效）、热重载与 setvar 运行时改配置。需要 Node.js v23+ 与 WhatsApp 账号，推荐 VPS 部署；明确声明依赖特定 fork 版 Baileys，否则无法正常工作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模型 AI 套件（GPT-4.5/DeepSeek/Gemini、图像生成、Whisper 转录、OCR）
- 250+ 命令：媒体编辑、下载器、群管理、音频特效、工具
- 动态插件系统：放 .js 文件加命令，无需重启
- 自动重连、会话持久化与运行时变量控制（setvar/getvar）

## 适用场景

- 在自己的 WhatsApp 号上运行机器人自动回复与执行命令
- 群主用它做反垃圾、反链接、警告踢人等群管理
- 下载 YouTube/TikTok 等平台内容并用 AI 处理图片语音

## 场景标签

`聊天机器人` `图像生成` `语音识别` `OCR` · 领域:对话与助手

## 证据(README 行号)

> L38: **CRYSNOVA AI V2** is a premium-grade WhatsApp self-bot built on Node.js and Baileys. It runs directly on your pers
> L60: - GPT-4.5, DeepSeek, Gemini integration

## 星数曲线

```mermaid
xychart-beta
    title "crysnovax/CRYSNOVA_AI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-28 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f1b0ca7ae70c` · [字段定义](../../DATASET.md)*
