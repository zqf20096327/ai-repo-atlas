# asterinas/KVerus

⭐ 27 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/asterinas/KVerus) · 组织维护

**将 Rust 代码迁移并形式化验证为 Verus 的 agent 技能工作流**

基于 agent 技能（skills）的工作流：把 Rust 代码迁移到 Verus，生成规范与证明、修复验证失败、评估证明质量并审计可执行语义，可用 kverus-run 跑端到端流水线或单独调用各阶段技能。技能可安装到任意目标项目中，配合 Codex 或 Claude Code 使用；依赖 Verus 命令行工具，Python 环境用 uv 管理。已在 Asterinas 系统验证项目 VOSTD 中使用，附论文（ASE 2026）。

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

- 流水线覆盖迁移、规范生成、证明修复、质量评估与审计
- kverus-run 端到端入口，也支持单独调用各技能
- 技能安装脚本支持 Codex 与 Claude Code 目标、copy/symlink 模式
- 在 Asterinas VOSTD 项目中有实际验证案例（含 RwMutex 验证与 1,075 行冗余证明精简）

## 适用场景

- 把现有 Rust 代码迁移到 Verus 并补齐形式化证明
- 修复 Verus 验证失败并精简冗余证明代码
- 对 Rust 实现做形式化验证审计

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: KVerus is a skill-based workflow for migrating Rust code to formally verified Verus, adding specifications and proof
> L30: KVerus ships a set of agent skills (under `skills/`) that can be installed into any target project for use with Cod

## 星数曲线

```mermaid
xychart-beta
    title "asterinas/KVerus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fb5aecd2390d` · [字段定义](../../DATASET.md)*
