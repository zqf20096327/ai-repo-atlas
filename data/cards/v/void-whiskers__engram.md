# void-whiskers/engram

⭐ 3 · Markdown · MIT · 推送 2026-11-26 · [GitHub](https://github.com/void-whiskers/engram) · 个人维护

**给个人与其 AI agent 共用的 git 版控第二大脑知识库模板**

一个纯 Markdown + Git 的结构化知识库模板，组织为 standards、experiments、goals、knowledge、tools、projects、investigations、personas 八类内容，配合 B-Tree 式 INDEX.md 导航（任意文档距根 ≤3 跳），供人与编码 agent 读写共享上下文。接入方式是向 Cline/Claude Code/Cursor 等助手的规则文件注入一段固定指令，使 agent 按导航协议取用记忆。依赖 git 与私有仓库克隆，无向量库或云服务。附带 .agents/skills/ 内置技能用于增改条目与校验链接；token 节省数据来自单代码库小样本试点，作者自述为方向性结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- B-Tree 索引导航：每个目录有 INDEX.md，文档距 AGENTS.md ≤3 跳
- 零重依赖：纯 Markdown + Git，无向量库/嵌入/云订阅
- 通过向 Cline、Claude Code、Cursor、Windsurf、Codex 等注入统一规则接入
- 内置 validate-memory、sync-memory 等 agent 技能维护记忆库

## 适用场景

- 让编码 agent 跨项目复用我的编码标准与项目约束
- 把实验记录和调查结论沉淀成 agent 可导航的知识库
- 控制 agent 上下文读取的 token 成本

## 场景标签

`Agent 记忆` `知识库管理` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: A shared second brain for you and all agents working with you — a living, navigable knowledge base that grows across
> L13: This repository is a structured knowledge base organized for **efficient agent navigation**. Agents and humans alik


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `3b68164e8348` · [字段定义](../../DATASET.md)*
