# hotalexnet/agent-checkpoint

⭐ 14 · Python · MIT · 推送 2026-09-21 · [GitHub](https://github.com/hotalexnet/agent-checkpoint) · 个人维护 · 中文 README

**给编程 agent 用的仓库级会话检查点与交接工具**

提供两个自包含技能 repo-checkpoint 与 repo-resume：会话结束时在 .agents/checkpoints/ 下生成 Markdown 交接文档（目标、决策、当前状态、验证、下一步），下次会话读取该文档、Git 状态与分支并恢复工作线。格式与工具无关，Codex、Claude Code、opencode 等可读写 Markdown 的 agent 均可跨会话、跨机器、跨模型交接。内置 30 天过期、活跃通道原子更新、常见凭据脱敏、结构校验（可拒绝未填 TODO）。要求 Python 3、Git 与 Bash，限制：脚手架不自动总结对话，交接质量取决于填写内容。

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

- 生成 Markdown 交接文档，跨 agent、跨会话、跨机器、跨模型恢复
- 活跃通道 --current 原子更新，恢复时优先读取
- 常见密码/令牌/API key/私钥等凭据脱敏
- validate/--strict 校验 frontmatter、过期与未填 TODO，prune 清理快照

## 适用场景

- 中断的编程会话下次继续同一工作线
- 换模型或换 agent 工具后恢复上下文
- 多机器间通过 Git 提交交接文档续做任务
- 团队共享或通过 .gitignore 私有化交接文档

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: Repo-local continuity skills for coding agents. Save the goal, decisions, files,
> L13: The checkpoint format is shared across Codex/OpenAI CLI, Claude Code, opencode,

## 星数曲线

```mermaid
xychart-beta
    title "hotalexnet/agent-checkpoint 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3b206e55839e` · [字段定义](../../DATASET.md)*
