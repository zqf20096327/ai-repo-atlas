# guanyang/llm-wiki

⭐ 29 · Python · MIT · 推送 2026-04-19 · [GitHub](https://github.com/guanyang/llm-wiki) · 个人维护 · 中文 README

**用 Obsidian + LLM Agent 持续维护的个人知识库方案**

受 Karpathy LLM Wiki 模式启发的个人知识库工程：人工策展原始材料放入 raw/，由 LLM Agent 按 schema 文件（AGENTS.md/CLAUDE.md/GEMINI.md 分别适配 OpenAI Codex、Claude Code、Gemini CLI、Kiro）执行 Ingest、Query、Lint、Publish、Refresh 等工作流，将知识编译为结构化互链的 Markdown wiki 页。核心机制包括置信度评分、遗忘曲线衰减、active→stale→archived 状态迁移、supersession 版本链追溯与四层记忆模型；Wiki 层兼容 Obsidian，推荐用其浏览与 Graph View 查看知识结构。本体是知识库模板与 Agent 技能规范，非独立运行的软件，需用户自备 LLM Agent 工具执行操作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 为 Codex/Claude Code/Gemini CLI/Kiro 提供三份等价 schema 文件
- 知识生命周期管理：置信度评分、遗忘曲线、状态迁移、supersession 版本链
- 编译优于检索：材料一次编译为结构化 wiki 页，查询基于预编译知识
- 四层记忆模型（raw→summaries→entities/concepts→synthesis）逐层晋升

## 适用场景

- 用 LLM Agent 自动整理阅读材料并维护互链的个人知识库
- 让 AI 基于已编译知识回答问题并做矛盾检测与健康检查
- 从 wiki 知识产出博客、报告、Marp 幻灯片等交付物

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L22: ├── AGENTS.md          # Schema spec (OpenAI Codex and other general agents)
> L81: All operations are executed through the `llm-wiki` skill (see `skills/llm-wiki/SKILL.md` for details):

## 星数曲线

```mermaid
xychart-beta
    title "guanyang/llm-wiki 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `18bf1f89fc4f` · [字段定义](../../DATASET.md)*
