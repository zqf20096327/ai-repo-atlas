# aaronsb/texflow-mcp

⭐ 20 · Python · MIT · 推送 2026-03-05 · [GitHub](https://github.com/aaronsb/texflow-mcp) · 个人维护

**带 MCP 接口的 LaTeX 文档编译器，供 AI agent 撰写文档**

通过 MCP 协议向 AI agent 暴露 LaTeX 文档创作工具：agent 在结构化文档模型（章节、段落、图表、公式）上操作，TeXFlow 负责宏包、导言区、字体与编译等 LaTeX 机制。提供创建骨架与 markdown 导入两种入口，模型以 JSON 自动保存，LaTeX 仅作为输出产物；提供 6 个工具（document/layout/edit/render/reference/queue）可编译 PDF、页面预览 PNG 与导出 .tex。XeLaTeX 与 poppler-utils 为可选系统依赖，缺省仍可导出 .tex。

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

- 结构化文档模型操作，LaTeX 仅作为输出产物
- markdown 导入与文档骨架两种入口流程
- 编译 PDF、页面 PNG 预览、导出 .tex
- reference 工具可检索 LaTeX 命令、符号、宏包与错误帮助

## 适用场景

- 让 Claude 等 agent 通过 MCP 直接撰写和排版 LaTeX 论文
- 把 markdown 稿件导入后由 agent 调整版式并编译 PDF
- 批量操作文档块并导出 .tex 成品

## 场景标签

 · 领域:文档排版/agent 工具

## 证据(README 行号)

> L7: A LaTeX document compiler with an MCP interface. AI agents operate on a structured document model — sections, paragr
> L61: TeXFlow has two entry flows, both converging on the same in-memory document model:

## 星数曲线

```mermaid
xychart-beta
    title "aaronsb/texflow-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e86f4877bc34` · [字段定义](../../DATASET.md)*
