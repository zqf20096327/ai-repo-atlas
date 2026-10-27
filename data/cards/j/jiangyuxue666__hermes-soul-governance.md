# jiangyuxue666/hermes-soul-governance

⭐ 24 · Python · 推送 2026-05-15 · [GitHub](https://github.com/jiangyuxue666/hermes-soul-governance) · 个人维护 · 中文 README

**Hermes Agent 的治理框架：替代原生记忆压缩并维护技能**

面向 Hermes Agent 用户的 SOUL.md 治理框架：用只读的 SOUL.md（无写入函数、无字数限制、置顶注入）替代原生 MEMORY.md/USER.md 的自动压缩循环，改为分类文件持久化（user-memory/ 按偏好、档案、环境、工作流分文件）；同时提供技能维护脚本 maintain.py，执行孤儿扫描、注册表同步、校验与 5 轴启发式合并检测五阶段流程。要求已安装 Hermes Agent，Python 3.8+，依赖其 venv 解释器。规则遵循依赖模型的指令遵循能力，合并检测为启发式可能误报。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SOUL.md 无写入函数，作为跨会话只读治理锚点
- 关键词到文件的记忆写入协议，分类文件持久化替代压缩
- maintain.py 五阶段技能维护：孤儿迁移、注册表同步、校验、合并检测、快照
- capability_finder.py 触发词评分实现技能调度

## 适用场景

- 替代 Hermes Agent 原生记忆压缩，避免上下文静默丢失
- 为 agent 自动创建的技能做注册、校验与清理
- 按触发词将用户请求路由到已注册技能

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L33: This framework is designed for **Hermes Agent**. You must have Hermes Agent installed and working before using this
> L81: - Disabling the default memory system and replacing it with file-based, categorized persistence

## 星数曲线

```mermaid
xychart-beta
    title "jiangyuxue666/hermes-soul-governance 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `47f488f6351f` · [字段定义](../../DATASET.md)*
