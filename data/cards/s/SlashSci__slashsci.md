# SlashSci/slashsci

⭐ 4 · 推送 2026-11-27 · [GitHub](https://github.com/SlashSci/slashsci) · [官网](https://slashsci.com/) · 组织维护 · 中文 README

**面向科研人员的本地优先文献管理与沉浸式译读工具**

SlashSci Library 是一款处于内测阶段的桌面文献管理应用，覆盖 macOS（Apple 芯片）与 Windows。功能包括块级全文解析（公式 KaTeX 渲染、引文就地展开）、逐句译读（原文/译文/对照三视图）、页边锚定批注（四色分类、双向溯源）、语料与术语库，以及本地文献库：支持 DOI/arXiv/PMCID 导入、期刊指标展示、AI 学科分类与全文检索。全库以 JSON/Markdown/XML 开放格式存于本机，不上传服务器；翻译与 AI 密钥由用户自管，接 Ollama 可完全离线。内置 MCP 服务，Claude Code 等 Agent 可直接检索本地库。安装包经内测社区发放，未签名需绕过系统拦截。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 块级全文解析与沉浸式逐句译读，三视图即时切换
- 页边锚定批注，四色分类，点击即定位原文
- 本地优先：开放格式存储，一键导出迁移
- 内置 MCP 服务，Claude Code 等 Agent 可直接检索

## 适用场景

- 科研人员精读英文论文并沉淀批注与术语
- 在本地建立可迁移的个人文献知识库
- 让 Claude Code 等 Agent 检索自己的文献库

## 场景标签

`科研工具` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L10:  为 AI 时代重构的文献管理
> L60:  本地优先，为 Agent 而生 ：全库以开放格式存于本机，一键导出迁移；内置 MCP 服务，Claude Code 等 Agent 可直接检索
> L74: - **本机存储**：文献以 JSON、Markdown 和 XML 等开放格式保存在本机文件夹，不上传服务器，也不被任何平台锁定。SQLite 只做可重建的索引。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `cbbcc0cf9fc8` · [字段定义](../../DATASET.md)*
