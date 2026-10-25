# seehiong/multi-agent-system-using-langgraph

⭐ 42 · Jupyter Notebook · MIT · 推送 2025-12-04 · [GitHub](https://github.com/seehiong/multi-agent-system-using-langgraph) · [官网](https://seehiong.github.io/posts/2025/11/building-a-langgraph-multi-agent-system/) · 个人维护

**博客配套的 LangGraph 多智能体系统示例仓库**

随博客文章发布的完整示例代码与 Jupyter notebooks：演示三种形态——确定性链条（TOTO 号码生成）、带 Postgres（经 MCP Toolbox）、Tavily 搜索与自定义 Python 工具的 ReAct agent，以及由 Supervisor 调度 SQL Agent、Amenities Agent 与 Web Research Agent 的多智能体系统。模型经 OpenRouter 接入。依赖 Python 3.10+、uv、Postgres（HDB 示例需），Tavily API key 可选。可用 langgraph dev 在 LangSmith Studio 中调试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种示例：确定性链、ReAct agent、Supervisor 多智能体系统
- 经 MCP Toolbox 接入 Postgres SQL 工具，含新加坡 HDB 数据集查询
- 可复现的 Jupyter notebooks 与 tools.yaml 工具配置
- 支持 langgraph dev 在 LangSmith Studio 中调试图结构

## 适用场景

- 跟随博客学习 LangGraph 多智能体系统搭建
- 参考 Supervisor 调度多个专业 agent 的实现方式
- 了解 MCP Toolbox 接 Postgres 作为 agent 工具的做法

## 场景标签

`多智能体` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L3: This repository contains the full source code and Jupyter notebooks for my blog post **“Building a LangGraph Multi-A
> L69: 1. **toto_generator.ipynb**
> L75: 3. **langgraph_mas.ipynb**

## 星数曲线

```mermaid
xychart-beta
    title "seehiong/multi-agent-system-using-langgraph 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-25 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `ac2f2edd019f` · [字段定义](../../DATASET.md)*
