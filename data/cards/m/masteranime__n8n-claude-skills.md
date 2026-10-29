# masteranime/n8n-claude-skills

⭐ 34 · Shell · MIT · 推送 2026-04-26 · [GitHub](https://github.com/masteranime/n8n-claude-skills) · 个人维护

**面向 Claude Code 的 n8n 工作流开发技能包（5 个 SKILL）**

由 n8n Verified Creator 从 100+ 生产工作流中提炼的 Claude Skills 集合，含 5 个技能：workflow-architect 按需求设计 n8n 工作流、chain-llm-pattern 多步 LLM 推理链、enrichment-waterfall 多供应商数据富集瀑布、mysql-checkpointing 批处理与幂等管道、debug-workflow 系统化调试。技能以 SKILL.md 自包含文件夹形式提供，兼容 Claude Code、Cursor、Codex、Gemini CLI 等遵循 Agent Skills 规范的 agent，通过 npx 命令或 git clone 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个自包含技能（SKILL.md + 参考文件），覆盖工作流设计、LLM 链、数据富集、MySQL 管道、调试
- 宣称源自 100+ 生产工作流的真实客户项目模式
- 兼容任何遵循 Agent Skills 规范的 agent（Claude Code/Cursor/Codex/Gemini CLI/Opencode）
- 提供 npx 一条命令安装与 install.sh 脚本两种安装方式

## 适用场景

- 让 Claude Code 按需求直接生成可导入 n8n 的工作流 JSON
- 排查 n8n 表达式语法、执行日志等调试问题
- 构建含检查点、幂等与重试逻辑的生产级自动化管道

## 场景标签

`工作流自动化` `代码生成` · 领域:效率与自动化

## 证据(README 行号)

> L20: |Skill|What it does|When it fires|
> L59: Copy any folder inside `skills/` into your agent's skills directory. Each folder is a self-contained skill with a `

## 星数曲线

```mermaid
xychart-beta
    title "masteranime/n8n-claude-skills 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28", "2026-10-29"]
    y-axis "stars" 31 --> 35
    line [32, 33, 34, 34]
```

2026-10-18 32 → 2026-10-29 34（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7e8f22332ee2` · [字段定义](../../DATASET.md)*
