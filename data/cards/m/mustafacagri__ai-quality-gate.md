# mustafacagri/ai-quality-gate

⭐ 31 · TypeScript · MIT · 推送 2026-10-07 · [GitHub](https://github.com/mustafacagri/ai-quality-gate) · [官网](https://www.npmjs.com/package/ai-quality-gate) · 个人维护

**面向 AI 编辑器的 MCP 代码质量门禁服务器，自动修复与上报问题**

一个 MCP Server，供 Cursor、Antigravity、OpenCode 等 MCP 编辑器中的 AI 调用 quality_fix 工具，在代码修改后执行质量检查。采用两阶段混合机制：Phase 1 用 ESLint（627 条规则，含 SonarJS/Unicorn/TypeScript-ESLint 等插件）+ Prettier 自动修复约 2-8 秒；Phase 2 可选接入 SonarQube Server（约 30-60 秒）。无法自动修复的问题返回给 AI 处理；修复失败时回滚改动。支持自定义正则规则、i18n locale 键校验、交互式配置向导与 CLI 模式（--check/--fix 等）。

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

- quality_fix MCP 工具：AI 改码后调用，自动修复并返回剩余问题
- Phase 1：ESLint 627 条规则 + Prettier 自动修复（约 2-8 秒）
- Phase 2 可选 SonarQube 接入，支持 Docker 部署 SonarQube
- 修复失败时回滚机制与自定义 line-based regex 规则

## 适用场景

- 在 Cursor/Antigravity 等 MCP 编辑器中给 AI 生成的代码加质量门禁
- 团队为 AI 编码流程强制统一的 ESLint 质量标准
- 为 i18n 项目校验 locale JSON 键的一致性

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: MCP Server for AI code quality automation.
> L10: AI writes code → calls `quality_fix` → Server fixes what it can → Reports remaining issues to AI.
> L47: - **Cursor**, **Antigravity**, **OpenCode** (or another MCP-capable editor) with MCP enabled.

## 星数曲线

```mermaid
xychart-beta
    title "mustafacagri/ai-quality-gate 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-30 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `12c09789ab3e` · [字段定义](../../DATASET.md)*
