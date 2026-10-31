# huseynovvusal/whatsapp-ai-bot

⭐ 16 · TypeScript · MIT · 推送 2026-09-04 · [GitHub](https://github.com/huseynovvusal/whatsapp-ai-bot) · 个人维护

**TypeScript WhatsApp 群聊 AI 机器人：Gemini/OpenAI 生成回复**

基于 Baileys 的 WhatsApp 机器人，用 TypeScript 编写：通过终端 QR 码绑定 WhatsApp 号码，在群聊中被 @ 提及时响应，私聊响应全部消息；接入 Google Gemini 或 OpenAI GPT 生成回答，按可配置时间窗口保留消息上下文。提供管理员命令（!status/!clear/!system 等）、按用户的速率限制（管理员豁免）、原生引用回复、自动重连与 Express 健康检查，以及无鉴权的极简 Admin Web UI（/admin，需置于可信网络）。Admin UI 明确不含身份验证，且声明仅供教育用途，需自行遵守 WhatsApp 服务条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gemini/OpenAI 双提供商可切换（LLM_PROVIDER 配置）
- 群聊仅 @ 提及响应，私聊全响应，含上下文消息记忆
- 可配置速率限制（默认每用户 60 秒内 2 次，管理员豁免）
- /admin Web UI 在线修改配置并持久化到 runtime_config.json，无需重启

## 适用场景

- 给 WhatsApp 群组或私聊挂一个可 @ 的 AI 助手
- 通过管理员命令调整系统提示词与清空记忆
- 限制群成员使用频率以防刷屏

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: A TypeScript-based WhatsApp bot using Baileys and Google Gemini AI to respond to messages in groups and private chat
> L12: - ✅ **AI-Powered Responses** - Google Gemini (or OpenAI GPT) integration

## 星数曲线

```mermaid
xychart-beta
    title "huseynovvusal/whatsapp-ai-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `59d855b827d4` · [字段定义](../../DATASET.md)*
