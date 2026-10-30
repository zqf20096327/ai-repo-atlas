# somastllc/dastuur-agent

⭐ 24 · TypeScript · 推送 2026-02-06 · [GitHub](https://github.com/somastllc/dastuur-agent) · [官网](https://dastuur.omartood.com) · 个人维护

**索马里临时宪法问答助手：用索马里语自然语言查询宪法条文**

面向终端用户的宪法问答 Web 应用：基于索马里临时宪法 PDF 构建知识库，通过 Google Gemini 生成回答，采用 Memvid 与自定义 RAG 管线（向量嵌入+关键词混合检索，对条文号查询如 'Qodobka 3aad' 加权）。支持多会话、localStorage 持久化历史、Markdown 渲染。安装需 Node.js 18+、Gemini API Key，放置宪法 PDF 后运行 npm run ingest 生成嵌入，再启动 Next.js 开发服务器。

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

- 基于宪法 PDF 的 RAG 问答，回答检索相关条文后生成
- 混合检索：0.6×向量相似度+0.4×关键词匹配，条文号查询加权
- 索马里语自然语言理解与条文号模式识别
- 多会话管理与 localStorage 聊天历史持久化

## 适用场景

- 用索马里语查询临时宪法条文内容
- 按条文号（如 Qodobka 3aad）定位具体条款
- 多轮对话持续了解宪法相关议题

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L8: An intelligent AI-powered assistant that helps users understand and navigate the Somali Provisional Constitution. Bu
> L18: - Context-aware responses using RAG technology

## 星数曲线

```mermaid
xychart-beta
    title "somastllc/dastuur-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-30 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0a406b826800` · [字段定义](../../DATASET.md)*
