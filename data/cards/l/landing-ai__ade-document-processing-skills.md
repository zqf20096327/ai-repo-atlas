# landing-ai/ade-document-processing-skills

⭐ 69 · MIT · 推送 2026-10-14 · [GitHub](https://github.com/landing-ai/ade-document-processing-skills) · 组织维护

**教编程 Agent 调用 LandingAI ADE 做文档解析抽取的技能包**

面向 Agent Skills 规范的 agent 技能：教会 Claude、Cursor、Roo Code 等编程助手通过 ADE REST API 或官方 Python/TypeScript 库对文档执行解析、字段抽取、分类、拆分，并组合为批处理、先分类后抽取、RAG 准备等流水线；抽取结果带边界框与页码可回溯。需 LandingAI 的 VISION_AGENT_API_KEY（含免费试用），支持 20+ 文件格式，无需模板或模型训练。以 Claude Code 插件市场或手动克隆方式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 解析/抽取/分类/拆分四大文档操作与组合流水线模式
- 抽取值附带边界框与页码，可回溯源文档
- RAG 准备模式：语义分块、embedding、向量库导入
- 支持 Claude Code 插件市场一键安装

## 适用场景

- 让编程助手批量解析发票并导出 CSV
- 混合文档按类型先分类再抽取字段
- 为 RAG 流水线做语义分块与向量库导入

## 场景标签

`文档解析` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: An agent skill for LandingAI's Agentic Document Extraction (ADE): production-ready document AI that converts complex
> L7: The skill teaches agentic coding assistants (Claude, Cursor, Roo Code, or any agent supporting the Agent Skills conv

## 星数曲线

```mermaid
xychart-beta
    title "landing-ai/ade-document-processing-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-18 69 → 2026-10-24 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bb7c8fdd3170` · [字段定义](../../DATASET.md)*
