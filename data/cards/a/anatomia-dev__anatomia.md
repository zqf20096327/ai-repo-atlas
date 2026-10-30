# anatomia-dev/anatomia

⭐ 33 · TypeScript · MIT · 推送 2026-09-11 · [GitHub](https://github.com/anatomia-dev/anatomia) · [官网](https://anatomia.dev) · 组织维护

**面向 Claude Code 与 Codex 的五阶段 agent 流水线 CLI**

Node.js CLI 工具，扫描代码库识别框架、数据库、约定与模式，生成 ana.json、scan.json、CLAUDE.md/AGENTS.md 等供 agent 读取的上下文文件与技能模板。变更经 Think/Plan/Build/Verify/Learn 五阶段流水线处理，每阶段产出 scope.md、spec.md、contract.yaml、build_report.md、verify_report.md 等工件，CLI 校验工件结构并计算内容哈希。proof chain 记录每次运行的断言满足率与发现，可转化为技能规则。原生支持 Claude Code 与 Codex，扫描输出兼容任何读取 markdown 的 AI 工具。需 Node.js 22+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扫描识别技术栈与约定，生成 agent 上下文与 5+3 个技能模板
- 五阶段流水线（scope/plan/build/verify/learn）产出可审计工件链
- CLI 校验 agent 保存的工件结构并计算内容哈希，拒绝格式错误输出
- proof health/promote/audit/stale 跟踪验证率与发现轨迹

## 适用场景

- 在 Claude Code 或 Codex 中以结构化流水线管理代码变更
- 为代码库生成供 AI 工具读取的项目上下文文件
- 跨运行追踪构建验证率与问题聚集点

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: Anatomia is a CLI and agent harness for Claude Code and Codex. It scans your codebase — detecting your stack, conven
> L92: Pipeline agents invoke ~20 additional CLI commands — the toolbelt. When an agent saves an artifact, the CLI validat
> L96: Native pipeline support for Claude Code and Codex.

## 星数曲线

```mermaid
xychart-beta
    title "anatomia-dev/anatomia 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-30 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `36031a6ed324` · [字段定义](../../DATASET.md)*
