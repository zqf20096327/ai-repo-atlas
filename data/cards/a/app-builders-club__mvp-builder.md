# app-builders-club/mvp-builder

⭐ 13 · Shell · MIT · 推送 2026-09-06 · [GitHub](https://github.com/app-builders-club/mvp-builder) · 组织维护

**面向 Claude Code/Codex 的文档驱动开发框架：规格先行、TDD 强制、自审循环**

以插件形式安装到 Claude Code 与 Codex CLI 的 MVP 构建框架。核心机制是文档驱动开发：PRD 访谈生成 PRD.md，规格按 FR-XXX→TEST-XXX→IMPL-XXX→CHK→REV 结构化；编排会话派发专职 agent（design-setup、feature-docs、feature-tdd、feature-review、feature-fix、feature-memory）逐阶段生成文档与代码，构建阶段强制 RED-GREEN TDD 循环，审查产出 feedback.md 并逐条修复。支持 Figma 往返提取设计 token，规则与技能按文件路径加载。安装途径含 Claude 插件市场、Codex CLI 插件及独立 shell 脚本安装器。

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

- 规格→测试→实现→检查→评审的结构化追踪链，跳步可检测
- 主会话编排专职 agent 的流水线，阶段间校验报告
- 构建阶段强制 RED-GREEN TDD 循环与原子提交
- feature-review/feature-fix 自审修复循环与跨会话 AICODE 标记

## 适用场景

- 用 AI agent 构建 MVP 时防止半成品代码与占位实现
- 把产品想法经 PRD 访谈转为结构化规格再生成代码
- 在 Claude Code 或 Codex CLI 中运行带质量门禁的 agent 流水线

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L31: **Orchestrated agent pipeline.** The main session dispatches specialized agents and validates every report between 

## 星数曲线

```mermaid
xychart-beta
    title "app-builders-club/mvp-builder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `027c36133cda` · [字段定义](../../DATASET.md)*
