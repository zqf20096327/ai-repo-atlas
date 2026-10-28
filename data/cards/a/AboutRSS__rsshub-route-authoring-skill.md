# AboutRSS/rsshub-route-authoring-skill

⭐ 24 · JavaScript · MIT · 推送 2026-09-16 · [GitHub](https://github.com/AboutRSS/rsshub-route-authoring-skill) · 组织维护 · 中文 README

**辅助 agent 编写可通过评审的 RSSHub 路由的技能包**

标准 Agent Skills 包（根目录含 SKILL.md），可被 CodeBuddy、Antigravity、Claude Code 等实现该标准的 agent 加载。规则内容提炼自 DIYgod/RSSHub 的 2,727 个路由 PR 与 18,680 条评审评论，可经 tools/ 流水线用 npm run fetch && npm run analyze 复现。使用时需在 RSSHub 检出目录内运行，配合 gh 认证与 Node.js/pnpm 环境；提供选择器验证与提交前静态检查脚本。声明为非官方社区项目，与 RSSHub 官方文档冲突时以后者为准。

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

- 规则提炼自 2,727 个路由 PR 与 18,680 条评审评论，计数可复现
- 标准 Agent Skills 包，兼容 CodeBuddy/Antigravity（已验证）与 Claude Code（文档记载）
- 提供 verify-selectors 选择器验证与 pre-submit 静态检查脚本
- 反馈回传机制要求用户显式同意，默认不做任何网络操作

## 适用场景

- 让 AI agent 首次提交即写出可通过 RSSHub 评审的路由代码
- 在提交 PR 前用脚本验证选择器与静态规范
- 了解 RSSHub 评审者最常要求修改的问题清单

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L100: This is a plain Agent Skills package: a folder with a
> L34: The rule content here is derived from real review data and is reproducible with `tools/`.

## 星数曲线

```mermaid
xychart-beta
    title "AboutRSS/rsshub-route-authoring-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-28 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `fb086897d3f6` · [字段定义](../../DATASET.md)*
