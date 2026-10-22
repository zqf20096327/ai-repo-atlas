# VeryGoodOpenSource/vgv-ai-flutter-plugin

⭐ 173 · Shell · MIT · 推送 2026-10-20 · [GitHub](https://github.com/VeryGoodOpenSource/vgv-ai-flutter-plugin) · 组织维护

**给 Flutter/Dart 开发者的 Claude Code 最佳实践技能插件**

Very Good Ventures 开发的 Claude Code 插件：以技能（skills）、子代理（agents）和钩子（hooks）形式向 Claude Code 注入 VGV 的 Flutter/Dart 开发规范。技能覆盖项目脚手架、Bloc 状态管理、GoRouter 导航、无障碍（WCAG 2.2）、国际化、安全审查、四道质量门禁等；hooks 校验 Very Good CLI、阻止 CLI 绕行并自动执行 dart analyze/format；附带两个 MCP 服务器配置与技能评测（evals）机制。技能在对话中按上下文自动激活，也可用斜杠命令调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 十余项技能覆盖架构、测试、无障碍、安全、许可证合规与 SDK 升级等
- flutter-reviewer 只读子代理按 VGV 标准审查变更代码
- SessionStart/PreToolUse/PostToolUse hooks 自动校验 CLI 并执行分析与格式化
- 连接 Dart/Flutter 与 Very Good CLI 两个 MCP 服务器
- 技能评测用对照实验区分技能效果与模型能力

## 适用场景

- 让 Claude Code 按 VGV 规范编写 Flutter/Dart 代码
- 自动化代码审查、质量门禁与 SDK 升级
- 为新项目按模板脚手架生成标准结构

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L6: A [Claude Code][claude_code_link] plugin that accelerates Flutter & Dart development with best-practices skills from
> L12: VGV AI Flutter Plugin is a collection of contextual best-practices skills that Claude uses when helping you write F

## 星数曲线

```mermaid
xychart-beta
    title "VeryGoodOpenSource/vgv-ai-flutter-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 171 --> 174
    line [172, 173]
```

2026-10-18 172 → 2026-10-22 173（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b3374223425f` · [字段定义](../../DATASET.md)*
