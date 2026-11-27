# SonarSource/sonarqube-cli

⭐ 306 · TypeScript · LGPL-3.0 · 推送 2026-11-26 · [GitHub](https://github.com/SonarSource/sonarqube-cli) · [官网](https://cli.sonarqube.com/) · 组织维护

**将 SonarQube 静态分析接入终端与 AI coding agent 的 CLI**

把 SonarQube Server/Cloud 接入终端的命令行工具，三种用法：为 Claude Code、Copilot CLI、Codex 等安装 pre-tool-use 钩子（提交代码前扫描硬编码密钥并阻止发送给 LLM 提供方）、交互式执行密钥扫描与 issue 查询、脚本化输出 JSON/toon 格式。需连接 SonarQube Cloud 或自托管 Server 并完成 token 认证；本地变更分析仅支持 SonarQube Cloud；提供 brew/mise/安装脚本三种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 为 Claude Code/Copilot CLI 等安装 pre-tool-use 密钥扫描钩子，阻止密钥发给 LLM 提供方
- 内置 MCP server，从 agent 直接访问 SonarQube 数据
- 默认输出 JSON，另有面向 LLM 的 token 高效 toon 格式
- 通过 sonar auth login 浏览器流程生成 token，支持环境变量供 CI/agent 使用

## 适用场景

- 让 AI coding agent 在处理代码前自动扫描硬编码密钥
- 本地快速查看本次改动引入的代码质量与安全问题
- 脚本化汇总多项目的 issue 严重度报告

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L8: SonarQube CLI integrates SonarQube Server and SonarQube Cloud into terminal and AI coding-agent workflows.
> L19: - **🔗 Agent Integration** — Seamless hooks for Claude Code, GitHub Copilot CLI, Codex, Cursor, Antigravity, OpenCod
> L48: 2. **🖥️ Interactive CLI** — Run commands directly in your terminal to scan code, check issues, and manage SonarQube

## 星数曲线

```mermaid
xychart-beta
    title "SonarSource/sonarqube-cli 星数(近 10 点)"
    x-axis ["2026-10-25", "2026-10-27", "2026-10-30", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-18", "2026-11-26", "2026-11-27"]
    y-axis "stars" 292 --> 307
    line [293, 294, 298, 300, 293, 302, 304, 305, 306, 306]
```

2026-10-25 293 → 2026-11-27 306（+13）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `9a3663bd5e10` · [字段定义](../../DATASET.md)*
