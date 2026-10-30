# Shikigami-Lab/Shikigami-Protocol

⭐ 15 · Python · AGPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/Shikigami-Lab/Shikigami-Protocol) · 组织维护 · 中文 README

**本地优先的有状态 AI 角色陪伴框架，带长期记忆与主动发言**

面向终端用户的开源 AI 陪伴角色框架：内置情绪×精力×好感度状态机、事实抽取+向量检索+每日总结的记忆管线、艾宾浩斯遗忘曲线，以及空闲时的后台反思与阈值触发的主动搭话。对话日志与状态存本地磁盘，推理可用云端 API、Ollama 等本地模型或混合。提供 Electron/浏览器 UI 与 FastAPI 后端，从源码或 Docker 运行，不发布预编译安装包；明确声明不做桌面自动化或多步 Agent。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 情绪×精力×好感度状态机驱动语气与 TTS 情感
- 内置记忆管线：事实抽取、ChromaDB 向量检索、每日日记、遗忘曲线
- 后台反思与 ASE 主动搭话（阈值触发而非定时器）
- 多种 TTS 引擎（Edge/Kokoro/GPT-SoVITS/Qwen3）与 SenseVoice/Whisper 本地语音输入

## 适用场景

- 与具备长期记忆和情绪状态的角色持续对话
- 多角色群聊会话（流式输出、逐角色署名）
- 角色在用户沉默时基于内部状态主动发起联系
- 手机/平板同网络访问本地服务器的 Web UI

## 场景标签

`聊天机器人` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L5: **A local-first framework for persistent, stateful conversational agents**
> L21: Most AI chat tools reset to zero when you close the tab. Shikigami Protocol is built around the opposite premise: a
> L63: - **Reflection + proactive speech (ASE)**: Background **Reflection** generates inner monologue while you are away; 

## 星数曲线

```mermaid
xychart-beta
    title "Shikigami-Lab/Shikigami-Protocol 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29", "2026-10-30"]
    y-axis "stars" 11 --> 16
    line [12, 13, 15, 15]
```

2026-10-18 12 → 2026-10-30 15（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7ff85cb756a3` · [字段定义](../../DATASET.md)*
