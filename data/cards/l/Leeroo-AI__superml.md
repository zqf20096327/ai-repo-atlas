# Leeroo-AI/superml

⭐ 196 · Python · Apache-2.0 · 推送 2026-03-17 · [GitHub](https://github.com/Leeroo-AI/superml) · [官网](https://leeroo.com/) · 组织维护

**给 AI 编程 agent 加持 ML 工程技能与知识库的插件**

面向 Claude Code、Cursor、Codex、OpenCode、Gemini CLI 等 AI 编程 agent 的插件：提供 7 个 ML 工作流技能（规划/校验/调试/迭代/实验追踪等）、一个跨会话记忆实验的持久 agent（ml-expert），以及基于 Leeroopedia（27k+ 页 ML/AI 框架文档）的 MCP 知识库工具，使 agent 回答时引用真实文档。无 API key 也可用（走 web search），带 API key 可访问知识库。另提供仅接入 MCP 工具的远程安装方式与针对特定领域优化技能的 self-refine 工具包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个 ML 工作流技能（ml-plan/ml-verify/ml-debug/ml-iterate/ml-experiment/ml-research/using-superml）
- Leeroopedia 知识库：1000+ 框架、27k+ 页文档，经 MCP 工具查询并引用出处
- 跨会话记忆硬件配置、实验与经验教训的 ml-expert 持久 agent
- 支持 5 种编程 agent（Claude Code/Cursor/Codex/OpenCode/Gemini CLI）

## 适用场景

- 让编程 agent 按真实框架文档规划训练配置并避免常见错误
- 调试 OOM/NaN/发散等 ML 训练问题并按根因分析
- 跨会话追踪实验假设与结果，避免重复失败实验

## 场景标签

`MLOps` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L19: It adds two things your coding agent doesn't have:
> L31: 3. **MCP tools** connect to the Leeroopedia knowledge base, your agent looks things up and cites real docs instead 
> L25: Works with Claude Code, Cursor, Codex, OpenCode, and Gemini CLI.

## 星数曲线

```mermaid
xychart-beta
    title "Leeroo-AI/superml 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 194 --> 197
    line [195, 196, 196]
```

2026-10-18 195 → 2026-10-24 196（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f47204128923` · [字段定义](../../DATASET.md)*
