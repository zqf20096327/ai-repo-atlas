# zvec-ai/zvec-agent-skills

⭐ 21 · TypeScript · Apache-2.0 · 推送 2026-04-09 · [GitHub](https://github.com/zvec-ai/zvec-agent-skills) · [官网](https://zvec.org/en/) · 组织维护 · 中文 README

**给 AI Agent 用的 Zvec 向量数据库官方技能包**

由 zvec-ai 维护的官方 Agent Skill 集合：将 Zvec 向量数据库（基于阿里巴巴 Proxima 引擎的进程内向量库）的技术文档整理为可被 AI Agent 加载的技能，覆盖 Python 与 Node.js 两种开发环境的快速入门、Collection 管理、数据操作、向量/混合/多模态搜索、RAG 构建与排错等主题。通过 npx skills add 安装技能，用 bun 构建生成分发产物；技能面向 Claude Code 与 Claude Desktop 场景使用。内容为文档知识，不直接运行模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 Python 与 Node.js 两大主题集的 Zvec 使用文档技能
- 通过 npx skills add 一行命令安装为 Agent 技能
- 构建系统将源码转换为可分发技能（bun run build）
- 提供 RAG、电商搜索、日志排障等使用场景示例

## 适用场景

- 让 Claude 类 Agent 在编码时获取 Zvec 数据库的正确用法指导
- 构建 RAG 检索或电商语义搜索时由 Agent 生成 Zvec 代码
- 为 Agent 补充向量数据库 schema 设计与索引策略知识

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L8: Official AI Agent skills for building with Zvec vector database.
> L10: Zvec Assistant is an AI Agent Skill that provides developers with complete technical guidance for the Zvec vector d

## 星数曲线

```mermaid
xychart-beta
    title "zvec-ai/zvec-agent-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `5a06c43950c6` · [字段定义](../../DATASET.md)*
