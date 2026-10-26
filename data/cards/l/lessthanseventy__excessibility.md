# lessthanseventy/excessibility

⭐ 43 · Elixir · MIT · 推送 2026-10-08 · [GitHub](https://github.com/lessthanseventy/excessibility) · [官网](https://hexdocs.pm/excessibility) · 个人维护

**Phoenix LiveView 的无障碍快照测试库（axe-core/WCAG）**

面向 Elixir/Phoenix 开发者的 Hex 包：在 ExUnit/Wallaby/LiveView 测试中用 html_snapshot 宏捕获 HTML 快照，测试后通过 Playwright 运行 axe-core 检查 WCAG 违规；支持基线锁定、快照对比审批、以 JSON 输出变更影响面（blast radius）供 CI 使用，可生成 Playwright 截图。另提供 LLM 调试指南：telemetry 自动采集、mix excessibility.debug、运行时证据摘要、MCP server 与 Claude Code 技能。本体为测试工具，AI 能力用于调试辅助。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 测试内捕获 HTML 快照，测试后经 Playwright 跑 axe-core 做 WCAG 检查
- 基线锁定、快照对比与交互式审批工作流
- mix excessibility.review 输出变更新引入的无障碍问题（支持 --format json）
- LLM 调试指南：telemetry 采集、debug 任务、MCP server 与 Claude Code 技能

## 适用场景

- 在现有 Phoenix 测试流程中持续检测无障碍回归
- 重构时锁定无障碍基线并审批差异
- CI 中与功能测试失败并列展示 axe-core 违规报告
- 配合 Claude Code 等 LLM 工具调试无障碍失败

## 场景标签

 · 领域:Web 开发/测试工具

## 证据(README 行号)

> L11: Excessibility helps you test your Phoenix apps for accessibility (WCAG compliance) by taking HTML snapshots during 
> L128: - LLM Debugging Guide — telemetry auto-capture, `mix excessibility.debug`, the runtime evidence digest, MCP server

## 星数曲线

```mermaid
xychart-beta
    title "lessthanseventy/excessibility 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-26 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `f2ced34042c4` · [字段定义](../../DATASET.md)*
