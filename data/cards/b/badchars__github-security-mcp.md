# badchars/github-security-mcp

⭐ 16 · TypeScript · MIT · 推送 2026-03-14 · [GitHub](https://github.com/badchars/github-security-mcp) · 个人维护

**给 AI agent 用的 GitHub 安全态势审计 MCP 服务器（39 工具/45 检查）**

基于 Model Context Protocol 的 MCP 服务器，向 AI agent 暴露 39 个工具，对 GitHub 组织、仓库、Actions 工作流、密钥、供应链与访问控制执行 45 项安全检查，覆盖分支保护、secret scanning、CodeQL、Dependabot、OIDC 等配置项。使用 Bun 运行，通过 Classic/Fine-grained PAT 或 GitHub App 认证，企业专属功能优雅降级为 NOT_APPLICABLE，发现仅存于会话内存，无持久化。适用于 Claude Code、Claude Desktop、Cursor 等 MCP 客户端，用公共 API 替代付费的企业安全功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 39 个 MCP 工具覆盖 6 大 GitHub 安全领域
- 45 项带严重度分级的检查（CRITICAL 至 INFO）
- Actions 工作流静态分析（脚本注入、pull_request_target、未固定 action 等 8 项）
- 仅 4 个依赖，token 经 GITHUB_TOKEN 环境变量读取

## 适用场景

- 让 AI agent 对 GitHub 组织做全面安全审计并汇总报告
- 检查 CI/CD 工作流的供应链与注入风险
- 审查团队权限、外部协作者与 PAT 使用情况

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3:  GitHub security posture analysis for AI agents.
> L34: **github-security-mcp** gives your AI agent 39 tools and 45 security checks via the Model Context Protocol. The age


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c07f359b4497` · [字段定义](../../DATASET.md)*
