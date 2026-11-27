# Tencent/WeKnora

⭐ 38,291 · Go · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/Tencent/WeKnora) · [官网](https://weknora.weixin.qq.com) · 组织维护 · 中文 README

**企业文档知识平台：RAG 问答、推理 Agent 与自维护 Wiki**

腾讯开源的 LLM 知识框架，面向企业文档理解、语义检索与推理。同一知识库支撑三种模式：带混合检索、多模态解析与引用的 RAG 问答；具备多步推理、技能沙箱、MCP 工具与本地浏览器操作的 Agent；以及带知识图谱与回滚的 Wiki。支持飞书/Confluence/Notion 等数据源自动同步与 10+ 文档格式，多工作区 RBAC，模型目录内置 31 个供应商，LLM、向量库与存储后端可替换。部署需 Docker/Docker Compose，另有 Kubernetes Helm、Lite 单二进制与桌面应用（源码构建）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 38,254 位贡献者
- 涨星:近 1 天 **+175**(自 20261016 起算)
- 平台:— · 协议:OPENAI-API / MCP / OLLAMA

## 能力要点

- RAG/Agent/Wiki 三种模式共享同一知识库
- 技能从 ClawHub/Git/ZIP 安装，运行于 Docker/E2B/Cube 沙箱
- 数据源自动同步（飞书/Confluence/Notion 等）与 10+ 文档格式解析
- 内置 MCP Server，可发布知识库给 Cursor、Claude 等工具

## 适用场景

- 把团队文档接入可引用出处的 RAG 问答
- 让 Agent 执行多步知识任务并操作浏览器
- 将文档组织成带知识图谱的 Wiki
- 在私有环境部署企业知识库并对接 IM 渠道

## 场景标签

`RAG` `聊天机器人` `文档问答` `知识图谱` · 领域:对话与助手

## 证据(README 行号)

> L32: WeKnora is an open-source, LLM-powered knowledge framework for enterprise document understanding, semantic retrieva
> L40:  01 RAG: answers you can check, with hybrid search, multimodal parsing and citations. 02 Agent: tasks done with kno
> L49: - **Models**: 31 built-in vendors with a generated model catalog, including OpenAI, DeepSeek, Qwen (Alibaba Cloud),

## 星数曲线

```mermaid
xychart-beta
    title "Tencent/WeKnora 星数(近 27 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 34998 --> 38590
    line [35297, 35379, 35542, 35650, 35773, 35911, 36051, 36117, 36179, 35297, 36824, 37106, 37201, 37314, 37394, 37428, 37471, 37547, 37660, 37750, 37812, 37901, 37953, 38000, 38087, 38216, 38291]
```

2026-10-25 35,297 → 2026-11-27 38,291（+2,994）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `b30b71a6d790` · [字段定义](../../DATASET.md)*
