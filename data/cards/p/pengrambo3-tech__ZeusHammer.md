# pengrambo3-tech/ZeusHammer

⭐ 67 · Python · 推送 2026-04-25 · [GitHub](https://github.com/pengrambo3-tech/ZeusHammer) · [官网](https://github.com/pengrambo3-tech/ZeusHammer) · 个人维护 · 中文 README

**本地优先的 AI 超级代理：本地意图路由+三层记忆+语音交互**

融合 ClaudeCode 工具执行引擎、Hermes 记忆与安全、OpenClaw 多渠道网关的开源 AI 代理。核心机制：Local Brain 在本地完成意图识别与技能匹配以减少 LLM API 调用；三层记忆（LRU 短期+SQLite FTS5 长期+工作记忆）与 Chroma 向量存储；Whisper+Edge TTS 语音全栈（唤醒词、双语切换）；内置中国大模型统一客户端（经 chinawhapi.com 接入）。README 自述弱点：生态与消息渠道规模不及 OpenClaw/Hermes。L179 存在未解决的 git 合并冲突标记。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Local Brain 本地意图识别+技能匹配，减少 LLM API 调用
- 三层记忆（LRU/SQLite FTS5/工作记忆）+ Chroma 向量存储
- Whisper STT + Edge TTS + 唤醒词（中英文）语音全栈
- 内置 DeepSeek/Qwen/GLM 等 7 家中国大模型统一客户端

## 适用场景

- 我用语音唤醒词让本机 AI 助手执行任务并保持离线
- 希望降低 LLM API 月度费用、让常见请求在本地处理
- 需要一个跨会话长期记忆并自动生成技能的 agent

## 场景标签

`Agent 记忆` `AI 助手` `语音 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L30: ZeusHammer is the **first AI agent that thinks locally before asking the cloud**. Our Local Brain architecture hand
> L55: |**Local Brain**|❌|❌|✅|80% tasks without LLM, intent recognition + skill matching|
> L246: ## Supported Models

## 星数曲线

```mermaid
xychart-beta
    title "pengrambo3-tech/ZeusHammer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-28 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e8b20b7304ae` · [字段定义](../../DATASET.md)*
