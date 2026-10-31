# Sanexxxx777/curated-claude-code

⭐ 16 · MIT · 推送 2026-09-07 · [GitHub](https://github.com/Sanexxxx777/curated-claude-code) · [官网](https://shulgin.is-a.dev) · 个人维护

**Claude Code 的精选技能与安全护栏自进化工具集**

面向 Claude Code 用户的策展工具集（harness）：10 个技能（如工具准入评估 vet、证据分级 proof、目标循环 goal、安全发布审计 ship-secure）、2 个 agent、5 组行为规则，拷贝到 ~/.claude/ 即可用。核心机制是自我改进循环——用户纠正转为记忆、发现沉淀为技能，新工具经 /vet 门控（安全为阻断步骤）才准入，并有 promotion gate 与 system-health 卫生扫描。明确不做大杂烩合集，无自动 hook，安装为手动 git clone 复制。

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

- 10 个技能 + 2 个 agent + 5 组行为规则的策展组合
- /vet 工具准入流水线，安全检查为阻断性步骤
- 自我改进循环：纠正→记忆→技能，经 promotion gate 验证
- 无自动 hook，所有变更需确认

## 适用场景

- 评估是否引入某个新工具、技能或 MCP
- 让 Claude Code 配置随使用积累而改进且不膨胀
- 发布 web 应用前做安全审计与推送前检查

## 场景标签

`提示工程` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3:  A small, vetted, self-evolving harness for Claude Code — curated, not dumped.
> L20: - ✅ A curated set of executable skills + always-on principles you can drop into `~/.claude/`.

## 星数曲线

```mermaid
xychart-beta
    title "Sanexxxx777/curated-claude-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f3f9c3be7095` · [字段定义](../../DATASET.md)*
