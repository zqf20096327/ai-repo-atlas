# timothywarner-org/context-engineering

⭐ 27 · Python · MIT · 推送 2026-09-19 · [GitHub](https://github.com/timothywarner-org/context-engineering) · [官网](https://techtrainertim.com) · 个人维护

**MCP 上下文工程教学仓库：语义记忆课程与配套教学应用**

由 Microsoft MVP Tim Warner 维护的培训仓库，教授基于 Model Context Protocol (MCP) 构建生产形态的 AI 语义记忆系统，技术栈为 Python、FastAPI、FastMCP 与 LangGraph。核心是旗舰教学应用 WARNERCO Schematica：实现 CoALA 四层记忆（工作/情景/语义/程序性），采用 9 节点 LangGraph 流水线，注册 28 个 MCP 工具、12 个资源与 5 个提示，含渐进式工具加载。另提供 4 个实验（含 JS Hello MCP、Azure 远程 MCP + OAuth）与 4 份 Jupyter 教学笔记本。需 Python 3.13、Node.js 20+ 与 Anthropic API key（缺失时降级）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WARNERCO 教学应用实现 CoALA 四层记忆与 9 节点 LangGraph 流水线
- 注册 28 个 MCP 工具、12 个资源、5 个提示，含渐进式工具加载元工具
- 4 个实验覆盖 JS MCP 入门、Python REPL 客户端、MCP Apps UI 与 Azure OAuth 远程部署
- 含 117 实体/221 关系的知识图谱与情景记忆评分公式（可查看逐事件分值）

## 适用场景

- 按 4×50 分钟课程结构学习 MCP 与上下文工程
- 在 Claude Desktop/Claude Code/VS Code Copilot 中接入 WARNERCO 记忆服务器做实验
- 参考 CoALA 记忆分层与渐进式工具加载的实现方式

## 场景标签

`教程课程` `Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L5: Welcome to the training hub for mastering **Context Engineering with Model Context Protocol (MCP)**. This course tea
> L60: ## Course Structure (4 x 50 Minutes)

## 星数曲线

```mermaid
xychart-beta
    title "timothywarner-org/context-engineering 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `347b03008e3f` · [字段定义](../../DATASET.md)*
