# rubyroidlabs/rails-audit-skill

⭐ 16 · MIT · 推送 2026-08-12 · [GitHub](https://github.com/rubyroidlabs/rails-audit-skill) · [官网](https://rubyroidlabs.com) · 组织维护

**面向 agent 的 Rails 应用审计技能：产出分级审计报告与评分**

运行于 Claude Code、Cursor 等 agent harness 的技能（skill），对 Ruby on Rails 应用执行六阶段技术审计：并行子代理运行 Brakeman、RubyCritic、bundler-audit、Gitleaks、Debride 等工具，再对后端、前端、测试、Git、基础设施、AI 工具链等 7 个领域做人工式代码审查，最终生成 RAILS_AUDIT_REPORT.md，含 Critical/High/Medium/Low 分级发现、0-10 评分与三层优先建议。非侵入式设计：临时添加依赖并在结束后还原。审计质量依赖所用模型的推理能力，高推理模型 token 消耗与时长大。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六阶段审计流程：工具并行收集 + 源码逐领域审查 + 结构化报告
- 集成 Brakeman、RubyCritic、bundler-audit、Gitleaks、Debride 等 10+ 分析工具并按项目自动选择
- 输出 Critical/High/Medium/Low 分级发现、0-10 评分与三层优先建议
- 非侵入式：依赖临时添加、运行后还原 Gemfile 与工作区

## 适用场景

- 让 Claude Code 或 Cursor 对我的 Rails 项目做全面技术审计
- 交付客户前检查 Rails 应用的安全问题与依赖漏洞
- 只针对 app/models 等特定目录做定向审计

## 场景标签

`代码审查` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L3: An agent skill that performs comprehensive technical reviews of Ruby on Rails applications. Runs automated analysis 
> L7: Works with any agent harness that supports skills — [Claude Code][claude-code], [Cursor][cursor], and others.

## 星数曲线

```mermaid
xychart-beta
    title "rubyroidlabs/rails-audit-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f0b802a4deca` · [字段定义](../../DATASET.md)*
