# marswangyang/personal-ai-memory

⭐ 69 · TypeScript · Apache-2.0 · 推送 2026-03-24 · [GitHub](https://github.com/marswangyang/personal-ai-memory) · [官网](https://ai-memory-beta.vercel.app/) · 个人维护 · 中文 README

**本地优先的 Chrome 扩展：捕获 AI 对话为私有记忆并注入回新对话**

基于 Plasmo（Chrome MV3）的浏览器扩展，被动拦截 ChatGPT、Claude、Gemini、Perplexity、Grok 的对话并存入浏览器本地 IndexedDB，构建本地记忆库。检索采用混合方案：Transformers.js ONNX 多语言向量检索（含时间衰减）与 MiniSearch BM25 关键词检索，经 RRF 融合；提供一键 Recall 将相关记忆作为 RAG 上下文注入新对话，并支持 JSON 全量备份与收藏提示词管理。无服务器、无 API key，仅首次运行下载 ONNX 模型时产生网络请求，可关闭匿名分析。开发者需 Node.js 18+ 与 pnpm 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 被动捕获 5 个 AI 平台对话并存于本地 IndexedDB
- 混合检索：ONNX 向量（时间衰减）+ BM25，RRF 融合
- 一键 Recall 将记忆作为 RAG 上下文注入新对话
- 8 种 UI 语言与 JSON 全量备份（含 embeddings）

## 适用场景

- 跨 AI 平台保存并检索历史对话记忆
- 在新对话中一键注入过往相关上下文
- 本地管理收藏的提示词并自动补全

## 场景标签

`RAG` `提示工程` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L20: > A Chrome extension that **silently captures** your ChatGPT / Claude / Gemini / Perplexity / Grok conversations an
> L70: |**Hybrid search**|Vector (time-decay) + BM25, fused with RRF for best-of-both results|
> L71: |**One-click Recall**|Injects relevant memories as a RAG prompt into ChatGPT, Claude, Gemini, Grok, and Perplexity|

## 星数曲线

```mermaid
xychart-beta
    title "marswangyang/personal-ai-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-18 69 → 2026-10-27 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `092a65bb1cba` · [字段定义](../../DATASET.md)*
