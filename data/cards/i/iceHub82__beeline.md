# iceHub82/beeline

⭐ 13 · Python · MIT · 推送 2026-08-04 · [GitHub](https://github.com/iceHub82/beeline) · 个人维护

**Claude Code 输出压缩插件：合并 caveman 与 i-have-adhd 风格规则**

面向 Claude Code 的输出风格插件：合并 i-have-adhd 的结构规则（行动先行、编号步骤、结尾单一动作）与 caveman 的省略规则，并新增工具输出纪律规则组（源头过滤、引用关键行、批量独立调用等）。提供 lite/full/ultra 三档压缩级别，仅作用于散文输出，不压缩代码与安全确认。附有基于真实 1,133 轮会话和 12 项代理循环任务的基准测试，说明节费效果取决于工作负载。经 Claude Code 插件市场命令安装。

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

- 合并两个既有输出风格规则集并扩展工具输出纪律规则组（规则 11–18）
- lite/full/ultra 三档压缩级别，仅影响散文输出
- 基准测试显示工具输出进入上下文减少 57–67%
- 单轮盲评（第二模型打分）覆盖 answered/actionable/complete/readable 四维

## 适用场景

- 长代理会话中压缩 Claude Code 的工具输出与散文以减少 token 消耗
- 让 AI 回复以行动为先、更易执行
- 在大量日志/测试套件输出的任务中推迟上下文压缩

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Compressed, action-first output for Claude Code.
> L78: /plugin marketplace add iceHub82/beeline
> L113: Supersedes `caveman` and `i-have-adhd` — running them together is contradictory.

## 星数曲线

```mermaid
xychart-beta
    title "iceHub82/beeline 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `3e3e8def4cdc` · [字段定义](../../DATASET.md)*
