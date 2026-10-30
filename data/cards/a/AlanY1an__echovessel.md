# AlanY1an/echovessel

⭐ 17 · Python · MIT · 推送 2026-08-27 · [GitHub](https://github.com/AlanY1an/echovessel) · [官网](https://www.alanyian.com/projects/echovessel/) · 个人维护 · 中文 README

**本地优先的数字人格引擎：长期记忆、语音与多渠道对话**

开源数字人格引擎，供想构建角色、陪伴型人格或经同意的数字分身的用户使用。由 memory / voice / channels / proactive / runtime 五模块组成守护进程：L1-L4 分层长期记忆（SQLite + sqlite-vec）、FishAudio TTS 语音、Web（内嵌 React 19）与 Discord DM 两个渠道、主动消息策略引擎、流式对话运行时。LLM 可接 OpenAI 兼容端点、Anthropic 或本地 Ollama，另有无需 API key 的 stub 模式。当前为 v0.0.1 早期 alpha，仅支持 macOS/Linux，无 PyPI 发布，需从源码以 uv 运行；部分管理界面为占位，导入管线无 HTTP 路由。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- L1-L4 四层长期记忆，SQLite + sqlite-vec 存储，含 916 个测试
- Web 与 Discord 双渠道共享同一人格记忆，跨渠道统一时间线
- LLM 支持任意 OpenAI 兼容端点、Anthropic 或本地 Ollama，可零 key stub 运行
- FishAudio TTS 语音输出，Discord 原生 OGG Opus 语音消息

## 适用场景

- 创建带长期记忆与关系演变的陪伴型角色或人格
- 通过 Discord DM 与 Web 同时和同一人格对话
- 本地运行保护隐私，为亲友构建经同意的数字分身

## 场景标签

`Agent 记忆` `语音合成` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L11: **EchoVessel** is an open-source engine for building digital personas that can remember, respond, evolve, and stay 
> L21: EchoVessel is not a generic chatbot.

## 星数曲线

```mermaid
xychart-beta
    title "AlanY1an/echovessel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `f6a5557dfdaa` · [字段定义](../../DATASET.md)*
