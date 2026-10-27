# ChenGan666/ZSN.AgentBrook

⭐ 23 · C# · MIT · 推送 2026-10-26 · [GitHub](https://github.com/ChenGan666/ZSN.AgentBrook) · [官网](https://agentbrook.com) · 个人维护 · 中文 README

**企业级 AI 智能体编排平台：可视化工作流+RAG+MCP**

基于 .NET 10 与 Semantic Kernel 的 AI 智能体编排平台，提供可视化 DAG 工作流引擎（20+ 节点类型、条件分支、人工审批、AI 自动生成下游节点链）、混合检索 RAG 知识库（pgvector + 全文检索 + Apache AGE 知识图谱 + 图片 VLM/OCR）、ClawAI Plan-Execute-Reflect 智能体、ServiceDesk 客服节点、基于 SearXNG+Playwright 的自主研究节点、FunASR 本地语音转写、IM 消息网关（企业微信/钉钉/飞书/WhatsApp）与 MCP Server/Client。支持 OpenAI/Claude/DeepSeek/Ollama/智谱/百度等多模型接入，附带 Vue3+Tauri 跨平台客户端与应用工厂打包服务。需从源码以 dotnet 运行，依赖 MySQL/PostgreSQL/Redis 等外部服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可视化 DAG 工作流引擎，20+ 节点类型，AI 三阶段流水线自动生成下游节点链
- 混合检索 RAG 知识库：pgvector 向量 + 全文 + Apache AGE 知识图谱，图片 VLM 描述与 OCR
- 内置 MCP Server/Client 双向调用
- 多模型支持且每个工作流节点可独立配置模型与参数

## 适用场景

- 拖拽编排带人工审批与子工作流的 AI 业务流程
- 搭建带知识库来源引用的智能客服
- 自动多轮搜索抓取并生成研究报告
- 把 App 配置编译为独立分发的桌面/Web 客户端

## 场景标签

`工作流自动化` `RAG` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: **企业级 AI 智能体编排平台**
> L30: - **可视化 DAG 工作流引擎** — 拖拽式设计器，20+ 节点类型，支持条件分支、并行执行、人工审批、子工作流嵌套，**AI 自动生成下游节点链**
> L324: 通过统一的 `IChatService` 接口对接多种 AI 提供商：

## 星数曲线

```mermaid
xychart-beta
    title "ChenGan666/ZSN.AgentBrook 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `cb1de2d0369c` · [字段定义](../../DATASET.md)*
