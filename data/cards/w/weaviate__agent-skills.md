# weaviate/agent-skills

⭐ 104 · Python · BSD-3-Clause · 推送 2026-10-20 · [GitHub](https://github.com/weaviate/agent-skills) · 组织维护

**Weaviate 官方 Agent Skills 集合：供 AI 代理操作 Weaviate 数据库**

Weaviate 维护的 Agent Skills 仓库：每个技能是包含指令、脚本与资源的文件夹，可被 Claude Code、Cursor、GitHub Copilot 等支持 Agent Skills 格式的代理自动发现，用于更准确地操作 Weaviate 数据库。提供创建/探索/查询集合、导入数据（含多向量与 PDF）等工具技能，以及 RAG、多模态 PDF 摄入、聊天机器人等 Cookbooks 蓝图。安装方式包括 npx skills、Claude Code 插件管理器与手动 clone。需配置 Weaviate Cloud 实例与环境变量，要求 Python 3.11+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供集合创建/探索/查询（关键词、向量、混合搜索）与数据导入技能
- Cookbooks 蓝图覆盖 RAG、多模态 PDF 摄入、Query Agent 聊天机器人等端到端应用
- 兼容任意支持 Agent Skills 格式的代理（Claude Code、Cursor、GitHub Copilot 等）
- 三种安装方式：npx skills / Claude Code 插件管理器 / git clone

## 适用场景

- 让 Claude Code 或 Cursor 等代理直接查询和管理我的 Weaviate 集合
- 用代理生成基于 Weaviate 的 RAG 或多模态 PDF 应用
- 通过交互式 quickstart 命令完成 Weaviate 环境初始化

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: Agent Skills to help developers build and use AI agents with Weaviate more effectively. Each skill is a folder conta
> L7: Works with any agent that supports the Agent Skills format.

## 星数曲线

```mermaid
xychart-beta
    title "weaviate/agent-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 103 --> 105
    line [104, 104]
```

2026-10-18 104 → 2026-10-24 104（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `2809bcd36bc4` · [字段定义](../../DATASET.md)*
