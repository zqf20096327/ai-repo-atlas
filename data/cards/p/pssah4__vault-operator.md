# pssah4/vault-operator

⭐ 262 · TypeScript · Apache-2.0 · 推送 2026-09-15 · [GitHub](https://github.com/pssah4/vault-operator) · [官网](https://pssah4.github.io/vault-operator/) · 个人维护 · 中文 README

**Obsidian 知识库的智能体 AI 操作层插件**

运行在 Obsidian 内的 agentic 插件：用户描述任务后，智能体循环执行规划、搜索（本地向量索引+全文+图扩展+重排序）、读写笔记并汇报。功能覆盖带段落级溯源的 PDF 摄取、网页剪藏、三层记忆、DOCX/XLSX 生成（PPTX beta）、知识库健康检查，并可作 MCP server 供 ChatGPT/Claude Desktop 读取。安全上 fail-closed，写操作默认需批准，shadow git 检查点可一键撤销。支持 BYOK 多提供商（含 Ollama/LM Studio 离线），通过 Obsidian 社区插件市场安装，需 Obsidian 1.8.7+ 桌面版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 智能体循环：选动作→对 vault 执行→结果回喂模型直至任务完成
- 带 block 级溯源的 PDF 深度摄取与三层跨会话记忆
- 本地向量索引+全文+wikilink 图扩展+cross-encoder 重排序的语义搜索
- fail-closed 权限模型与 shadow git 一键撤销检查点
- 可作为 MCP server 让 ChatGPT/Claude Desktop 等读取同一知识库

## 适用场景

- 让 AI 智能体整理、改写和扩充我的 Obsidian 笔记
- 把 PDF 论文摄取成带段落溯源的源笔记并生成关联笔记
- 对知识库做健康检查并自动修复孤儿笔记、断链等问题
- 通过 ChatGPT 或 Claude Desktop 以 MCP 方式访问我的 vault

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L47: A chatbot reads your prompt and answers. Vault Operator runs a loop: it picks an action, executes it against your v
> L5: **Agentic AI operating layer for your vault.**

## 星数曲线

```mermaid
xychart-beta
    title "pssah4/vault-operator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 261 --> 263
    line [262, 262]
```

2026-10-18 262 → 2026-10-26 262（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `f2d9844cd494` · [字段定义](../../DATASET.md)*
