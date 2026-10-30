# TheAstrelo/Claude-Pipeline

⭐ 47 · Shell · MIT · 推送 2026-09-04 · [GitHub](https://github.com/TheAstrelo/Claude-Pipeline) · 个人维护

**面向 Codex/Claude Code 的 13 阶段自动化 AI 开发流水线**

用单一 Bash 引擎驱动的 AI 编程流水线，将任务描述转化为经审查并提交的代码：13 个阶段（0–12）覆盖需求、设计、对抗性审查、计划、实现、质量检查、安全审计与最终代码审查提交。支持 Codex 与 Claude Code 两类 provider，提供 Opus/Sonnet 与 GPT-5.6 Sol/Terra 的版本化路由、确定性 QA 路径、非豁免安全扫描器、预算上限与断点恢复。限制：模板、--fix 等功能仍在路线图中未实现，生产自动提交要求仓库初始状态干净。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 13 阶段流水线，含对抗性设计审查与 OWASP 安全扫描
- Claude/Codex 双 provider，版本化模型路由与 4 档 profile
- 确定性 QA 路径：干净阶段零模型调用
- Phase 12 审查真实 git diff，仅 APPROVE 才提交并支持有限自动修复

## 适用场景

- 让 AI 编程工具按结构化流程交付经过审查的代码
- 在提交前自动执行安全扫描与测试门禁
- 对 AI 生成的变更做代码审查并自动提交

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L11: One command. 13 phases (0–12). Design review, security, testing, and a final code-review-and-commit gate — handled 
> L18: Built for **Codex and Claude Code** with one Bash engine.
> L35: - Uses Claude tool allowlists or Codex sandbox boundaries per phase

## 星数曲线

```mermaid
xychart-beta
    title "TheAstrelo/Claude-Pipeline 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 45 --> 48
    line [46, 47, 47]
```

2026-10-18 46 → 2026-10-30 47（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `ddba92f0cfdd` · [字段定义](../../DATASET.md)*
