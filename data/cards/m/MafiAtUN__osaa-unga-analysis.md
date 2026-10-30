# MafiAtUN/osaa-unga-analysis

⭐ 15 · Python · MIT · 推送 2025-11-07 · [GitHub](https://github.com/MafiAtUN/osaa-unga-analysis) · [官网](https://deepwiki.com/MafiAtUN/osaa-unga-analysis) · 组织维护

**联合国大会演讲 AI 分析平台，产出每日分析报告**

面向联合国 OSAA 政府间团队的 Streamlit 应用：内置 1946-2025 年 11,093 篇联大演讲语料库（199 国、全量 embeddings），支持用多种 LLM（GPT-4、Claude 等）对演讲做 AI 分析，产出情感分析、主题提取、文档分类与交叉引用分析；提供跨 80 年趋势分析、文档上传（PDF/DOCX/MP3）、数据库对话与可视化。含用户认证与角色权限管理，自动区分非洲成员国与发展伙伴。需配置 OpenAI API key 并初始化本地数据库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11,093 篇演讲（1946-2025、199 国）内置语料库，100% embeddings 覆盖语义搜索
- 多模型 AI 分析：情感分析、主题提取、文档分类、交叉引用
- 支持上传 PDF/DOCX/MP3 文档并结合上下文分析
- 用户认证、角色权限与管理员门户

## 适用场景

- 分析成员国联大演讲并生成对齐 OSAA 优先事项的分析报告
- 跨年份追踪特定议题或国家的发言趋势
- 对非洲成员国与发展伙伴的立场做对比分析
- 通过对话直接查询联大演讲数据库

## 场景标签

`语义搜索` `数据分析` `文档问答` · 领域:效率与自动化

## 证据(README 行号)

> L11: The UNGA Analysis App is a comprehensive platform for analyzing United Nations General Assembly speeches from 1946 
> L22: - **New Analysis**: AI-powered speech analysis with multiple models
> L37: - Multiple AI model support (GPT-4, Claude, etc.)

## 星数曲线

```mermaid
xychart-beta
    title "MafiAtUN/osaa-unga-analysis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `250cd376eed3` · [字段定义](../../DATASET.md)*
