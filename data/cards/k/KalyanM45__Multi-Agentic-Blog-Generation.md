# KalyanM45/Multi-Agentic-Blog-Generation

⭐ 34 · Python · MIT · 推送 2026-04-10 · [GitHub](https://github.com/KalyanM45/Multi-Agentic-Blog-Generation) · [官网](https://kalyanm45.github.io/BlogBoard-AI-Blog-Generator/) · 个人维护

**自动生成并发布技术博客文章的 AI 写作平台**

BlogBoard 是端到端自动化博客平台：通过 LangGraph 执行有状态工作流，调用 Groq 的 LLM 推理，自主调度、撰写、排版并发布关于机器学习与人工智能的技术文章，经 GitHub Actions 部署到静态前端网站，动态渲染 Markdown 内容。本地运行需 Python 3.12+、langgraph/groq/python-dotenv 依赖（用 uv 管理），并要求配置 Groq API Key（.env 文件中的 GROQ_API_KEY）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph 有状态工作流驱动文章生成流程
- 接入 Groq LLM 推理生成技术文章
- GitHub Actions 自动部署到静态前端，动态渲染 Markdown
- 提供 git clone + uv 依赖安装的本地运行步骤

## 适用场景

- 自动生成 ML/AI 技术文章并发布到博客站点
- 本地搭建自动化 AI 写作与发布流水线
- 学习 LangGraph 与 Groq 集成的多代理工作流项目

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: BlogBoard is an end-to-end, fully automated blogging platform. It autonomously schedules, writes, formats, and publi
> L9: Powered by **LangGraph** for stateful workflow execution and **Groq** for blazing-fast LLM inference, it ensures tha

## 星数曲线

```mermaid
xychart-beta
    title "KalyanM45/Multi-Agentic-Blog-Generation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `172a8ba93e05` · [字段定义](../../DATASET.md)*
