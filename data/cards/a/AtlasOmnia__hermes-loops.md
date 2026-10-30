# AtlasOmnia/hermes-loops

⭐ 31 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/AtlasOmnia/hermes-loops) · [官网](https://hermesagenttools.com/) · 组织维护

**面向 Hermes Agent 的自主循环工具集：自动实验与健康巡检**

AtlasOmnia Hermes Agent 工具集的一部分，提供三类可审查的自主 agent 循环：autoresearch 是 Karpathy 式 propose→test→keep/revert 仓库实验框架，由 agent 修改本地 Git 仓库、按评分保留或回退提交，且 provider/agent 无关；maintenance 含只读健康巡检（返回 healthy/warning/unavailable/unknown）与仅生成建议的改进评估循环，不写入 Hermes 安装；hermes-diagnostic-review 以技能形式提供 LLM 驱动的诊断回顾。两个代码包从各自目录以 pip 独立安装。

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

- autoresearch：agent 改仓库→测评分→保留/回退的本地 Git 实验循环，不推送远端
- maintenance：只读健康探针 + 建议式改进评估，不自动应用
- 诊断回顾以 hermes-custom-pack 技能形式提供，人工把关晋升
- provider 与 agent 无关的设计

## 适用场景

- 让 agent 在本地仓库自动迭代实验并保留有效改动
- 对 Hermes 安装做只读健康巡检
- 从重复会话结果中生成待人工审核的改进建议

## 场景标签

`编码 Agent` `LLM 可观测性` · 领域:编码与开发

## 证据(README 行号)

> L5: Autonomous agent loops for Hermes Agent: small,
> L11: |autoresearch|Karpathy-style propose→test→keep/revert harness for repository experiments|Yes — commits/reverts in a
> L25: and keeps good changes as local commits or reverts the rest. Provider- and agent-agnostic; never

## 星数曲线

```mermaid
xychart-beta
    title "AtlasOmnia/hermes-loops 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-28 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `134485ece284` · [字段定义](../../DATASET.md)*
