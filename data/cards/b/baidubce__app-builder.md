# baidubce/app-builder

⭐ 587 · Python · Apache-2.0 · 推送 2026-04-26 · [GitHub](https://github.com/baidubce/app-builder) · [官网](https://appbuilder.cloud.baidu.com/) · 组织维护 · 中文 README

**百度千帆AppBuilder客户端SDK，助开发者搭建AI原生应用**

百度智能云千帆 AppBuilder 平台的客户端 SDK（Python 为主，另有 Java/Go 版本与 Docker 镜像），面向 AI 原生应用开发者。功能覆盖：调用千帆平台大模型与 40+ 百度生态能力组件、通过 AppBuilderClient 访问网页端发布的 AI 原生应用、KnowledgeBase 知识库管理（文档增删改查）、基于 Message/Component/AgentRuntime 的工作流编排、Tracing 监控，以及部署为 Flask/gunicorn API 服务、Chainlit 前端或百度云公有云服务。提供覆盖文档解析、切片、向量化、检索、答案生成的 RAG 组件表。使用需个人 Token，组件调用前需申领试用额度。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用千帆平台大模型与 40+ 百度生态能力组件
- KnowledgeBase 知识库管理与 RAG 全流程原子组件（解析/切片/向量化/检索/生成）
- AgentRuntime 支持部署为 Flask/gunicorn API 服务或 Chainlit 交互前端
- appbuilder_bce_deploy 一键部署到百度云提供公网 API

## 适用场景

- 用 Python 代码搭建产业级 RAG 应用
- 纯代码态构建带 FunctionCall 与自定义工作流的 Agent 应用
- 将网页端发布的 AI 原生应用通过 SDK 集成到自有系统

## 场景标签

`RAG` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: 百度智能云千帆AppBuilder-SDK是百度智能云千帆AppBuilder面向AI原生应用开发者提供的一站式开发平台的客户端SDK。
> L15: 百度智能云千帆AppBuilder-SDK提供了以下AI应用开发者的必备功能：

## 星数曲线

```mermaid
xychart-beta
    title "baidubce/app-builder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 586 --> 588
    line [587, 587]
```

2026-10-18 587 → 2026-10-23 587（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3e53744284df` · [字段定义](../../DATASET.md)*
