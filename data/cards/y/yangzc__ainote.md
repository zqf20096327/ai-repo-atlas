# yangzc/ainote

⭐ 25 · JavaScript · MIT · 推送 2026-08-12 · [GitHub](https://github.com/yangzc/ainote) · 个人维护 · 中文 README

**自托管 AI Agent 工作流平台：可视化编排、知识库 RAG、数字员工**

面向构建智能应用的开源自托管平台：提供可视化工作流编辑器（分支/循环/AI 节点）、拖拽式表单构建器（16+ 字段类型）与数据管理；知识库支持文档摄取、pgvector 向量检索与 RAG 流水线；多模型 LLM 接入（OpenAI、DeepSeek、Qwen、OneAPI 代理）。数字员工可通过 iframe/JS SDK 嵌入第三方站点，或经钉钉、企微等网关渠道对话。提供 Tauri 桌面客户端与多租户组织管理。部署方式包括 GHCR 预构建镜像、源码 Docker Compose 与裸机手动安装；裸机需 Node.js≥20、pnpm≥8、PostgreSQL≥15（pgvector 扩展），Temporal 为推荐组件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可视化工作流编辑器（分支、循环、AI 节点）
- 知识库 RAG：文档摄取 + pgvector 向量检索
- 数字员工可经 iframe/JS SDK 嵌入或钉钉/企微渠道对话
- GHCR 预构建镜像一条 Docker 命令部署

## 适用场景

- 搭建带知识库问答的智能客服数字员工
- 通过拖拽方式编排 AI 工作流并发布表单收集数据
- 在钉钉/企微内接入 AI 对话机器人

## 场景标签

`工作流自动化` `聊天机器人` `RAG` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: An AI agent workflow platform for building intelligent applications with visual flow orchestration, knowledge bases
> L34: - **Visual Workflow Editor** — Drag-and-drop flow builder with branching, loops, and AI nodes
> L46: - **AI Agent Studio** — Multi-model LLM integration (OpenAI, DeepSeek, Qwen, etc.), tool orchestration

## 星数曲线

```mermaid
xychart-beta
    title "yangzc/ainote 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `c08abdcc661a` · [字段定义](../../DATASET.md)*
