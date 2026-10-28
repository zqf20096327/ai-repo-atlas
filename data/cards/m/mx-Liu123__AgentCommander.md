# mx-Liu123/AgentCommander

⭐ 41 · HTML · Apache-2.0 · 推送 2026-04-17 · [GitHub](https://github.com/mx-Liu123/AgentCommander) · 个人维护

**编排 LLM CLI 的图结构工作流引擎，用于 ML 实验迭代**

面向机器学习工程师与科研人员的图结构工作流引擎：通过编排 Gemini CLI、Qwen CLI、Claude Code、OpenCode 等 LLM CLI，构建可自定义的无限循环迭代工作流，自动化 ML 代码的调试与优化循环。Agent 可分析代码与历史结果、修改并调试 strategy.py、解读生成图表、检索 Arxiv/GitHub 获取灵感，并将经验教训持久化到 history.json。提供拖拽式可视化编辑器、进度树可视化、目录级沙箱隔离与 PBS/Slurm 集群模板。需 Python 3.10+，通过 git clone 与 pip 安装，Web UI 运行在 localhost:8080。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 原生集成 Gemini/Qwen/Claude/OpenCode 多种 LLM CLI 后端
- 分层工作流（外层进化策略+内层实验执行）与进度树可视化
- Agent 自主编码调试、多模态图表解读、Arxiv/GitHub 在线检索
- 目录级沙箱隔离、文件系统快照与自动回滚；PBS/Slurm HPC 模板

## 适用场景

- 让 AI 自动迭代优化我的机器学习训练代码
- 科研中自动化调试与实验循环，只定义搜索空间与评估逻辑
- 在 HPC 集群上编排长时间的进化式实验工作流

## 场景标签

`工作流自动化` `编码 Agent` `科研工具` · 领域:效率与自动化

## 证据(README 行号)

> L29: Refined through rigorous practical application, it is a graph-based workflow engine designed to orchestrate AI Agen
> L53: * **Multi-Model Support**: Native integration with Gemini, Qwen, Claude, and OpenCode CLIs. Use the backend that be

## 星数曲线

```mermaid
xychart-beta
    title "mx-Liu123/AgentCommander 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-28 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f6e5a490e15c` · [字段定义](../../DATASET.md)*
