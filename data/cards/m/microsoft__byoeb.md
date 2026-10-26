# microsoft/byoeb

⭐ 41 · Python · CC-BY-4.0 · 推送 2026-10-23 · [GitHub](https://github.com/microsoft/byoeb) · 组织维护

**构建专家审核 WhatsApp 聊天机器人的平台**

BYOeB（Build Your Own Expert Bot）是微软开源的平台，供开发者构建基于 WhatsApp 的 expert-in-the-loop 聊天机器人：每条回答先由模型生成，再由人类专家（如医生、法务）验证和编辑，编辑结果可回流更新知识库。支持自定义知识库（ChromaDB 向量库）、多语言、文本与音频输入输出。回答生成与翻译、TTS、语音识别依赖 Azure OpenAI、Azure AI Translator 等云服务，通过 Flask 部署，含 cron 定时任务（未答查询上报专家、邮件确认 KB 更新等）。面向医疗、法律等专业领域场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | CC-BY-4.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 专家验证/编辑每条回答，编辑回流更新知识库
- 自定义知识库：原始文档经 OpenAI Embedding 构建 ChromaDB
- 多语言与文本/音频输入输出（翻译、TTS、语音识别）
- cron 任务链：未答查询升级、专家邮件确认、账户过期等

## 适用场景

- 为医疗或法律场景搭建有人工专家把关的问答机器人
- 利用专家编辑持续改进领域知识库
- 通过 WhatsApp 向患者等用户提供多语言文本与音频问答

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L2: BYOeB (Build Your Own Expert Bot) is a platform designed to build expert-in-the-loop WhatsApp-based chatbots. It ena
> L81: - Every response to the user query needs to be verified (and if needed, edited) by the expert.

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/byoeb 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 40 --> 44
    line [43, 41, 41]
```

2026-10-18 43 → 2026-10-26 41（-2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8d33582348c0` · [字段定义](../../DATASET.md)*
