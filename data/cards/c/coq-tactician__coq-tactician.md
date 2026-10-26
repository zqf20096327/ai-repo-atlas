# coq-tactician/coq-tactician

⭐ 87 · OCaml · MIT · 推送 2026-10-19 · [GitHub](https://github.com/coq-tactician/coq-tactician) · [官网](https://coq-tactician.github.io) · 组织维护

**Coq 定理证明器的战术学习与证明合成插件**

Coq 证明助手的插件，通过机器学习从既有 tactic 脚本中学习，在用户交互证明过程中给出下一步 tactic 建议，或直接接手完成证明合成；用户仍保留对整体证明策略的控制。作为 Coq 插件支持 Coq 8.10 至 master 各版本，因 Coq 插件 API 不保证向后兼容，仓库为每个主要 Coq 版本维护独立分支（coq8.10…coqdev），并有每日 CI 对上游 Coq 编译各分支。安装与用法细节在手册中，README 未给出具体命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从既有 tactic 脚本学习并给出下一步建议
- 可整体接手证明合成（proof synthesis）
- 支持 Coq 8.10 至 master，按版本维护独立分支

## 适用场景

- 在 Coq 交互证明中获得下一步 tactic 建议
- 让插件自动完成部分证明合成
- 在多个 Coq 版本的开发项目中使用与基准测试

## 场景标签

 · 领域:形式化验证/定理证明

## 证据(README 行号)

> L5: Tactician is a tactic learner and prover for the Coq Proof Assistant. The system will help
> L7: To this end, Tactician will learn from previously written tactic scripts, and either gives

## 星数曲线

```mermaid
xychart-beta
    title "coq-tactician/coq-tactician 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 86 --> 88
    line [87, 87]
```

2026-10-18 87 → 2026-10-26 87（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `f352687eefaa` · [字段定义](../../DATASET.md)*
