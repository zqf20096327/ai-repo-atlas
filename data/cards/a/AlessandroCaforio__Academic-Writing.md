# AlessandroCaforio/Academic-Writing

⭐ 23 · Jupyter Notebook · MIT · 推送 2026-03-31 · [GitHub](https://github.com/AlessandroCaforio/Academic-Writing) · 个人维护

**用 Claude Code 多智能体流程写实证经济学硕士论文的完整实践记录**

作者记录其在 Bocconi 大学撰写实证经济学硕士论文（自动化任务替代对美国政治意识形态的影响）时搭建的 Claude Code 工作流：CLAUDE.md 持久项目记忆、8 条常驻规则、11 个斜杠命令技能、17 个专用子代理，覆盖文献 RAG 核验（105 篇论文 ChromaDB 语料）、计量方法审查（Opus 模型的因果推断代理）、LaTeX 编译（tectonic）与校对。README 明确声明这不是可安装模板，而是供参考改编的真实项目示例；运行需 Claude Code CLI，RAG 部分需 Python 3.10+、ChromaDB 与 sentence-transformers。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 17 个专用子代理 + 8 条常驻规则 + 11 个斜杠命令技能的三层结构
- /verify-claims 连接 105 篇论文（10,217 chunks）的 ChromaDB RAG 语料
- CLAUDE.md 约 600 行持久项目记忆，跨会话保留数据管道与决策上下文
- 因果推断代理运行在 Opus 模型，其余代理用默认模型控制成本

## 适用场景

- 参考如何为长周期学术写作项目配置 Claude Code 多代理环境
- 改编为其他大型研究或写作项目的 Claude Code 配置
- 了解 CLAUDE.md / rules / skills / agents 的组织方式与经验教训

## 场景标签

`多智能体` `RAG` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L7: **This is not a template you install** — it's a real-world example of how to configure Claude Code for a complex, mu
> L175: 1. **Fork this repo** and strip out the thesis-specific content

## 星数曲线

```mermaid
xychart-beta
    title "AlessandroCaforio/Academic-Writing 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5dec5a2d9d0c` · [字段定义](../../DATASET.md)*
