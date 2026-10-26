# lopadova/claude-mem-sync

⭐ 27 · TypeScript · MIT · 推送 2026-06-20 · [GitHub](https://github.com/lopadova/claude-mem-sync) · [官网](https://doc.claude-mem-sync.padosoft.com) · 个人维护

**为 claude-mem 提供团队 AI 记忆共享：经 git 同步开发者间记忆**

面向使用 claude-mem 的开发团队的 Claude Code 插件与 CLI 工具：读取本地 claude-mem SQLite 数据库中的观察记录（决策、修复、发现），按类型/关键词/标签过滤后导出到私有 git 共享仓库，经 CI 合并机器人去重、按评分淘汰（上限 500 条观察），再导入各成员本地库。提供 PostToolUse 访问追踪 hook、PR 人工审查模式、9 页签 Web 仪表盘、开发者知识画像与 LLM 驱动的知识蒸馏（GitHub Copilot 或 Anthropic API）。支持 GitHub/GitLab/Bitbucket（含自托管），安装依赖 Node.js ≥ 18、git，运行时需 Bun 或 Node。

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

- 过滤导出 + 复合键去重 + 评分淘汰的团队记忆共享，以 git 为传输层
- PostToolUse hook 追踪 Claude 实际使用的记忆，纳入淘汰评分
- CI 合并机器人模板（GitHub Actions/GitLab CI/Bitbucket Pipelines）
- LLM 知识蒸馏：从团队观察提取 CLAUDE.md 规则与知识文档

## 适用场景

- 让团队成员共享各自 Claude 会话中积累的决策与修复记录
- 避免同一 bug 被重复发现、同一决策被反复讨论
- 通过 PR 审查模式在记忆入库前做人工把关
- 分析团队知识覆盖、知识缺口与 bus factor 风险

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: > Team memory sharing for claude-mem — sync AI memories across developers via git.
> L109: This single step installs both the **plugin** (PostToolUse hook for access tracking) and the **CLI tool** (`mem-sy

## 星数曲线

```mermaid
xychart-beta
    title "lopadova/claude-mem-sync 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6376bcae505a` · [字段定义](../../DATASET.md)*
