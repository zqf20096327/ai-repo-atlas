# DECRUX9812/hermes-loopguard

⭐ 5 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/DECRUX9812/hermes-loopguard) · [官网](https://github.com/DECRUX9812/hermes-loopguard#readme) · 个人维护

**Hermes Agent 插件：为 cron/kanban 自动化拦截无效模型调用以节省 token**

以 Hermes Agent 插件形式提供的自动化门控层：在 cron 与 kanban 任务唤醒代理之前先做判定——状态未变化时输出 {"wakeAgent": false} 使 Hermes 不构建 prompt、不调用 LLM（零 token 变更门）；语义门可路由到 TypeSafe Jev 或任意 OpenAI 兼容端点等廉价后端，本地启发式为兜底；另含 computer-use 门控与工具门（可拦截或转交人工审批，但不自动放行）。仅支持安装到 hermes 命令所在 Python 环境，editable 安装才能被插件加载器识别。未上架 PyPI，需从 GitHub 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零 token 变更门：未变化轮询不触发任何模型调用
- 四级语义后端链：TypeSafe → OpenAI 兼容 → Hermes 辅助任务 → 本地正则启发式
- computer-use 基准：廉价模型链相对大模型循环每轮成本为其 6.4%
- 失败策略 fail-open（wake）/skip 可选，无遥测上报

## 适用场景

- 让定时轮询任务在无新内容时不唤醒 agent、不烧 token
- 用廉价模型对例行分诊问题做前置判定，仅复杂项升级到大模型
- 为自动化中的 shell 命令加一道分类与人工审批门

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L6: A Hermes Agent plugin (plugin id **`loopguard`**).
> L14: LoopGuard puts those decisions on a cheap, typed path before the agent wakes.
> L126: LoopGuard evaluates gate questions using a fast, cheap backend. `backend: auto` evaluates


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `cc19f26cacc9` · [字段定义](../../DATASET.md)*
