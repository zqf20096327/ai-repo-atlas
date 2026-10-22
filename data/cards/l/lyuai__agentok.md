# lyuai/agentok

⭐ 424 · TypeScript · NOASSERTION · 推送 2026-07-08 · [GitHub](https://github.com/lyuai/agentok) · [官网](http://studio.agentok.ai/) · 个人维护

**可视化拖拽构建 AG2 多智能体应用并生成 Python 代码的 Studio**

基于 AG2（前 AutoGen）的图形化开发工具：用户在画布上以节点和连线编排智能体会话关系（群聊、顺序聊天），在边上配置工具调用，经代码生成器产出依赖极少的自包含 Python 代码，可在任意环境作为普通程序执行，目标为 ag2 1.0 API。提供工具编辑器、流程数据可视化与 AG2 执行原始日志查看；RAG 功能已移除。前端为 Next.js，后端 API 可经 Docker 或 Poetry 本地运行，使用 Supabase 做认证与存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图编排→原生自包含 Python 代码生成（目标 ag2==1.0.0b0）
- 会话关系可视化（群聊/顺序聊天）与边级工具配置
- 工具编辑器与变量配置
- 附带 AG2 执行原始 stdout/stderr 日志

## 适用场景

- 不写样板代码，拖拽搭建多智能体会话工作流
- 诊断和调试 AG2 多智能体流程的执行过程
- 导出独立 Python 代码部署到任意环境

## 场景标签

`多智能体` `代码生成` · 领域:Agent 开发

## 证据(README 行号)

> L3: **AG2 Visualized - Build Agentic Apps with Drag-and-Drop Simplicity.**
> L24: Agentok Studio is a tool built upon AG2 (Previously AutoGen), a powerful agent framework from Microsoft and a vibra
> L54: We strive to create a user-friendly tool that generates native Python code with minimal dependencies. Simply put, A

## 星数曲线

```mermaid
xychart-beta
    title "lyuai/agentok 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 423 --> 425
    line [424, 424]
```

2026-10-18 424 → 2026-10-22 424（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `4aee42669ff8` · [字段定义](../../DATASET.md)*
