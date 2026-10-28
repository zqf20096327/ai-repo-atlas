# Jordan-Jarvis/jenkins-mcp-enterprise

⭐ 30 · Python · GPL-3.0 · 推送 2026-09-21 · [GitHub](https://github.com/Jordan-Jarvis/jenkins-mcp-enterprise) · 个人维护

**面向 Jenkins 的 MCP 服务器：构建管理、日志诊断与多实例路由**

一个 Model Context Protocol 服务器，向 AI 客户端暴露 Jenkins 操作工具：同步/异步触发构建、按 jenkins_url 路由到对应 Jenkins 实例、日志检索（ripgrep 正则/错误过滤/分段导航）、AI 辅助的构建失败诊断（可配置推荐参数），以及可选的基于 Qdrant 的日志向量语义检索与服务端任务定义编辑上传。面向管理 CI/CD 流水线的开发/运维人员，维护的安装路径为源码安装与 Docker/Compose，需 Python 3.10+、Jenkins API token；双层配置（主配置+诊断配置覆盖），诊断不提供覆盖时使用内置默认。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 jenkins_url 将每次工具调用路由到正确的 Jenkins 实例
- AI 辅助构建失败诊断，诊断参数可配置覆盖
- 可选 Qdrant 向量检索对日志块做语义搜索
- 日志工具链：ripgrep 正则搜索、错误过滤、分段导航

## 适用场景

- 让 Claude Desktop 等 MCP 客户端直接触发和检查 Jenkins 构建
- 通过对话分析失败构建并在嵌套流水线中定位根因
- 多 Jenkins 实例环境下的统一接入与路由

## 场景标签

 · 领域:DevOps/CI-CD 集成

## 证据(README 行号)

> L1: # Jenkins MCP Server Enterprise
> L3: > Jenkins MCP server for multi-instance routing, build diagnostics, and optional vector search.
> L5: A Model Context Protocol (MCP) server for Jenkins that provides build management, log inspection, failure diagnostic

## 星数曲线

```mermaid
xychart-beta
    title "Jordan-Jarvis/jenkins-mcp-enterprise 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `50e7579b49ce` · [字段定义](../../DATASET.md)*
