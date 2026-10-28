# ApocData/ApocData-skill

⭐ 101 · Shell · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/ApocData/ApocData-skill) · [官网](http://www.apocdata.com) · 组织维护 · 中文 README

**A股金融数据服务：供 AI agent 调用的公告解析与行情 API Skill/MCP**

面向 AI agent 的 A 股数据层：将全市场公告解析为结构化字段（AI 摘要、类别、重要性、情感、来源链接），并提供行情、财务、资金流、龙虎榜、宏观等 11 组共 45 个只读端点。仓库核心是可直接加载进 Claude 等 agent 的 SKILL.md 能力卡，另提供 46 工具的 MCP server 与 OpenAPI 导入路径。免费档免注册可用（每日 2000 次、行情延迟约 15 分钟），注册后解锁更高配额。仅用于研究辅助，非投资建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 公告 PDF 解析为结构化字段：AI 摘要/类别/重要性/情感/来源链接
- 11 组 45 个只读 HTTP 端点，覆盖行情、财务、资金流、龙虎榜、宏观等
- SKILL.md 多文件渐进加载结构，简单查询仅耗约 4K tokens
- MCP server（46 工具）与 OpenAPI 导入（GPT Actions/Dify/Coze/n8n）多种接入方式

## 适用场景

- 让 Claude/ChatGPT 等 agent 直接查询 A 股行情与财务数据
- 获取带 AI 摘要和情感标注的公告结构化数据做研究
- 通过 MCP 或 OpenAPI 把 A 股数据接入量化或投研工作流

## 场景标签

`金融量化` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L17: The `SKILL.md` in this repository is a capability card that can
> L80: - **Multiple integration paths** — Skill package (one-command install), MCP server (46 tools),

## 星数曲线

```mermaid
xychart-beta
    title "ApocData/ApocData-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 100 --> 103
    line [102, 101, 101]
```

2026-10-18 102 → 2026-10-28 101（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `0ca9c272aa48` · [字段定义](../../DATASET.md)*
