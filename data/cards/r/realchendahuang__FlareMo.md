# realchendahuang/FlareMo

⭐ 340 · TypeScript · AGPL-3.0 · 推送 2026-11-01 · [GitHub](https://github.com/realchendahuang/FlareMo) · [官网](https://flaremo.app) · 个人维护 · 中文 README

**部署在 Cloudflare 边缘的笔记/任务/知识库应用，兼作 AI Agent 长期记忆**

运行于 Cloudflare Workers 的自托管第二大脑：D1 与 R2 存储笔记、任务、文章与附件，含 SQLite FTS5 全文搜索、Workers AI 向量检索、待办/看板、团队空间与三级可见性、PWA 离线同步、插件系统。AI 部分：提供 flaremo CLI 与 flaremo-memory 技能，让 Claude、Cursor、Codex、ChatGPT 等通过 MCP 或 REST 读写跨会话长期记忆，人工可在 /memory 页面审核。提供一键部署、GitHub Action、Agent 部署与手动 wrangler 四种部署方式；数据一键导出导入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 笔记/待办/文章沉淀为可搜索、互链的知识库
- Agent Memory CLI + 跨 Agent 技能，通过 MCP/REST 读写长期记忆，人工可审核
- FTS5 全文搜索与向量语义检索（可回退）
- PWA 离线同步、一键部署到 Cloudflare 免费额度

## 适用场景

- 零服务器自托管个人笔记与任务管理
- 让 Claude/Cursor/Codex 等 Agent 保存和复用长期记忆
- 小团队共享知识空间并按三级可见性控制权限

## 场景标签

 · 领域:知识管理/自托管应用

## 证据(README 行号)

> L37: - **AI-native, not bolted on**: Agent Memory ships a CLI and a cross-agent skill, so Claude, Cursor, Codex, ChatGPT
> L54: ### 2. AI Long-term Memory (CLI + Skills)
> L55: - **Agent Memory**: Ships `flaremo` CLI and the `flaremo-memory` skill — agents record and update cross-session lon


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-02 · 置信度 mid · 依据 README sha `9a76326a73ac` · [字段定义](../../DATASET.md)*
