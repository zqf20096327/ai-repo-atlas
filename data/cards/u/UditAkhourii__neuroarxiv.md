# UditAkhourii/neuroarxiv

⭐ 437 · TypeScript · MIT · 推送 2026-09-17 · [GitHub](https://github.com/UditAkhourii/neuroarxiv) · [官网](https://www.divergent.sh/blog/neuroarxiv-never-build-from-scratch) · 个人维护

**Claude Code/Codex 技能：设计架构前先检索 arXiv 先行工作并收敛出单一建议**

以 agent 技能（SKILL.md）形式提供的工具：在设计新架构前通过真实 HTTP 抓取 arXiv 论文，隔离阅读避免来源互相锚定，再收敛为一条带引用的建议，含首选方案、落选原因与已知失败模式。安装方式为 npx 一行命令，可落位到 Claude Code 与 Codex CLI 的 skills 目录，也提供 git clone 本地构建路径。附有与冷启动、普通 web 搜索的三条件评测记录（EVALS.md）。

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

- 抓取真实 arXiv 元数据，声明可溯源至摘要，明确反幻觉引用
- 隔离阅读后强制收敛为单一建议并说明落选方案
- npx 一行安装，同时支持 Claude Code 与 Codex CLI
- 与冷启动/web 搜索的三条件评测有公开评分与逐题记录

## 适用场景

- 在实现非平凡算法或架构前让 agent 先核对 arXiv 先行工作
- 在 Claude Code / Codex CLI 中以技能方式触发先验检索
- 获得带引用与风险提示的单一定向技术方案

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: # NeuroArxiv — a skill to kill from-scratch coding
> L70: Works for **Claude Code and Codex CLI**. Both discover skills at

## 星数曲线

```mermaid
xychart-beta
    title "UditAkhourii/neuroarxiv 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 435 --> 438
    line [436, 437, 437]
```

2026-10-18 436 → 2026-10-25 437（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9450624e2afc` · [字段定义](../../DATASET.md)*
