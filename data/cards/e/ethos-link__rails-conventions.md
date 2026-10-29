# ethos-link/rails-conventions

⭐ 18 · Ruby · MIT · 推送 2026-10-27 · [GitHub](https://github.com/ethos-link/rails-conventions) · 组织维护

**面向编码 Agent 的 Rails 8 约定技能包：按既有代码库规范写码与审查**

一个 SKILL.md 格式的 Rails 编码约定技能，供 Claude/Codex 类编码 Agent 加载：引导 Agent 先检查代码库既有模式（模型、控制器、路由、测试、部署），再按现有命名与分层约定编写代码；覆盖 Active Record 建模、迁移纪律、GoodJob/Solid Queue 后台任务、安全清单（含 SSRF 加固与多租户）、价值导向测试等范围。通过 npx skills 命令安装与更新，附验证脚本与前瞻测试提示词。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 引导 Agent 先检视本地模式再按既有约定生成代码
- 覆盖 Active Record/PostgreSQL、后台任务适配器检测、安全清单与测试策略
- 迁移与 installer 文件由生成器产出而非手工编造
- 提供 ruby scripts/validate_skill.rb 验证脚本与 npx skills 安装/更新命令

## 适用场景

- 团队用编码 Agent 在既有 Rails 代码库中保持一致风格
- 用 Agent 审查 Rails 8 PR 的生产就绪度
- 让 Agent 编写适配 GoodJob/Solid Queue 的后台任务

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L8:  SKILL.md ·
> L13: `rails-conventions` is for real production work in Rails codebases where consistency matters.
> L17: - inspect local patterns first (models, controllers, routes, tests, deploy setup)

## 星数曲线

```mermaid
xychart-beta
    title "ethos-link/rails-conventions 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `c9d4998786fa` · [字段定义](../../DATASET.md)*
