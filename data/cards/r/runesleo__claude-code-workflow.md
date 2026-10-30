# runesleo/claude-code-workflow

⭐ 709 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/runesleo/claude-code-workflow) · [官网](https://leolabs.me) · 个人维护 · 中文 README

**给 AI 编程 Agent 加可回滚工作边界的轻量配置系统**

面向使用 Claude Code、Codex 或 Cursor 的开发者，以最小配置模板（共享 AGENTS.md Core 约 1,604 字节 + 各客户端适配层）为 Agent 施加可靠性边界：先看现状、保留无关改动、按风险验证、不可逆动作先确认。安装器支持 dry-run 预览、--apply 写入、带时间戳备份与逐目标回滚；提供隔离 demo 项目做首次行为验收。不含任务数据库、后台自动化或团队编排。仓库另含作者个人系统结构（九条业务线、单 Writer、会话收尾）与多个实验性 Lab 作为可选参考。Windows PowerShell 安装器尚未提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一 Shared Core 同时适配 Claude Code / Codex / Cursor 三端
- 安装器默认 dry-run 预览，覆盖前自动备份、支持逐目标回滚
- 提供隔离 demo 项目的首次成功行为验收（保留无关改动、运行测试、给出验证证据）
- verify.sh 检查安装契约、回滚、模板体积上限与泄漏

## 适用场景

- 防止 AI 编程 Agent 覆盖未查看的现有改动或假报完成
- 删除、发布、生产变更等不可逆动作前强制确认
- 更换 AI 编程工具时把同一组工作边界带到新客户端

## 场景标签

 · 领域:AI 编程工具/Agent 工作流

## 证据(README 行号)

> L7: > 给你已经在使用的 AI 编程 Agent 装上一层极小、可回滚的工作边界：先看现状、保留无关改动、按风险验证、对不可逆动作先确认。
> L141: Claude Code、Codex 和 Cursor 都能获得同一组核心可靠性行为，但你只需要安装自己正在使用的客户端。Codex 直接读取 shared `AGENTS.md`，Claude Code 通过薄入口引用它；Cur
> L143: |客户端|常驻模板|字节数|

## 星数曲线

```mermaid
xychart-beta
    title "runesleo/claude-code-workflow 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24", "2026-10-30"]
    y-axis "stars" 707 --> 710
    line [709, 708, 709, 709]
```

2026-10-18 709 → 2026-10-30 709（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d63c1c1dee70` · [字段定义](../../DATASET.md)*
