# PolarCoding85/convex-agent-skillz

⭐ 16 · MIT · 推送 2026-02-10 · [GitHub](https://github.com/PolarCoding85/convex-agent-skillz) · 个人维护

**面向 Convex 后端开发的 Claude Code 技能知识合集（6 技能+命令+Agent）**

为使用 Convex 后端框架的开发者提供的 Claude Code skills 集合：包含 6 个技能（convex 核心、convex-agent、convex-components、convex-auth、convex-clerk、convex-workos），按上下文自动激活，覆盖查询/变更、AI agent 构建、组件模式与认证集成；另含 /create-features 自定义命令和 convex-expert 自定义 Agent。安装方式为克隆仓库并复制 .claude 目录到项目根，前置条件是已安装 Claude Code 并有 Convex 项目。技能内容为 Markdown 参考文档，可自行扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个技能按上下文自动激活（查询/组件/认证/AI agent 触发词）
- 覆盖 @convex-dev 生态组件（Agent、Workflow、Rate Limiter、Stripe 等）的模式文档
- /create-features 命令将实现计划拆解为带验收标准的特性文档
- 技能以 SKILL.md + references/ 文档组织，支持自定义扩展

## 适用场景

- 在 Convex 项目中让 Claude Code 按 Convex 最佳实践辅助编写查询与 schema
- 为 AI 聊天/agent 功能获取 @convex-dev/agent 的线程、工具调用与流式模式指导
- 配置 Clerk 或 WorkOS 认证集成时获取对应模式参考

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A curated collection of Claude Code skills for Convex backend development. These skills give Claude deep expertise i
> L7: Skills are knowledge bases that Claude Code loads automatically based on context. When you're working in a Convex pr

## 星数曲线

```mermaid
xychart-beta
    title "PolarCoding85/convex-agent-skillz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4da5ff747356` · [字段定义](../../DATASET.md)*
