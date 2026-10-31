# DECRUX9812/typesafe-skill-router

⭐ 14 · Python · MIT · 推送 2026-09-21 · [GitHub](https://github.com/DECRUX9812/typesafe-skill-router) · 个人维护

**Hermes Agent 插件：调用前用 TypeSafe 挑出唯一值得加载的技能**

面向 Hermes Agent 的可选插件。当已安装技能达数百个时，模型可能读漏合适的技能；本插件在模型调用前先将请求发给 TypeSafe（jev-latest 模型），经两阶段（分块 Choice + fits 判断）选出唯一适配技能，并在用户消息末尾追加一行提示。默认关闭，无命中不注入，所有失败路径仅记日志并返回 None。仅用 Python 标准库，需 TypeSafe API key，每次路由约 $0.001、0.6–1.2 秒；阈值在英文请求上标定，其他语言下分数偏低（西语约低 0.14）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 两阶段路由：分块 Choice 粗筛 + shortlist 精选，gate/fits/fits_margin 阈值均在代码中
- 失败安全：无 key、超时、传输错误等一律单行日志并返回 None，不影响对话轮
- 数据面明确：仅发送当轮请求文本与技能描述，不发送历史、文件、凭据
- 每决策一行日志，配合会话存储可对真实轮次评分

## 适用场景

- 技能数量多到模型读漏合适技能的 Hermes Agent 用户
- 在对话中希望自动获得该加载哪个技能的提示
- 通过日志与缓存离线重放并调优阈值

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: A Hermes Agent plugin that names **the one skill worth loading** — before the model call.
> L17: It is **opt-in** (`enabled: false` by default), injects **nothing** when nothing fits, and every

## 星数曲线

```mermaid
xychart-beta
    title "DECRUX9812/typesafe-skill-router 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a06e6c2346dd` · [字段定义](../../DATASET.md)*
