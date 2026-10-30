# eddmann/obsidian-mcp

⭐ 15 · TypeScript · MIT · 推送 2025-12-03 · [GitHub](https://github.com/eddmann/obsidian-mcp) · 个人维护

**面向 git 同步 Obsidian 库的 MCP 服务器，供 LLM 读写笔记**

基于 Model Context Protocol 的服务器，让 Claude、ChatGPT 等 LLM 访问和管理 git 仓库形式的 Obsidian 笔记库。提供 18 个工具（文件读写/移动/补丁、目录操作、模糊搜索、标签管理、日志记录）和 1 个资源。工作流程：服务端从 git 克隆/拉取笔记库，LLM 通过 MCP 工具修改内容，服务端自动提交并推送。支持 stdio 本地运行、带 OAuth 的 HTTP 模式及 AWS Lambda 无服务器部署。要求笔记库为 git 仓库并推送至远端。

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

- 18 个工具：文件/目录操作、模糊搜索、标签管理、日志记录
- git 仓库克隆-修改-自动提交推送的同步机制
- 支持 stdio 本地、HTTP+OAuth 远程、AWS Lambda（DynamoDB 会话）三种部署模式

## 适用场景

- 通过 Claude Desktop 等客户端用自然语言读写我的 Obsidian 笔记
- 让 ChatGPT 等远程 LLM 经 OAuth 接入笔记库
- 自动整理笔记标签、检索内容并记录日志

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L5: A Model Context Protocol (MCP) server for git-backed Obsidian vaults. Access and manage your notes through Claude, C
> L11: This MCP server provides **18 tools** and **1 resource** to interact with your Obsidian vault through LLMs:
> L102: 1. Server clones/pulls your vault from git

## 星数曲线

```mermaid
xychart-beta
    title "eddmann/obsidian-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9e3d5c4e4f51` · [字段定义](../../DATASET.md)*
