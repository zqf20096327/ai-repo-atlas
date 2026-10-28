# smixs/mentor

⭐ 85 · Python · MIT · 推送 2026-08-08 · [GitHub](https://github.com/smixs/mentor) · 个人维护

**分析 Claude Code 与 Codex 会话历史并生成 HTML 工作洞察报告的 agent 技能**

一个可安装到 Claude Code、OpenAI Codex 等 skills 兼容 agent 的技能：本地读取 ~/.claude 转录与 ~/.codex rollouts 会话历史（不上传数据），由 collect.py 统计消息数、工具调用、编辑量、语言分布等指标，agent 读取统计摘要撰写八个章节的分析（含摩擦点与修复建议、CLAUDE.md 建议行），render_report.py 合并为单文件 report.html。默认分析近 30 天，可跨两个 agent 汇总。主题与满意度等判断由模型推断并被标注为假设。捆绑脚本依赖 uv。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地读取 Claude Code 与 Codex 会话历史，数据不上传
- 统计为实际计数而非模型猜测
- 生成含八个章节、内联 SVG 图表的单文件 report.html
- 每个摩擦点附带可执行的修复：CLAUDE.md 行、hook 或习惯

## 适用场景

- 每周复盘我与编码 agent 的协作模式与时间损耗
- 跨 Claude Code 与 Codex 发现两个工具中反复出现的习惯问题
- 从会话数据中获得可复制粘贴的 CLAUDE.md 配置建议

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L4: ## a skill that reads your local session history and writes report on how you actually work.
> L12: - **Reads your local session history.** Claude Code transcripts under `~/.claude` and Codex rollouts under `~/.code
> L54: For Codex, clone the skill into `~/.codex/skills/mentor` instead. The bundled scripts need `uv`; the skill itself i

## 星数曲线

```mermaid
xychart-beta
    title "smixs/mentor 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 83 --> 86
    line [84, 85, 85]
```

2026-10-18 84 → 2026-10-28 85（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6ee0c637f323` · [字段定义](../../DATASET.md)*
