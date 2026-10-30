# anormang1992/vre

⭐ 15 · Python · Apache-2.0 · 推送 2026-06-18 · [GitHub](https://github.com/anormang1992/vre) · 个人维护

**Python 库：用知识图谱对 AI agent 的行动做认知边界拦截**

面向自主 agent 开发者的 Python 库（VRE 类与 vre_guard 装饰器）：在受保护工具执行前，检查所涉概念是否在-authored 知识图谱中达到所需深度（D0 存在到 D4+ 推论的五级分层，深度由边结构决定并可加 min_depth 下限）；未满足则阻断并以四类结构化 Gap 对象（存在/深度/关系/可达性）呈现缺口。默认 SQLite 后端开箱即用，可选 Neo4j。自述非权限系统、非沙箱、非幻觉过滤器，仅强制与已建模领域一致。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 行动前按知识图谱深度（D0-D4+，单调）校验概念 grounding，未达标即阻断
- 阻断时返回四类结构化 Gap 对象而非通用错误
- 约束由图结构自身承载（边上的深度与策略），SQLite 默认后端零外部服务
- 支持 agent_key 稳定身份（~/.vre/agents.json）与 JSONL trace

## 适用场景

- 为自主 agent 的危险操作（删文件、执行命令）加认知前置校验
- 把 agent 的未知领域显式化为结构化 Gap，供上报或人工介入
- 在自建知识图谱上做可审计的行动许可策略

## 场景标签

`Agent 框架` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L18: VRE is a Python library that gives an autonomous agent an explicit, inspectable
> L20: guarded tool executes, VRE checks that the concepts the action touches are
> L67: VRE addresses this directly. It imposes a contract: before an action executes, the agent must demonstrate that the

## 星数曲线

```mermaid
xychart-beta
    title "anormang1992/vre 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `cf24f9443dc7` · [字段定义](../../DATASET.md)*
