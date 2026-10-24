# cxuu/golang-skills

⭐ 181 · HTML · Apache-2.0 · 推送 2026-06-20 · [GitHub](https://github.com/cxuu/golang-skills) · 个人维护

**给 AI 编程助手的 Go 语言最佳实践技能包（20 项技能）**

面向 AI 编程助手的 Agent Skills 集合：20 个模块化技能教 AI 助手编写地道、生产级 Go 代码，内容提炼自 Google/Uber Go 风格指南、Effective Go 与 Go Wiki 评审意见。机制上采用渐进式披露（48 个参考文件按需加载）、决策树式流程指引、8 个自动化检查脚本与 4 个资产模板。兼容 Claude Code、Cursor、Codex 等多种 agent 工具，通过 npx skills 一键安装。上游来源快照保留于 source/ 目录并在 THIRD_PARTY_NOTICES.md 记录许可信息。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20 个模块化 Go 技能，覆盖并发、错误处理、测试、性能等主题
- 48 个参考文件按需加载（渐进式披露），减少上下文占用
- 8 个捆绑脚本自动执行 gofmt/vet/lint、命名检查、测试脚手架等
- 支持 npx skills、Claude Code 插件市场、Cursor 远程规则三种安装方式

## 适用场景

- 让 Claude Code / Cursor 等 AI 助手按 Google/Uber 风格写 Go 代码
- 为 AI 编程助手的 Go 代码评审提供系统性检查清单
- 通过捆绑脚本自动执行命名、文档、错误处理等常规检查

## 场景标签

`代码生成` `代码审查` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: AI Agent Skills for writing idiomatic,
> L92: These skills follow the Agent Skills open standard,

## 星数曲线

```mermaid
xychart-beta
    title "cxuu/golang-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 179 --> 182
    line [180, 181, 181]
```

2026-10-18 180 → 2026-10-24 181（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ebed8ef2b3a0` · [字段定义](../../DATASET.md)*
