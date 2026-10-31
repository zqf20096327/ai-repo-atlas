# isakskogstad/Skolverket-MCP

⭐ 13 · TypeScript · MIT · 推送 2026-04-22 · [GitHub](https://github.com/isakskogstad/Skolverket-MCP) · [官网](https://skolverket-mcp.onrender.com/) · 个人维护

**瑞典教育署开放数据的 MCP 服务器：让 AI 助手查询课纲与学校数据**

面向瑞典国家教育署（Skolverket）三个公开 API 的 Model Context Protocol 服务器，通过 stdio 传输接入 Claude Desktop、Claude Code、OpenAI Codex、Gemini、Cursor 等 MCP 客户端。实现 41 个工具（覆盖 Läroplan 课纲 API、学校单位登记、职业教育计划 API）、4 个资源和 5 个提示模板，供教师、学生及研究者以自然语言检索、比较与分析瑞典教育数据。从源码安装（git clone + npm install + build），运行需 Node.js。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对接 Skolverket 三个公开 API，提供 41 个 MCP 工具
- 支持 Claude Desktop/Code、Codex、Gemini、Cursor 等客户端的 stdio 接入配置
- 含 4 个资源与 5 个提示模板（课程分析、版本比较、升学指导等）

## 适用场景

- 教师做课程规划与知识要求比较
- 学生和家长比较高中项目与选课
- 检索学校名录与课纲演变分析

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L9: En Model Context Protocol (MCP) server som ger AI-assistenter tillgång till **alla Skolverkets öppna API:er** – Läro
> L13: Installera lokalt enligt guide nedan. Servern körs via stdio-transport och integreras sedan i din MCP-klient (Claud

## 星数曲线

```mermaid
xychart-beta
    title "isakskogstad/Skolverket-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f5f8ec4ed48f` · [字段定义](../../DATASET.md)*
