# agentforge-tech/AgentForge-Desktop

⭐ 3 · Java · 推送 2026-11-27 · [GitHub](https://github.com/agentforge-tech/AgentForge-Desktop) · 组织维护 · 中文 README

**本地优先的桌面 AI agent 工作台：装一个应用即可与 agent 对话**

面向 macOS 与 Windows 的本地优先 agent 工作台：Electron 壳内嵌 Spring Boot 后端与打包的 JRE 8，运行时无需安装 JDK、Maven 或数据库。提供流式对话与工具调用、任务化 SSE 断线续传、本地图片/文件/文件夹作为多模态资源、按会话绑定工作区、Skill 发现与导入、高风险 bash 命令人工审批与权限模式、模型 CRUD 与连通性/Function Call 测试、SQLite 持久化与版本化迁移，以及 macOS arm64/x64 与 Windows x64 的一键打包脚本。安装方式为源码构建（Node 22+/npm 10+/JDK 8/Maven 3.9+）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 流式推理、工具调用与可取消运行的 agent 循环，SSE 事件持久化支持断点续传
- 本地资源多模态：图片路由到视觉模型，文本文件与路径经 read_resource 工具读入上下文
- 人工介入机制：ask_user 提问、高风险命令审批、默认/完全访问两种权限模式
- SQLite 版本化迁移带 SHA-256 校验，配置热重载

## 适用场景

- 在本机一站式与配置好的 agent 对话并执行工作区任务
- 管理多个模型与 agent 配置，做连通性与 Function Call 测试
- 让 agent 读取本地项目文件夹并在其中执行工具
- 需要人工审批高风险命令的本地 agent 自动化

## 场景标签

`Agent 框架` `多模态` · 领域:Agent 开发

## 证据(README 行号)

> L5: A local-first AI agent workbench for macOS and Windows. AgentForge Desktop pairs a Vue 2 + Vite + Electron shell wit
> L17: - **Zero setup** — Electron launches the backend JAR on a free local port with a one-time token; no JDK, Maven, or 
> L19: - **Real agent loop** — streaming reasoning, tool calls, workspace-aware execution, and cancellable runs, not a cha


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `89efcf8c949e` · [字段定义](../../DATASET.md)*
