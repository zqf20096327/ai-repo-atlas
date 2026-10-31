# btb-finance/Autonomous-AI-Agent

⭐ 21 · TypeScript · MIT · 推送 2026-02-08 · [GitHub](https://github.com/btb-finance/Autonomous-AI-Agent) · [官网](https://www.btb.finance) · 组织维护

**TypeScript 自动化 Twitter 机器人：用 AI 回复 $BTB 提及**

面向 BTB Finance 社区运营的自治 Twitter 机器人：每 60 秒轮询提及、筛选含 $BTB 的推文、抽取问题、检索本地知识库，再通过 OpenRouter（Claude/GPT-4/Gemini 等，含免费模型）生成回答并回复。含速率限制处理、测试命令与调试模式。运行需 Node.js v18+、Twitter 开发者账号（推荐 Basic 档）与 OpenRouter API key；钱包功能仅标注为未来预留。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每 60 秒轮询 Twitter 提及并筛选含 $BTB 的推文
- 本地知识库检索后经 OpenRouter 模型生成回复
- 支持 OpenRouter 免费与付费模型（Claude/GPT-4/Gemini/deepseek 等）
- 内置速率限制处理与推文/提及测试命令

## 适用场景

- 加密项目自动回复社区成员在 Twitter 上的提问
- 围绕代币提及做持续监控与信息分发
- 需要低成本免费模型跑社区运营机器人的场景

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L3: An intelligent Twitter bot that monitors mentions of $BTB, provides information about BTB Finance, and engages with 
> L126: 5. **AI Response Generation**: Uses your chosen OpenRouter model to generate an appropriate response

## 星数曲线

```mermaid
xychart-beta
    title "btb-finance/Autonomous-AI-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a31a08c6e1db` · [字段定义](../../DATASET.md)*
