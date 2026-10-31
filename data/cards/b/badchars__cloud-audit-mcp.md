# badchars/cloud-audit-mcp

⭐ 24 · TypeScript · MIT · 推送 2026-03-14 · [GitHub](https://github.com/badchars/cloud-audit-mcp) · [官网](https://github.com/badchars/cloud-audit-mcp) · 个人维护

**供 AI agent 调用的多云安全审计 MCP 服务器（AWS/Azure/GCP）**

面向 AI agent 的云安全审计 MCP 服务器：把 AWS、Azure、GCP 的 API 封装为 38 个工具与 60+ 项检查，agent 可按上下文选择检查、串联发现（如公开 S3 + Lambda 角色构成数据外泄路径）、生成修复命令并复核，覆盖公开存储、IAM 提权路径、密钥暴露等。通过 Claude Code、Claude Desktop、Cursor 等 MCP 客户端接入，复用本地云凭证，无需额外 API key。以 git clone + Bun 从源码运行，无安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 38 个工具覆盖 AWS(13)/Azure(13)/GCP(8)/元工具(4)
- 60+ 检查项并映射 CIS/OWASP/MITRE 等标准
- 复用已有云凭证，无需额外 API key
- 元工具支持汇总发现并生成 markdown/JSON 报告

## 适用场景

- 让 AI agent 实时检查多云账号的关键配置错误
- 渗透测试前的云环境侦察（IMDS、提权路径、攻击链）
- 审计 S3/GCS/Azure Storage 的公开访问与敏感文件暴露

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L6:  This gives your AI agent direct access to cloud APIs — it reads, correlates, and fixes.
> L45: Every existing tool is designed for **humans to read reports**. cloud-audit-mcp is designed for **AI agents to take
> L52:  MCP → AI agent calls tools in real-time


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a174758e6e6e` · [字段定义](../../DATASET.md)*
