# evanhu1/talk2arxiv

⭐ 531 · TypeScript · Apache-2.0 · 推送 2026-10-02 · [GitHub](https://github.com/evanhu1/talk2arxiv) · [官网](https://talk2arxiv.org) · 个人维护

**把 arXiv/bioRxiv 论文链接变成可对话阅读器的 Web 应用**

面向论文读者的网站：将 arxiv.org 域名替换为 talk2arxiv.org 即可在 HTML/PDF 阅读器中与读过全文的 AI 对话。整篇论文文本直接进入模型上下文（无分块、嵌入或向量库），通过 OpenRouter 调用 GPT-6 Luna 并流式返回；支持划选提问、引用预览与引用论文加入对话、作者其他著作索引、跨读者共享的答案缓存。架构为 Vercel 托管 React 前端 + Cloudflare Worker API，聊天历史存于浏览器 localStorage。超出约 80 万 token 的论文会报错。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 整篇论文全文进入模型上下文，无分块/嵌入/向量数据库
- 划选段落 Ask AI/Explain，公式以 LaTeX 传入
- 引用文献预览并可加入对话，作者其他著作自动建索引
- 基于 Cloudflare Cache API 的跨读者答案缓存（7 天过期）

## 适用场景

- 阅读 arXiv 论文时向 AI 提问摘要、方法与局限
- 点开参考文献预览并追问被引论文内容
- 在手机上边读边问、保留每篇论文的本地聊天记录

## 场景标签

`科研工具` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: Change `arxiv.org` to `talk2arxiv.org` in any paper link to read the paper and chat with an AI that has read all of 
> L17: - **Whole-paper context.** No chunking, embeddings, or vector database. The full paper text goes into the model's c
> L32:  - `POST /api/chat` puts the paper text and the conversation into one prompt. It sends the prompt to GPT-6 Luna (`o

## 星数曲线

```mermaid
xychart-beta
    title "evanhu1/talk2arxiv 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 529 --> 532
    line [530, 531, 531]
```

2026-10-18 530 → 2026-10-30 531（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `c06f4242ebd9` · [字段定义](../../DATASET.md)*
