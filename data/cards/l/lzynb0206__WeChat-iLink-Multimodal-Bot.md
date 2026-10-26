# lzynb0206/WeChat-iLink-Multimodal-Bot

⭐ 52 · Java · 推送 2026-10-04 · [GitHub](https://github.com/lzynb0206/WeChat-iLink-Multimodal-Bot) · 个人维护 · 中文 README

**基于 Spring Boot 与阿里云百炼的多模态微信机器人**

通过微信 iLink SDK 接入微信，结合 DashScope 上的 Qwen 系列模型提供文本、图片理解与生成、语音识别（ASR）与合成（TTS）、翻译等能力。采用 Skill → RAG → LLM/Tool 的分层路由：确定性工作流由 Skill 执行，本地 JSON 知识库做关键词检索 RAG，其余交给 LLM 与 Function Calling（支持 Java 21 虚拟线程上的并行工具调用）。面向希望在其上扩展工具、技能与知识库的开发者。当前 RAG 为关键词匹配而非语义检索，对话无持久记忆。运行需 Java 21、Node.js 18+ 与 DashScope API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Skill → RAG → LLM/Tool 分层路由
- 多轮与并行的 Function Calling（Java 21 虚拟线程）
- 文本/图片/语音多模态输入输出（SILK 解码、ASR/TTS）
- 本地 JSON 知识库的关键词 RAG

## 适用场景

- 搭建个人微信 AI 助手或客服机器人
- 通过扩展 BotTool/BotSkill 增加工具与确定性工作流
- 接入项目自有知识做问答

## 场景标签

`AI 助手` `多模态` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L26: |💬|WeChat integration|QR-code login and text, image, voice, file, and image replies|
> L27: |🧠|Multimodal AI|Chat, intent recognition, image understanding, image generation, ASR, and TTS|
> L61: 3. **LLM/Tool** handles open-ended chat, image requests, and tool selection.

## 星数曲线

```mermaid
xychart-beta
    title "lzynb0206/WeChat-iLink-Multimodal-Bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-26 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3380c304733b` · [字段定义](../../DATASET.md)*
