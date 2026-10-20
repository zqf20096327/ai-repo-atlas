# samber/cc-skills-golang

⭐ 3,521 · Go · MIT · 推送 2026-10-01 · [GitHub](https://github.com/samber/cc-skills-golang) · [官网](https://skills.sh/samber/cc-skills-golang) · 个人维护

**Go 语言 AI 编程助手技能集：30+ 条即载即用的领域规范**

面向 Claude Code、Codex、Gemini、Copilot、Cursor、Antigravity、Openclaw、OpenCode 等编码助手的 Go 语言 agentic skills 集合，以 SKILL.md 格式按需加载。技能覆盖代码风格、错误处理、安全、并发、测试、性能、可观测性等 29 个通用主题及 wire/cobra/testify 等 17 个工具库主题，由个人维护者基于自身 Go 项目提交用 Claude Code 引导生成后人工编辑与测试。提供 npx skills 安装、各客户端插件/克隆安装方式，并给出 3439 题的技能评测（整体 97% vs 无技能 57%）与各技能 token 权重。README 标注部分技能为进行中或待办（如 golang-temporal）。

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

- 29 个通用 Go 技能 + 17 个工具库技能（含 golang-code-style、golang-testing 等）
- 支持 skills CLI、Claude Code 插件、git clone 等多客户端安装方式
- 3439 题评测：启用技能 97% 通过率对比未启用 57%
- 技能为原子化交叉引用单元，标注 token 权重与可覆盖标记

## 适用场景

- 为我的编码助手补充 Go 语言编码规范与最佳实践
- 团队按需加载安全、测试、性能等专项 Go 技能
- 查找 wire/cobra/testify 等常用 Go 库的使用规范

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: AI agent skills are reusable instruction sets that extend your coding assistant with domain-specific expertise, load
> L109: ## 🧩 Skills
> L134: ||Skill|Flags|Error rate gap|Description (tok)|SKILL.md (tok)|Directory (tok)|

## 星数曲线

```mermaid
xychart-beta
    title "samber/cc-skills-golang 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-20"]
    y-axis "stars" 3502 --> 3522
    line [3503, 3521, 3521]
```

2026-10-18 3,503 → 2026-10-20 3,521（+18）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-20 · 置信度 high · 依据 README sha `e71c4049c6e4` · [字段定义](../../DATASET.md)*
