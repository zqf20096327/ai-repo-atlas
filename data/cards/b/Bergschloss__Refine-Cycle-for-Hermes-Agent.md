# Bergschloss/Refine-Cycle-for-Hermes-Agent

⭐ 42 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/Bergschloss/Refine-Cycle-for-Hermes-Agent) · 个人维护

**Hermes Agent 自我改进插件：跨会话识别重复错误并写入最小修正**

面向 Hermes Agent 的插件：会话结束后读取自身轨迹中的错误并指纹化，仅在错误跨会话重复出现时触发，由模型提出一处最小编辑（新增记忆/创建或修补技能），经大小、注入与重复检查后写入日志再应用，并在后续会话中核验效果。每日最多三次修改、最多 30 次模型调用，支持一键回滚，不重写基础指令、不过滤对话。提供 Telegram 通知与桌面状态栏入口。兼容 Hermes 0.19–0.21.x，需运行安装脚本并调整主机内存上限与审批队列配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 错误指纹化，跨会话统计重复后才触发编辑
- 最小编辑（记忆/技能）经安全检查后写入日志再应用，支持回滚
- 每日变更与模型调用次数受限，异常时停止而非假装成功
- 后续会话核验教训效果（working/unused/unreliable/too early）

## 适用场景

- 让我的 Hermes Agent 不再跨会话重复同样的失败命令或错误假设
- 自动沉淀小教训并事后核验是否生效
- 对 agent 的自我修改保留日志与一键回滚控制

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: Refine Cycle — a self-improvement plugin for Hermes Agent
> L19: It adapts the `/refine` concept from
> L85: hermes plugins install Bergschloss/Refine-Cycle-for-Hermes-Agent

## 星数曲线

```mermaid
xychart-beta
    title "Bergschloss/Refine-Cycle-for-Hermes-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-30 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5d10564166e5` · [字段定义](../../DATASET.md)*
