# naver-ai/chacha-chatbot

⭐ 42 · Python · MIT · 推送 2025-12-29 · [GitHub](https://github.com/naver-ai/chacha-chatbot) · [官网](https://naver-ai.github.io/chacha) · 组织维护

**引导儿童分享情绪事件的活动 LLM 聊天机器人（CHI 2024）**

ACM CHI 2024 论文的聊天机器人源码实现：利用大语言模型（GPT-3.5 与 GPT-4）通过对话引导儿童讲述个人事件并表达情绪，面向儿童情绪感知的人机交互研究场景。提供命令行与 Web 两种运行方式（Python 后端 + React/TypeScript 前端），使用 Poetry 与 npm 安装依赖，需付费 OpenAI API key。会话与消息以文件存储（info.json / dialogue.jsonl）替代数据库，支持 Web 端回看会话并导出 CSV 聊天记录。

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

- 基于 GPT-3.5/GPT-4 的儿童情绪引导对话
- 命令行与 Web（前后端）两种运行方式
- 文件存储会话数据，支持 Web 回看与 CSV 导出聊天记录

## 适用场景

- 儿童情绪感知相关的人机交互研究部署
- 复现 CHI 2024 论文中的对话系统
- 收集并分析儿童情绪对话日志

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: # ChaCha (CHAtbot for CHildren's emotion Awareness): LLM-Driven Chatbot for Enhancing Emotional Awareness in Childre
> L9: This repository is a source code of the chatbot implementation presented in the ACM CHI 2024 paper, titled "**ChaCha
> L22: 4. Paid OpenAI API key (ChaCha uses GPT-3.5 and GPT-4 models internally).

## 星数曲线

```mermaid
xychart-beta
    title "naver-ai/chacha-chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8972997e8ad3` · [字段定义](../../DATASET.md)*
