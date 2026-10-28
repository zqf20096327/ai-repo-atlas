# DylanUnicorn/little-alphaxiv

⭐ 20 · TypeScript · MIT · 推送 2026-10-16 · [GitHub](https://github.com/DylanUnicorn/little-alphaxiv) · 个人维护 · 中文 README

**自托管 arXiv 论文阅读工作区：LLM 对话检索+PDF 伴读**

自部署的论文阅读与讨论应用：用自然语言向助手描述需求，助手调用 arXiv/OpenAlex/Semantic Scholar 检索（可选 web_search）并以卡片呈现结果；点击后左侧 pdf.js 打开 PDF，右侧为注入论文全文的论文感知助手，支持标注、分支对话与 Zotero 笔记同步。用户自带 OpenAI 兼容 API key（OpenAI、Anthropic 网关、Ollama、one-api/new-api 均可），数据存于服务器端 SQLite，API key Fernet 加密。后端 FastAPI、前端 React/TS，提供 Docker、本地开发与 Linux 单文件 .run 三种运行方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话式论文检索（arXiv/OpenAlex/Semantic Scholar 工具调用）+ 论文全文注入的伴读助手
- 多用户账号体系，API key Fernet 加密存储，数据留在自建服务器
- PDF 标注（矩形/手绘/文本/高亮）与 Zotero 笔记一键同步
- 兼容任意 OpenAI 兼容端点：OpenAI、Anthropic 网关、本地 Ollama、one-api/new-api

## 适用场景

- 在自己服务器上搭建论文检索与阅读环境，数据不经第三方
- 阅读 arXiv PDF 时与基于论文原文的 AI 助手讨论、划选提问
- 把阅读标注同步到 Zotero 做文献管理

## 场景标签

`科研工具` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5: **A self-hosted, alphaxiv-style arXiv paper-reading workspace.**
> L35: Little Alphaxiv is a self-hosted reading-and-discussion workspace for arXiv
> L39: right panel — the paper's full text is injected into the conversation, so you

## 星数曲线

```mermaid
xychart-beta
    title "DylanUnicorn/little-alphaxiv 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c204987192bf` · [字段定义](../../DATASET.md)*
