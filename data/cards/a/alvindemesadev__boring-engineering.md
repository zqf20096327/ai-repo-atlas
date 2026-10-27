# alvindemesadev/boring-engineering

⭐ 22 · JavaScript · MIT · 推送 2026-08-26 · [GitHub](https://github.com/alvindemesadev/boring-engineering) · [官网](boring-engineering.pages.dev) · 个人维护

**防止 AI 编程代理过度设计的 SKILL.md 决策技能**

一个遵循 Agent Skills 开放规范的 SKILL.md 技能文件，供 AI 编程代理加载：将 KISS、YAGNI、实用 DRY 原则转化为 4 步决策系统（需求过滤、复用检查、最简正确方案、抽象必要性判断），代理在实现、重构或审查代码时自动激活。采用渐进披露三阶段加载以控制 token 消耗。通过 git clone 或 curl 复制文件到代理的 skills 目录安装，兼容 Claude Code、Cursor、Kiro、Copilot 等 40+ 工具，并提供对照基准测试结果。

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

- 将 KISS/YAGNI/DRY 转化为 4 步决策系统，代理编码时自动激活
- Agent Skills 渐进披露三阶段加载（发现/激活/深度参考）
- 兼容 40+ 工具的开放规范，单个 SKILL.md 跨代理使用
- 附带 v1.1 基准测试（12 tickets × 5 arms × 5 tries，300 单元）

## 适用场景

- 让编程代理在实现功能时避免过早抽象与过度设计
- 重构或代码审查时自动执行复杂度判断
- 在多个 AI 编程工具间复用同一份工程原则技能

## 场景标签

`代码审查` `编码 Agent` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: An AI agent skill that turns KISS, YAGNI, and practical DRY into a concrete decision system — so your coding agent s
> L70: This skill uses the Agent Skills open spec — a standard supported by 40+ tools as of 2026. One `SKILL.md`, any comp
> L91: #### Claude Code

## 星数曲线

```mermaid
xychart-beta
    title "alvindemesadev/boring-engineering 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8369cc58a0e1` · [字段定义](../../DATASET.md)*
