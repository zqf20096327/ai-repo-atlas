# VisionForge-OU/foreman

⭐ 443 · Python · NOASSERTION · 推送 2026-06-29 · [GitHub](https://github.com/VisionForge-OU/foreman) · 组织维护

**监督 headless Claude Code agents 的门控交付编排 TUI**

面向开发者的终端编排工具：在任意仓库上运行 plan→ADR/PRD→issues→TDD build→e2e 流水线，设计阶段设人工审批门（SHA-256 哈希封存），构建阶段以本地 claude CLI headless stream-json 模式驱动并行 worker，各在独立 git worktree 中执行，编排器强制 turn/cost/time 预算、每日成本上限与 PreToolUse 拒绝钩子。全部状态为仓库内人类可读文件，无数据库，可从磁盘恢复。要求 Python 3.11+、claude CLI 与 git，在 Linux/WSL2 上开发测试。提供 retro 失败聚类与 bench 基准的门控技能/提示补丁飞轮。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 门控流水线：plan→ADR/PRD→issues→TDD build→e2e，设计阶段人工审批
- 并行 worker 各在独立 git worktree 中运行，按 touches 足迹防冲突
- 编排器强制预算上限、每日成本硬停与合并门（证据/验收/回归棘轮）
- 无数据库：全部状态为仓库内人类可读文件，崩溃后从磁盘恢复

## 适用场景

- 让 Claude Code agents 按门控流程自动完成功能交付
- 在代理构建中保留人工设计审批与升级处理
- 对失败的 agent 运行做 retro 聚类并生成需过基准的提示补丁

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L20: Foreman spawns the locally-installed `claude` CLI in headless stream-json mode,
> L36: - 🤖 **Real headless agents** — spawns the locally-installed `claude` CLI in stream-json mode, parses its events, an

## 星数曲线

```mermaid
xychart-beta
    title "VisionForge-OU/foreman 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 442 --> 446
    line [443, 444, 445]
```

2026-10-18 443 → 2026-10-24 445（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `58f207d1214b` · [字段定义](../../DATASET.md)*
