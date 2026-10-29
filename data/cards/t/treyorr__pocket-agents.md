# treyorr/pocket-agents

⭐ 17 · TypeScript · MIT · 推送 2026-05-31 · [GitHub](https://github.com/treyorr/pocket-agents) · 个人维护

**单文件自包含的 agent 后端运行时：工具、RAG、持久化运行**

以单个可执行二进制分发的 AI agent 后端：提供模型路由、加密的 provider 密钥管理、HTTP 与内部工具执行、基于文档上传（PDF/DOCX/TXT/MD/CSV/JSON/HTML）自动分块嵌入的 RAG 知识库、事件时间线的持久化运行记录、监控与认证。无需 Node 运行时、外部数据库或多服务编排，下载二进制后一条命令启动，内置 Web 控制台，并提供流式与管理两套 API 端点，面向构建 AI 应用的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单二进制提供完整 agent 平台，无外部数据库依赖
- 内置 Web 控制台管理 agents、模型、工具与密钥
- 知识集合上传文档后自动分块与嵌入实现 RAG
- 事件时间线的持久化运行与流式 chat/run API

## 适用场景

- 为 AI 应用客户端（如 @ai-sdk/react）提供一个自托管后端
- 本地或服务器上一键部署带工具与 RAG 的 agent 服务
- 通过 Web 控制台与 API 管理 agent、密钥与运行记录

## 场景标签

`Agent 框架` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L3: The complete agent runtime in a single executable.
> L5: PocketAgents gives you a full AI backend you can run anywhere with one file: model routing, encrypted provider keys,
> L7: No Node runtime setup, no external database, no multi-service orchestration. Download one binary and run.

## 星数曲线

```mermaid
xychart-beta
    title "treyorr/pocket-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `935772fbf04a` · [字段定义](../../DATASET.md)*
