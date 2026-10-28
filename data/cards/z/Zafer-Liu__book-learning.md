# Zafer-Liu/book-learning

⭐ 45 · Python · GPL-3.0 · 推送 2026-10-21 · [GitHub](https://github.com/Zafer-Liu/book-learning) · 个人维护 · 中文 README

**自托管多账户教材 RAG 学习助手，回答必须引用原文**

基于 Flask + SQLite 的自托管学习工作区：上传 Markdown/TXT/DOCX 教材，分块索引后提供问答、章节讲解、要点提纲与自测四种模式。检索走词法/FTS5/向量三通道，RRF 融合；回答中每个声明需携带 C（教材）/W（网络）引用标签，服务端校验，无证据或编造标签的回答整体拒绝且不保存。附带批注阅读器、长对话自动压缩、可选联网补充（智谱 web-search-pro 或远程 MCP）与 Anki 导出。数据按账户和书隔离，单实例部署（1 个 Gunicorn worker），GPL-3.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- C/W 双轨引用校验：无证据或编造标签的回答整体拒绝
- 三通道检索（词法/FTS5/向量）RRF 融合，无嵌入服务时降级为关键词检索
- 四种学习模式：问答、章节讲解、要点提纲、自测（可导出 Anki CSV）
- 长对话服务端自动压缩与上下文计量条；可选联网补充默认关闭

## 适用场景

- 把自己的教材传上去，通过带引用的问答定位原文出处
- 边读边批注并就选中段落提问或生成自测题
- 为班级或小组部署多账户学习工作区（注册码/邀请码控制）

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L12: Book Learning (「书内」, a.k.a. BOOKNOTE) is a self-hostable, multi-account textbook study workspace: upload Markdown /
> L74: - **Evidence-constrained generation** — as in Diagram 4: answers must stand on this turn's retrieved evidence; othe

## 星数曲线

```mermaid
xychart-beta
    title "Zafer-Liu/book-learning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-28 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `74d6a97fed35` · [字段定义](../../DATASET.md)*
