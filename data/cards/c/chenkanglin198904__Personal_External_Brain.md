# chenkanglin198904/Personal_External_Brain

⭐ 200 · Python · MIT · 推送 2026-09-29 · [GitHub](https://github.com/chenkanglin198904/Personal_External_Brain) · 个人维护 · 中文 README

**本地优先的个人知识图谱工具：从笔记/网页/PDF/音视频构建可溯源召回**

运行于本地的个人知识管理工具：将笔记、网页、Markdown、PDF（含扫描件）、音频/视频摄入并挂载到个人知识图谱（Kuzu 图数据库 + LanceDB 向量库，Python 后端 + React 前端）。核心机制包括主题隔离召回、每条事实置信度评分、声明须匹配原文 source_span、以拒答率为质量指标、决策与结果回写闭环；明确不做图外生成的通用助手，未承诺自动抽象与云端多用户同步。提供 Docker Compose 与源码两种运行方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多格式摄入（笔记/网页/PDF/音视频）并自动链接入图谱
- 主题隔离召回与单条事实置信度评分
- 声明须匹配原文 source_span，拒答率为质量指标
- 决策记录与真实结果回写，形成反馈闭环

## 适用场景

- 把读过的研究/会议/对话内容沉淀为可溯源的个人知识图谱
- 需要带原始出处和上下文的精确召回，而非全文搜索
- 记录决策及其后续结果，供下次类似问题参考

## 场景标签

`知识图谱` `知识库管理` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L28: - Multi-format ingestion: notes, web pages, Markdown, PDFs, audio/video automatically extracted and linked into the
> L65: - **Ingest**: scratch notes, web pages, Markdown, PDF (including scans), audio, video. Five gates refuse listicles 
> L78: - Not a ChatGPT wrapper. It does not invent an encyclopedia off-graph.

## 星数曲线

```mermaid
xychart-beta
    title "chenkanglin198904/Personal_External_Brain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 199 --> 201
    line [200, 200]
```

2026-10-18 200 → 2026-10-23 200（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d430c1eee4e0` · [字段定义](../../DATASET.md)*
