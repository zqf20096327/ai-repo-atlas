# BeeBombshell/brilliant

⭐ 24 · TypeScript · MIT · 推送 2026-06-16 · [GitHub](https://github.com/BeeBombshell/brilliant) · [官网](https://brilliant.beebombshell.com) · 个人维护

**对话式 AI 日历应用：通过聊天管理 Google 日程**

基于 React 构建的日历应用，提供日/周/月视图、拖拽建事件，并与 Google Calendar 双向同步（每 60 秒自动同步、5 并发批量同步队列）。AI 部分通过 Tambo 平台实现：聊天界面调用 5 个 AI 工具（创建/查询/修改/删除/批量更新日历事件），配合时间、视图、即将到来事件三类上下文助手，支持生成式表单与会话历史及检查点回退。采用无后端的 OAuth2 Implicit Flow，token 约 1 小时过期后需重新认证；复杂重复规则（BYSETPOS、EXDATE）暂不支持。

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

- 聊天式日程管理：5 个 AI 工具含批量更新
- Google Calendar 双向同步（60 秒间隔、5 并发批量队列）
- 时间/视图/事件三类上下文助手提供实时日历感知
- 检查点式撤销/回退系统与生成式表单

## 适用场景

- 用自然语言创建、移动、批量调整日程
- 在日/周/月视图中配合 AI 聊天管理日程
- 需要 Google Calendar 双向同步的日历前端

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: An intelligent calendar application with conversational AI capabilities, built with React and integrated with Google
> L11: - **Day View**: Focus on a single day with time-based event layout
> L17: ### AI-Powered Scheduling (via Tambo)

## 星数曲线

```mermaid
xychart-beta
    title "BeeBombshell/brilliant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `86fce9657298` · [字段定义](../../DATASET.md)*
