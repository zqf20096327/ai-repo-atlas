# codingjoe/esupgrade

⭐ 15 · JavaScript · BSD-2-Clause · 推送 2026-10-27 · [GitHub](https://github.com/codingjoe/esupgrade) · 个人维护

**面向 JavaScript/TypeScript 开发者的语法自动升级工具**

esupgrade 是一个自动重写 JavaScript/TypeScript 语法的 CLI 工具：基于 Web Platform Baseline 浏览器兼容策略，将 var、字符串拼接、传统 for 循环、Object.assign、Math.pow 等旧写法转换为 const/let、模板字面量、for...of、对象展开、指数运算符等现代语法。支持 .js/.jsx/.ts/.tsx/.mjs/.cjs 等文件类型，可通过 npx 运行，也可集成到 pre-commit、husky 或作为 Claude Code agent skill 安装。含 newly-available 选项以启用更新特性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Baseline 浏览器兼容策略执行语法转换
- 支持 var→const/let、Object.assign→对象展开、Math.pow→** 等多项转换
- 提供 pre-commit、husky 集成与 Claude Code agent skill 形式
- 支持 .js/.jsx/.ts/.tsx/.d.ts/.mjs/.cjs 七种文件类型

## 适用场景

- 把存量 JS/TS 代码自动升级为现代语法
- 在 pre-commit/husky 钩子中自动执行语法升级
- 让 Claude Code 通过 agent skill 分析并建议代码转换

## 场景标签

 · 领域:前端开发工具

## 证据(README 行号)

> L64: esupgrade is available as a skill in [Claude Code]. The plugin is distributed via the codingjoe/claude-plugins mark
> L1: esupgrade: Auto-upgrade your JavaScript syntax

## 星数曲线

```mermaid
xychart-beta
    title "codingjoe/esupgrade 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `69aa7ac5eabf` · [字段定义](../../DATASET.md)*
