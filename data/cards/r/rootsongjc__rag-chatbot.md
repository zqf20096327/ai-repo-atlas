# rootsongjc/rag-chatbot

⭐ 61 · TypeScript · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/rootsongjc/rag-chatbot) · [官网](https://jimmysong.io/book/rag-handbook/) · 个人维护 · 中文 README

**为 Hugo 网站构建可嵌入 RAG 聊天机器人的 Cloudflare Workers 方案**

基于 Cloudflare Workers 的网站 RAG 聊天机器人项目：读取 Hugo 站点 content/ 目录的 Markdown，经切块、嵌入后写入 Cloudflare Vectorize 索引；/chat 接口检索 Top-K 片段、组装提示词并调用 LLM 生成中文回答，返回来源引用（source, url）。前端提供本地存储的 widget.js 可嵌入 Hugo 站点。模型后端可在 Gemini 与通义千问之间切换。支持全量重建索引、单文件增量摄入、中英双语博客的向量抽取与语言过滤检索，内置 ADMIN_TOKEN 管理接口与 Cloudflare 免费额度说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Markdown → 切块 → 嵌入 → 写入 Cloudflare Vectorize 的完整摄入流水线
- Gemini 与通义千问双模型后端可切换
- widget.js 前端组件嵌入 Hugo 网站，返回来源引用
- 中英双语博客去重向量化和按页面语言过滤检索

## 适用场景

- 给自己的 Hugo 博客添加基于站内内容的问答机器人
- 对中英双语博客构建可按语言检索的向量知识库
- 在 Cloudflare Workers 上零服务器部署 RAG 服务

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L3: Build an embeddable RAG Chatbot for your website using Cloudflare Workers. The JavaScript widget is stored locally f
> L10: - /chat: Retrieve Top-K chunks + assemble prompt + call LLM to generate Chinese answers


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `1f80aef8af60` · [字段定义](../../DATASET.md)*
