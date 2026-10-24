# SonarSource/sonarqube-mcp-server

⭐ 670 · Java · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/SonarSource/sonarqube-mcp-server) · [官网](https://www.sonarsource.com/products/sonarqube/mcp-server/) · 组织维护

**官方 SonarQube MCP 服务器：让 AI agent 接入代码质量与安全分析**

SonarSource 官方维护的 Model Context Protocol 服务器，使 Claude Code、Codex CLI、Cursor、Gemini CLI、GitHub Copilot、Windsurf、Zed、VS Code 等 AI agent 客户端连接 SonarQube Server 或 SonarQube Cloud，读取代码质量与安全分析结果，并支持在 agent 上下文中直接分析代码片段。主要以容器镜像 sonarsource/sonarqube-mcp 分发，通过环境变量提供 token/org/URL 认证，需设置 STORAGE_PATH 指定可写存储目录；另提供交互式配置生成器与各客户端的一键安装入口。限制：容器内访问 SonarQube for IDE 需额外网络配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以容器镜像分发，支持版本标签固定与 OCI 兼容运行时（Podman/nerdctl）
- 覆盖十余种 AI agent 客户端的安装配置说明
- 支持在 agent 上下文中直接分析代码片段
- 提供交互式配置生成器生成客户端配置

## 适用场景

- 在 Claude Code/Cursor 等 agent 中查询 SonarQube 代码质量与安全问题
- 让 agent 在编码过程中直接分析代码片段
- 在 CI/CD 的 GitHub Copilot coding agent 中使用 SonarQube 检查

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L8: The SonarQube MCP Server is a Model Context Protocol (MCP) server that enables seamless integration with SonarQube S
> L9: It also supports the analysis of code snippet directly within the agent context.

## 星数曲线

```mermaid
xychart-beta
    title "SonarSource/sonarqube-mcp-server 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23", "2026-10-24"]
    y-axis "stars" 664 --> 671
    line [665, 667, 669, 670]
```

2026-10-18 665 → 2026-10-24 670（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `256ef90b2e27` · [字段定义](../../DATASET.md)*
