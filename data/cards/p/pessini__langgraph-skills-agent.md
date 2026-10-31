# pessini/langgraph-skills-agent

⭐ 14 · Python · Apache-2.0 · 推送 2026-05-31 · [GitHub](https://github.com/pessini/langgraph-skills-agent) · [官网](https://medium.com/@pessini/stop-stuffing-your-system-prompt-build-scalable-agent-skills-in-langgraph-a9856378e8f6) · 个人维护

**博客配套示例：用技能模块化构建可扩展的 LangGraph Agent**

Medium 文章《Stop Stuffing Your System Prompt》的配套演示仓库：在 LangGraph 上实现渐进式知识加载、按领域拆分的 Agent Skills、工具驱动的技能激活。代码已演进为可复用的异步 BaseAgent（含 LLM 重试分类、工具调用配对安全、Langfuse 管理的提示词），通过 LangGraph 本地 dev server 运行与测试，仅保留图代码与单元测试。配置 OPENAI_API_KEY 或使用 Ollama 默认值。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 渐进式知识加载与技能驱动的领域模块化
- 可复用异步 BaseAgent：重试分类与工具调用配对安全
- 通过 LangGraph 本地 dev server 运行，Langfuse 管理提示词
- 提供 make install/dev/test 工作流与 SDK 冒烟测试

## 适用场景

- 参考系统提示词过长问题的技能化拆分方案
- 学习 LangGraph StateGraph、interrupt/resume 等机制
- 复用 BaseAgent 构建带重试与工具安全的 Agent

## 场景标签

`Agent 框架` `提示工程` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L17: This repo is a LangGraph application. The local code is:
> L3: Demo from the Medium article: Stop Stuffing Your System Prompt: Build Scalable Agent Skills in LangGraph.

## 星数曲线

```mermaid
xychart-beta
    title "pessini/langgraph-skills-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `cc4c19bc77db` · [字段定义](../../DATASET.md)*
