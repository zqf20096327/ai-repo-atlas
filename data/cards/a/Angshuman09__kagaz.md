# Angshuman09/kagaz

⭐ 34 · TypeScript · 推送 2026-10-12 · [GitHub](https://github.com/Angshuman09/kagaz) · [官网](https://kagaz-notes.vercel.app) · 个人维护

**可对话的 PDF 笔记应用：上传文档并问答获取答案**

基于 Next.js 16 + Convex 的 Web 应用，用户经 Clerk 登录后上传 PDF 或文本文件，系统提取文本、分块并生成嵌入，随后在聊天界面提问并获得基于文档内容的 AI 生成回答（RAG，Gemini + LangChain）。支持写作与组织笔记（Tiptap 编辑器），集成 Stripe/Dodo 支付。已知限制：仅支持 PDF 与文本、超大文件受 token 上限约束可能仅部分嵌入或超时。需自行部署并配置 Convex/Clerk 等账号。

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

- PDF/文本上传后提取-分块-嵌入的 RAG 问答流程
- 使用 Google Generative AI (Gemini) 与 LangChain
- Clerk 认证、Tiptap 富文本笔记编辑、Stripe 支付集成

## 适用场景

- 上传自己的 PDF 或笔记并向文档提问获取答案
- 在写作整理笔记的同时基于文档内容问答
- 自部署一套个人文档问答 Web 应用

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5: *Write, organize, and ask questions. Kagaz turns your notes into answers.*
> L59: 5. **Get Answers**: Receive AI-generated answers based on your document content

## 星数曲线

```mermaid
xychart-beta
    title "Angshuman09/kagaz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8631331ff246` · [字段定义](../../DATASET.md)*
