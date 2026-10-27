# eclipse-langium/langium-ai

⭐ 30 · TypeScript · MIT · 推送 2026-10-16 · [GitHub](https://github.com/eclipse-langium/langium-ai) · 组织维护

**帮助将 LLM 接入 Langium DSL 的工具套件：评测、拆分与 Agent 技能**

围绕 Langium 领域特定语言（DSL）的 AI 工具套件，由三部分组成：核心库 langium-ai-tools 提供 LLM 生成 DSL 代码的校验评测器、按 AST 节点切分文档的 Splitter、语法规则覆盖率分析器、vitest 风格测试 API 与多模型评测矩阵；CLI（lai）驱动 init→生成描述符→生成系统提示词→评测→分析的迭代流程；另附带面向编码代理（Claude Code、Codex 等）的 Agent 技能，可生成 MCP 服务器将 DSL 解析器与校验器暴露为工具。以 npm 包形式分发，MIT 许可。

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

- LangiumEvaluator 用真实解析器/校验器校验 LLM 生成的 DSL 代码并输出结构化诊断与评分
- lai CLI 驱动 init→gen descriptor→gen sysprompt→evaluate→analyze 的迭代流程
- 按 AST 节点类型切分 DSL 文档以供向量库等管道摄取
- Agent 技能可生成将 DSL 解析器/校验器暴露为工具的 MCP 服务器

## 适用场景

- 为我的 DSL 项目评测不同 LLM 生成代码的语法与语义正确性
- 迭代优化面向 DSL 的系统提示词并跟踪评测结果
- 让编码代理通过技能和 MCP 服务器理解并校验我的 DSL

## 场景标签

`模型评测` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L14: Langium AI is a suite of tools that make it easier to integrate AI applications with Langium DSLs. It provides a co
> L35: - **Evaluator** (`LangiumEvaluator`) — validates LLM-generated DSL code against your real parser and validator, ret

## 星数曲线

```mermaid
xychart-beta
    title "eclipse-langium/langium-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e07f347e8bf1` · [字段定义](../../DATASET.md)*
