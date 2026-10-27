# modelscope/modelscope-mcp-server

⭐ 26 · Python · Apache-2.0 · 推送 2025-12-15 · [GitHub](https://github.com/modelscope/modelscope-mcp-server) · [官网](https://modelscope.cn/mcp/servers/@modelscope/modelscope-mcp-server) · 组织维护 · 中文 README

**ModelScope 官方 MCP Server：让 Agent 访问其模型与数据集生态**

ModelScope 官方维护的 MCP 服务器，基于 FastMCP v2 构建，向 AI agent 与聊天机器人暴露 ModelScope 生态资源：通过对话调用文生图/图生图的 AIGC 模型，检索与查看模型、数据集、Studio 应用、论文及 MCP 服务器等资源的详情，并读取认证用户与环境上下文。使用需申请 ModelScope API Token，通过 JSON 配置接入 Claude Desktop、Cursor、VS Code、Cherry Studio 等 MCP 客户端，也可使用预构建 Docker 镜像或 uv 本地运行（stdio/HTTP/SSE 传输）。文档语义搜索与 Gradio API 调用标注为 Coming Soon。仓库描述标注 Deprecated。

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

- 文生图/图生图的 AIGC 模型调用
- 检索模型、数据集、Studio、论文、MCP 服务器等 ModelScope 资源
- stdio 与 HTTP/SSE 双传输模式，支持 MCP Inspector 调试
- 提供预构建 Docker 镜像与 PyPI 包

## 适用场景

- 在 Claude Desktop/Cursor 等 MCP 客户端中直接生成图片
- 让 AI agent 按条件检索 ModelScope 的模型与数据集
- 通过对话查询 ModelScope 资源详情与当前认证上下文

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L11: Empowers AI agents and chatbots with direct access to ModelScope's rich ecosystem of AI resources. From generating 
> L200: - **FastMCP v2** - High-performance MCP framework

## 星数曲线

```mermaid
xychart-beta
    title "modelscope/modelscope-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `1d22b6f01cca` · [字段定义](../../DATASET.md)*
