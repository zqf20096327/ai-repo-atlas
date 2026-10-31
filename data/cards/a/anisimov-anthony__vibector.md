# anisimov-anthony/vibector

⭐ 13 · Go · MIT · 推送 2026-01-10 · [GitHub](https://github.com/anisimov-anthony/vibector) · 个人维护

**通过提交模式检测 AI 生成代码的 Git 仓库分析工具**

Go 编写的本地 Git 仓库分析工具，通过提交大小、代码速度（每分钟增删行数）、提交时间间隔与百分位统计等提交模式，标记可能为 AI 生成的代码提交。提供可配置阈值（flags、.vibector.yaml 或环境变量）、文件排除、text/JSON 双输出格式；分析为只读操作，完全离线、无遥测、不修改仓库。以 go install 或源码编译安装，供开发与审计场景使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按提交大小、速度、时间间隔与百分位统计标记可疑提交
- 阈值可通过 flags、配置文件与环境变量设置
- text 与 JSON 输出格式，支持文件排除
- 只读分析，完全离线，无数据传输

## 适用场景

- 审查仓库中疑似 AI 生成的大批量提交
- 代码评审优先级排序与仓库合规审计
- 团队编码速度研究分析

## 场景标签

 · 领域:开发者工具/代码审计

## 证据(README 行号)

> L8: **Vibector** is a Git repository analysis tool designed to detect potential AI-generated code by examining commit pa
> L61: Analyze a repository for suspicious commits that may indicate AI-generated code.

## 星数曲线

```mermaid
xychart-beta
    title "anisimov-anthony/vibector 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `51b75f2e0e05` · [字段定义](../../DATASET.md)*
