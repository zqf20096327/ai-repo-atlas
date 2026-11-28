# star-kz/dsh-subagent-model-switcher

⭐ 3 · JavaScript · MIT · 推送 2026-11-04 · [GitHub](https://github.com/star-kz/dsh-subagent-model-switcher) · 个人维护 · 中文 README

**DSH 子 agent 会话的模型与思考强度切换插件**

一个 DSH（DeepSeek Harness）插件，在子 agent 会话输入框中提供模型与思考强度选择器，主会话不渲染、不改动官方选择器。运行中的子 agent 后续请求即可生效；选择按会话持久化保存，支持清除覆盖恢复默认继承。通过插件 Host 端的设置覆盖与 agent 事件实现切换，不调用官方会拒绝子会话的 session/selectModel。通过 DSH 插件管理安装，需 DSH Web 与 @deepseek-ai/schemastery。

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

- 仅为子 agent 会话提供模型与思考强度选择器，主会话不渲染
- 运行中的子 agent 在后续请求中生效
- 选择按会话保存，重启后仍有效，可清除覆盖恢复默认
- 基于插件 Host 端设置覆盖与 agent 事件实现

## 适用场景

- 在 DSH 中为不同子 agent 会话指定不同的模型与思考强度
- 重启后保持子 agent 会话的模型选择
- 需要临时覆盖子会话模型并随时恢复默认的场景

## 场景标签

 · 领域:开发工具/Agent 基础设施

## 证据(README 行号)

> L3: **子 agent 会话模型切换** —— 给 DeepSeek Harness 子会话输入框补上「模型 + 思考强度」选择器。
> L10: - 可切换模型与思考强度；运行中的子 agent 在后续请求生效。

## 星数曲线

```mermaid
xychart-beta
    title "star-kz/dsh-subagent-model-switcher 星数(近 2 点)"
    x-axis ["2026-11-23", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-23 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `114f21184091` · [字段定义](../../DATASET.md)*
