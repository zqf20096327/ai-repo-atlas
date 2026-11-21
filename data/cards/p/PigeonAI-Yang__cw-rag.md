# PigeonAI-Yang/cw-rag

⭐ 4 · Python · 推送 2026-10-14 · [GitHub](https://github.com/PigeonAI-Yang/cw-rag) · 个人维护 · 中文 README

**给冒险岛经典世界玩家的本地客户端数据检索 Codex Skill**

CW RAG 是供 Codex 使用的本地 Skill：把 MapleStory Classic World 客户端静态数据（怪物、地图、装备、技能、任务等）导入为 SQLite 快照，用 FTS5 做文本检索、SQL 读结构字段与静态关系。不含模型 API、不使用 embeddings 或向量库，答案由用户所接的 AI 根据检索结果组织。客户端文件只读，查询仅读本地快照、不发起网络请求。安装需 Windows PowerShell 与 Python 3.10+，另含按每秒经验排序的练级子 Skill。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将客户端数据建立 SQLite 快照，FTS5 文本检索加 SQL 读取结构字段
- 不调用模型 API、不使用 embeddings 或向量数据库
- 查询仅读取本地快照，不联网、不上传客户端文件
- 支持中文提问，将中文概念改写为英文来源词或使用 ID

## 适用场景

- 让 Codex 根据本地客户端数据比较武器属性与需求
- 按怪物等级与地图位置找练级路线
- 查询技能前置和任务关联 NPC

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L9: CW RAG（Classic World RAG）是一个供 Codex 使用的本地 Skill，用来检索 MapleStory Classic World（冒险岛经典世界）客户端静态数据。它在用户指定目录创建 SQLite 快照。P
> L113: 不包含。CW RAG 用 Python 和 SQLite 检索本地快照。FTS5 用于文本检索，SQLite 查询用于读取结构字段和静态关系。CLI 不调用模型 API，也不依赖 embeddings 或向量数据库。由你使用的 

## 星数曲线

```mermaid
xychart-beta
    title "PigeonAI-Yang/cw-rag 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-11-08", "2026-11-21"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-19 3 → 2026-11-21 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `e15ac7c12ce3` · [字段定义](../../DATASET.md)*
