# ZaxbyHub/opencode-swarm

⭐ 510 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/ZaxbyHub/opencode-swarm) · 组织维护

**OpenCode 的多 agent 群体编码插件：架构师主导、门禁式流水线**

面向使用 OpenCode 的开发者的插件，将单一 AI 编码会话转变为架构师（architect）协调的专职 agent 团队：编码、评审、测试、安全检查等角色分工，通过门禁流水线在 reviewer 与 test engineer 批准后才交付代码。机制包括独立自动评审引擎、shell 写入静态检测、跨进程 scope 强制、13 种语言配置与 tree-sitter 解析校验、Epic 并行波次模式（可选）、外部技能治理管线；状态存于 .swarm/ 可恢复。安装需 Bun ≥1.3.13 或 Node.js ≥22.13，部分高级功能（外部技能、技能优化器、PR Monitor）默认关闭需配置开启。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- architect 主导的专职 agent 团队与门禁式 QA 流水线
- shell 命令写入静态检测与跨进程 scope 强制（TTL、symlink 防护）
- 13 种语言配置与 tree-sitter 20 种语法解析校验
- Epic Mode 并行波次执行，每个 coder 在隔离 worktree 中工作

## 适用场景

- 让 AI 编码会话自动走评审+测试门禁再交付
- 在多 agent 并行编码中防止文件范围冲突与越权写入
- 通过 GitHub Action 从 issue 标签触发实现流水线并产出证据 PR

## 场景标签

`多智能体` `编码 Agent` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L13: OpenCode Swarm is a plugin for OpenCode that turns a single AI coding session into an **architect-led team of speci
> L25: Most AI coding tools let one model write code and ask that same model whether the code is good. That misses too muc

## 星数曲线

```mermaid
xychart-beta
    title "ZaxbyHub/opencode-swarm 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-24"]
    y-axis "stars" 504 --> 512
    line [505, 507, 511, 510]
```

2026-10-18 505 → 2026-10-24 510（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1b3616e89643` · [字段定义](../../DATASET.md)*
