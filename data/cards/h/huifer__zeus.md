# huifer/zeus

⭐ 22 · Shell · MIT · 推送 2026-04-07 · [GitHub](https://github.com/huifer/zeus) · [官网](https://tanstackship.com/) · 个人维护 · 中文 README

**面向长期项目的结构化 AI 交付框架（Claude Code 技能集）**

以 Claude Code skills/agents 形式提供的项目交付框架：用确定性规划工件（spec/prd/task/roadmap）约束 AI，按 wave 逐波执行并产出原子提交，通过 Git commit-msg 钩子强制提交规范。包含 6 个阶段角色 agent（researcher/planner/executor/analyst/docs/tester），支持 android/chrome/ios 三平台 AI 生成测试流（依赖 adb、chrome-cli、xcrun simctl 等平台工具链），并以生产反馈归因驱动的版本演进闭环。限制：不手动写测试用例，需在 Claude 类 AI runtime 中运行。

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

- spec/prd/task/roadmap 确定性规划工件 + wave 式原子执行
- commit-msg Git 钩子强制提交规范（如 feat(T-003)）
- android/chrome/ios 三平台 AI 生成测试流与原生工具链执行
- 6 个阶段角色 agent 分工与 ai-logs 决策日志契约

## 适用场景

- 长期项目中用 Claude Code 按规格驱动的流程开发与执行
- 存量代码库的安全接管（/zeus:discover 生成上下文工件）
- 多平台（Android/iOS/Chrome）自动生成并执行测试流

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L8: Structured, version-aware AI delivery framework for long-running projects.
> L80: Zeus uses phase-specific agents under `.claude/agents`:

## 星数曲线

```mermaid
xychart-beta
    title "huifer/zeus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `aea76fac89aa` · [字段定义](../../DATASET.md)*
