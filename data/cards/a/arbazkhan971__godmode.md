# arbazkhan971/godmode

⭐ 27 · Shell · MIT · 推送 2026-08-28 · [GitHub](https://github.com/arbazkhan971/godmode) · 个人维护

**把 AI 编码助手变为自主工程循环的插件（135 技能）**

面向 Claude Code、Cursor、Codex、Gemini CLI、OpenCode 等平台的插件，将 AI 编码助手改造为自主迭代工程循环：度量、修改、验证、保留或回滚，直至目标达成。提供 135 个技能（13 个领域）、7 个并行子代理（每代理独立 git worktree，每轮最多 5 个）、失败记忆系统（8 类失败分类、跨会话持久化于 .godmode/lessons.md）、Karpathy 作者纪律预置与四层 token 优化（声明约 90% 路由上下文缩减）。基准为仓库自测：30 个小任务、同模型双臂对比。

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

- measure–modify–verify–keep/revert 迭代循环，回归自动 git 回滚
- 135 个技能跨 13 个领域，7 个子代理并行执行（独立 worktree）
- 失败分类（8 类）与跨会话教训持久化
- 四层 token 优化：渐进披露路由、stdio 压缩、terse 输出、token 日志

## 适用场景

- 让现有 AI 编码助手自主迭代优化代码直至指标达标
- 多代理并行开发并在隔离 worktree 中合并测试
- 自动化安全审计（STRIDE + OWASP）与 TDD 测试生成

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L126: Godmode is an open-source plugin that adds autonomous coding capabilities to AI assistants like Claude Code, Curso
> L128: It ships with 135 expert skills across 13 domains (performance optimization, security auditing, TDD, deployment, d

## 星数曲线

```mermaid
xychart-beta
    title "arbazkhan971/godmode 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-27 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bb3e95e7a5a0` · [字段定义](../../DATASET.md)*
