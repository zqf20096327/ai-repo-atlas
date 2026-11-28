# insistgang/Luyao_AI_Project

⭐ 10 · Python · 推送 2026-10-05 · [GitHub](https://github.com/insistgang/Luyao_AI_Project) · 个人维护 · 中文 README

**基于 MiniMax API 的情感陪伴 AI「路遥」，带长期记忆与语音**

面向终端用户的情感陪伴应用，通过 MiniMax abab6.5s-chat 模型进行 Persona 对话与异步记忆抽取，Speech 2.8/2.6 负责语音合成与声纹克隆。关键机制：双轨长期记忆 RAG（本地 ChromaDB）、Persona Guardrail、一条回复拆成多条气泡并与语音按时间同步。Python + uvicorn 运行后端，另以 ui.py 提供界面。限制：Render 免费实例空闲休眠，ChromaDB 不跨重启持久化，仅适合演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一套 MiniMax Key 同时用于聊天、异步记忆抽取、TTS 与声纹克隆
- 双轨长期记忆 RAG、异步记忆提取与 Persona Guardrail
- 回复拆分为多条气泡并与语音按时间同步
- 从音频素材准备并克隆音色（需说话人授权）

## 适用场景

- 搭建有长期记忆的情感陪伴对话角色
- 克隆已授权的声音为角色配音
- 本地演示多 Agent 与 RAG 记忆机制

## 场景标签

`Agent 记忆` `多智能体` `语音合成` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L3: 基于 MiniMax 全栈 API 的情感陪伴 AI：`abab6.5s-chat` 负责 Persona 对话与记忆抽取，Speech 2.8/2.6 负责克隆音色和语音合成。
> L35: - 双轨长期记忆 RAG、异步记忆提取与 Persona Guardrail。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `86dc849afd1a` · [字段定义](../../DATASET.md)*
