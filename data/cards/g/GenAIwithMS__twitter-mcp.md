# GenAIwithMS/twitter-mcp

⭐ 26 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/GenAIwithMS/twitter-mcp) · 个人维护

**让 AI 助手通过 MCP 操作 X(Twitter)的服务器**

基于 TypeScript 的 Model Context Protocol (MCP) 服务器，使 Claude Desktop、Cursor IDE 等 MCP 客户端能以自然语言操作 Twitter/X：发推与带图发推（JPG/PNG/GIF/WEBP）、搜索、回复、引用、点赞转推收藏、获取用户资料与会话线程、监控提及、自动拆分长文发布推文串。认证用 Twitter OAuth 1.0a，内置速率限制；可选接入 Xquik/Hermes Tweet 与 GetXAPI 只读搜索后端。通过 npx 交互式安装器或 Docker/Podman 镜像部署，凭据以环境变量注入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖发推/带图/搜索/回复/引用/点赞转推/线程管理等 Twitter API 操作
- npx 交互式安装器自动写入 Claude Desktop、Cursor IDE 等客户端的 MCP 配置
- 官方 Docker/Podman 镜像，stdio 传输，容器以非 root 用户运行
- 可选 Xquik/Hermes Tweet 与 GetXAPI 只读搜索后端

## 适用场景

- 在 Claude Desktop 对话中直接发推、搜推和管理 Twitter 互动
- 社媒运营者让 AI 助手批量监控提及与关键词
- 把长内容自动拆分为推文串发布

## 场景标签

 · 领域:AI 助手工具接入/社交媒体自动化

## 证据(README 行号)

> L29: A Model Context Protocol (MCP) server that enables seamless interaction with Twitter/X through AI assistants such a
> L162: The first prompt asks which AI assistant environment you want to integrate with. Available options are:
> L164: - Claude Desktop App

## 星数曲线

```mermaid
xychart-beta
    title "GenAIwithMS/twitter-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-29 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1445ac9d0cd1` · [字段定义](../../DATASET.md)*
