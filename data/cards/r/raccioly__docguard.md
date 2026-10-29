# raccioly/docguard

⭐ 32 · JavaScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/raccioly/docguard) · [官网](https://www.npmjs.com/package/docguard-cli) · 个人维护

**校验项目文档一致性并为 AI agent 生成修复提示的 CLI 工具**

面向规范驱动开发（CDD）的文档校验层：检查文档声明与仓库证据是否一致（如 API-Reference 端点对照 OpenAPI spec），检测漂移，输出 CDD 成熟度评分。漂移分为机械类（docguard fix --write 自动改，无 AI）与 agent 类（diagnose 输出 AI 可执行的修复提示）。作为 GitHub Spec Kit 官方社区扩展校验 spec.md/plan.md/tasks.md 结构，另提供 MCP server（只读、Docker 镜像）、pre-commit 钩子、GitLab CI 组件与 GitHub Action。分发渠道为 npm 核心包（无安装脚本）、PyPI 薄包装（仍需 Node.js 18+）与 Homebrew。README 明确引用研究但不据此声称工具有效性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- diagnose→AI 修复→guard 验证的文档漂移闭环，区分机械修复与 agent 修复
- Spec Kit 官方社区扩展，校验 spec/plan/tasks 的章节结构与 FR/SC/T ID 追溯
- 只读 MCP server 以 GHCR 容器镜像分发，无需 Node.js
- guard/diagnose 支持 JSON 输出并标记每个 issue 的 mechanical/agent 归属

## 适用场景

- 在 CI/pre-commit 中拦截文档与代码漂移
- 让编码 agent 按 diagnose 生成的提示修复过时文档
- 校验 Spec Kit 产出的 spec.md/plan.md/tasks.md 质量
- 为 AI agent 提供经校验的共享文档上下文

## 场景标签

 · 领域:开发者工具/文档治理

## 证据(README 行号)

> L33: DocGuard enforces **Canonical-Driven Development (CDD)** — a methodology where documentation is the source of truth
> L135: diagnose  →  AI reads prompts  →  AI fixes docs  →  guard verifies
> L165: DocGuard is a community extension for GitHub's **Spec Kit** framework. While Spec Kit focuses on **creating** spec

## 星数曲线

```mermaid
xychart-beta
    title "raccioly/docguard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-29 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `547c6c855c00` · [字段定义](../../DATASET.md)*
