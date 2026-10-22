# MCP-Manager/MCP-Security-Checklists

⭐ 199 · JavaScript · AGPL-3.0 · 推送 2026-10-20 · [GitHub](https://github.com/MCP-Manager/MCP-Security-Checklists) · [官网](https://mcpmanager.ai) · 组织维护

**MCP 服务器与 AI agent 安全采用的检查清单与指南仓库**

由构建 MCP Manager 的安全团队维护的知识型仓库，发布一系列围绕 MCP（Model Context Protocol）安全采用的检查清单、索引与经验文档，覆盖部署基础设施（Docker 容器化本地 MCP、暴露 localhost、远程运行 STDIO MCP）、OAuth 排查与身份管理、日志审计可观测性、威胁与漏洞索引、AI agent 构建与工具选择安全。提供示例 Dockerfile 与脚本帮助用户在沙箱中运行本地 MCP 服务器，面向采用 AI agent 与 MCP 的企业及开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖部署、认证、审计、威胁、agent 构建五大类的检查清单体系
- 提供在 Docker 沙箱中安全运行本地 MCP 服务器的指南、Dockerfile 与脚本
- 维护 MCP 服务器网络安全威胁清单与已报告漏洞索引

## 适用场景

- 为本地或远程 MCP 服务器部署建立安全基线
- 排查 MCP OAuth 与身份管理问题
- 评估与审计现有 MCP 服务器的威胁和风险
- 构建 AI agent 时参考工具选择与安全清单

## 场景标签

`网络安全` `精选清单` · 领域:学习与行业

## 证据(README 行号)

> L3: We're a team of security and AI enthusiasts building MCP Manager, a comprehensive MCP security solution for business
> L5: In this repository we will publish a range of checklists, indexes, lessons learned and helpful utilities to help you


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `f4fbd6637769` · [字段定义](../../DATASET.md)*
