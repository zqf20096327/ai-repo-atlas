# ashnkumar/llm-full-stack-tutorial

⭐ 41 · Python · MIT · 推送 2026-08-06 · [GitHub](https://github.com/ashnkumar/llm-full-stack-tutorial) · 个人维护

**全栈 RAG 网页问答教程配套示例（OpenAI+Pinecone+Flask+React）**

教程系列"用 OpenAI、Flask、React、Pinecone 构建全栈 LLM 应用"的配套示例仓库：用户输入 URL，后端抓取网页文本、调用 OpenAI Embeddings API 生成向量并存入 Pinecone，再检索相似片段构造提示词经 ChatCompletions 获取回答，前端为 React 聊天界面。仓库分两部分分支（后端 RAG、前端 UI）。README 明确声明代码写于 2023 年 11 月，所依赖 SDK 已变更，原样安装无法运行索引路径，需参考 PR #1 的迁移版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Flask 后端完成网页抓取、OpenAI 嵌入与 Pinecone 检索
- React 前端聊天界面输入 URL 并提问
- 提供 part1_backend / part2_frontend 与帖子对应的冻结分支
- README 声明代码基于 2023 年旧版 SDK，需迁移方可运行

## 适用场景

- 学习 RAG 全栈应用的分步构建过程
- 参考 OpenAI Embeddings + Pinecone 向量检索的接法
- 对照分支阅读后端与前端各自的实现

## 场景标签

`RAG` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L4: This is a sample application built for the following tutorial series, "Build a full-stack LLM application with OpenA
> L19: * **Backend (Flask):** This handles the logic to scrape the website and call OpenAI's Embeddings API to create embe

## 星数曲线

```mermaid
xychart-beta
    title "ashnkumar/llm-full-stack-tutorial 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-29 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `10d7eed7bd23` · [字段定义](../../DATASET.md)*
