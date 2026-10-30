# microsoft/agentic-sdlc-starter

⭐ 20 · Shell · 推送 2026-04-08 · [GitHub](https://github.com/microsoft/agentic-sdlc-starter) · 组织维护

**规范驱动的 AI 辅助软件开发参考架构（5 步流水线）**

微软维护的参考架构仓库：以 GitHub Copilot 为代码生成引擎，通过 5 个专用 agent 提示词将 PRD、技术设计文档与用户故事分步转化为生产可用的代码。流程含评估器（分析输入找缺口）、解析器（消解歧义）、规格生成器、代码生成器与校验器；生成器只读规格文件与 copilot-instructions，不直接读 PRD/TDD。配置以 bootstrap 脚本一次性替换占位符，提示词与技术栈无关，默认示例为 Python/FastAPI/Neo4j。需在 Copilot Chat 或任意有文件访问能力的 LLM 中手动逐步运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 步 agent 提示词流水线：PRD+用户故事→代码
- 零假设原则：所有歧义在生成前标记并消解
- 生成器仅读规格与 copilot-instructions，规格之外不构建
- 提示词与技术栈无关，仅守护文件绑定具体栈

## 适用场景

- 团队以规格驱动方式用 AI 生成结构化代码
- 将 PRD 与用户故事按固定流程转化为可评审的代码产出
- 为不同行业合规要求定制 AI 编码守护规则

## 场景标签

`提示工程` `代码生成` · 领域:Agent 开发

## 证据(README 行号)

> L3: Reference architecture for spec-driven, AI-assisted software development using GitHub Copilot, MCP, and repo-based c
> L7: A 5-step AI pipeline that turns **PRD + User Stories → Production-Ready Code** using GitHub Copilot as the code gene
> L76: Run each prompt sequentially in GitHub Copilot Chat (or any LLM with file access):

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/agentic-sdlc-starter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `43ab912a0b17` · [字段定义](../../DATASET.md)*
