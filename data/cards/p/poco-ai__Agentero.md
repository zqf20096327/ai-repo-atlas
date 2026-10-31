# poco-ai/Agentero

⭐ 1,065 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/poco-ai/Agentero) · [官网](https://agentero.app) · 组织维护 · 中文 README

**人与 Agent 协作的一站式科研文献工作台（桌面应用）**

桌面端科研工作台，面向科研人员：保留 PDF 阅读批注体验，同时把论文解析为结构化 Markdown/LaTeX 供模型消费；文献、笔记与交互记录以标准文件形式存储于本地。Agent 部分基于 ACP 协议连接本地运行的 Agent（如 Claude Code、OpenCode、Codex），并可作 MCP Server 让 ChatGPT Web、Claude Desktop 等客户端检索本地文献库；另提供 CLI 批量自动化。支持 Zotero 一键迁移、S3 同步、arXiv 推荐与 RSS 订阅。Linux 需 Ubuntu 22.04+ 且依赖 webkit2gtk 4.1。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 论文公式/表格自动解析为结构化 Markdown 与 LaTeX 上下文
- ACP 协议连接本地 Agent，内置 MCP Server 供外部客户端调用本地文献库
- Zotero 数据库一键迁移，兼容浏览器扩展与 BibTeX 导出
- 本地透明存储（PDF/Markdown 标准文件）+ S3 同步 + CLI 自动化

## 适用场景

- 文献阅读时让本地 Agent 基于论文原文答疑与推导
- 把本地文献库接入 ChatGPT/Claude 等外部 AI 客户端作上下文
- 从 Zotero 迁移并继续管理已有文献与笔记
- 通过脚本批量导入文献、抓取元数据与写笔记

## 场景标签

`科研工具` `文档问答` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L30: **Agentero 并非旨在替代 Zotero，而是探索一种人与 Agent 协同处理科研上下文的新方式**：
> L51: * **基于 ACP 协议连接本地 Agent**：底层遵循 Agent Client Protocol，支持连接各类本地运行的 Agent（如 Claude Code、OpenCode、Codex 或本地模型），不绑定特定厂商，
> L52: * **内置 MCP (Model Context Protocol)**：可作为 MCP Server 运行，允许 ChatGPT Web、Claude Desktop 等外部客户端直接检索并调用本地文献库作为上下文。


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c19b8f560e13` · [字段定义](../../DATASET.md)*
