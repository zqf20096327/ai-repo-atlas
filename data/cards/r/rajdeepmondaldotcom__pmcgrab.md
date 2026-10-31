# rajdeepmondaldotcom/pmcgrab

⭐ 24 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/rajdeepmondaldotcom/pmcgrab) · [官网](https://rajdeepmondaldotcom.github.io/pmcgrab/) · 个人维护

**给生医 AI/RAG 管线的 PMC 文献解析库：PMC ID 进、干净论文 JSON 出**

Python 库与 CLI：读取 PubMed Central 文章与 JATS XML（按 PMCID/PMID/DOI 联网获取，或解析本地 XML 文件），输出结构化的论文 JSON，默认含标题、摘要、正文、图表；溯源、关系图、诊断等字段需显式请求 full JSON。可选下载图片文件（默认关闭，走 PMC OA 包并回退逐文件 URL），未知 JATS 块以可读回退记录保留而非丢弃。面向生物医学 RAG、搜索、文本挖掘与知识图谱等文献摄取管线的开发者，需 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PMCID/PMID/DOI/本地 XML 多种输入模式，支持多进程批量解析
- 默认输出干净论文 JSON，full 模式提供溯源、关系图与诊断字段
- 可选图片/补充文件下载，含 tar 路径检查与大小上限等安全默认
- 未知 JATS 内容保留为可读回退记录，不静默丢弃

## 适用场景

- 为生物医学 RAG 或搜索系统批量准备干净的论文全文语料
- 把 PubMed Central 开放获取文章连同图片一起摄取进知识库
- 本地已下载的 JATS XML 批量转结构化 JSON 供下游文本挖掘

## 场景标签

`RAG` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L11: PMCGrab turns PubMed Central articles and JATS XML into structured JSON for
> L17: Use it when you need clean article context for RAG, search, text mining,

## 星数曲线

```mermaid
xychart-beta
    title "rajdeepmondaldotcom/pmcgrab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2a7b5c7bd9ec` · [字段定义](../../DATASET.md)*
