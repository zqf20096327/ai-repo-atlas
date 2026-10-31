# triggerdotdev/agentcrumbs

⭐ 13 · TypeScript · 推送 2026-03-13 · [GitHub](https://github.com/triggerdotdev/agentcrumbs) · [官网](https://agentcrumbs.dev) · 组织维护

**给 AI agent 用的运行时结构化追踪库：写码留痕、合并前剥离**

面向 AI 编码 agent 的开发期追踪工具：agent 写代码时内联埋入 trail/crumb 调用，故障时启动 Collector 并用 query/tail 查询结构化轨迹，查看实际执行顺序与数据。crumb 仅存在于功能分支，`agentcrumbs strip` 在合并前剥离全部标记，CI 用 `strip --check` 强制。禁用时返回冻结 noop 函数，零运行时依赖。以 npm 包分发，内置 @tanstack/intent 技能接入 Claude Code、Cursor 等 agent 配置；支持 Node.js 18+/Bun/浏览器，collector 与语言无关。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- trail/crumb/scope/wrap/snapshot 等 API 生成结构化执行轨迹
- `agentcrumbs strip` 剥离标记，CI 以 `strip --check` 校验
- 禁用命名空间返回冻结 noop 函数，零运行时依赖
- collector 语言无关，任意支持 HTTP 的语言可发送 crumb，多服务输出交织查看

## 适用场景

- AI agent 修复运行时故障时查询实际执行轨迹而非猜测
- 多服务开发期统一收集内联追踪数据
- 通过 CI 强制保证调试埋点不进入主分支

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: AI agents can read your code but they can't see what happened at runtime. agentcrumbs fixes that. Agents drop struct
> L21: The agent will wire the skills into your agent config (CLAUDE.md, .cursorrules, etc.), then scan your repo to build

## 星数曲线

```mermaid
xychart-beta
    title "triggerdotdev/agentcrumbs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `326f91c5791b` · [字段定义](../../DATASET.md)*
