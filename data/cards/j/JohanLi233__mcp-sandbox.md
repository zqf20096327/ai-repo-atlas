# JohanLi233/mcp-sandbox

⭐ 39 · Python · Apache-2.0 · 推送 2025-12-19 · [GitHub](https://github.com/JohanLi233/mcp-sandbox) · [官网](http://www.mcpsandbox.xyz/) · 个人维护 · 中文 README

**供 LLM 安全执行 Python 代码的 Docker 沙箱 MCP 服务器**

基于 MCP 协议的 Python 代码执行服务器：在隔离的 Docker 容器中为用户和 LLM 提供代码执行、包安装（支持自定义 PyPI 镜像）、终端命令、文件上传与生成文件的网络链接访问。提供 7 个工具（创建/列出沙箱、执行代码、安装包、查询安装状态、执行命令、上传文件），通过 SSE 端点与 MCP Inspector 或 Claude Desktop 等客户端集成，支持可选 API key 认证与内置 Web UI。源码方式安装运行。

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

- 在隔离 Docker 容器中执行 Python 代码与终端命令
- 沙箱内安装 Python 包并支持自定义 PyPI 镜像
- SSE 端点接入 MCP 客户端（如 Claude Desktop），可选 API key 认证
- 内置 Web UI 管理沙箱并查看执行结果

## 适用场景

- 让 Claude Desktop 等 MCP 客户端中的 LLM 安全运行 Python 代码
- 多用户环境下经 API key 认证共享代码执行沙箱
- LLM 执行代码后生成文件并通过链接获取

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L18: Python MCP Sandbox is an interactive Python code execution tool that allows users and LLMs to safely execute Python
> L41: The default SSE endpoint is http://127.0.0.1:8181/sse, and you can interact with it via the MCP Inspector through S

## 星数曲线

```mermaid
xychart-beta
    title "JohanLi233/mcp-sandbox 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 38 --> 41
    line [40, 39, 39]
```

2026-10-18 40 → 2026-10-29 39（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `dc27fb11d5d8` · [字段定义](../../DATASET.md)*
