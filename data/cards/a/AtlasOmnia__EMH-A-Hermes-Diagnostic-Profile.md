# AtlasOmnia/EMH-A-Hermes-Diagnostic-Profile

⭐ 48 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/AtlasOmnia/EMH-A-Hermes-Diagnostic-Profile) · [官网](https://hermesagenttools.com/) · 个人维护

**Hermes Agent 的诊断型配置档：诊断并安全修复 Agent 故障**

非官方的 Hermes Agent 配置档（profile）分发，包含 18 个诊断类技能，覆盖内存、Kanban、插件、网关、provider、会话、CLI/TUI/Desktop、更新与恢复等子系统的故障诊断、分诊、修复与文档化。采用只读优先的调查方式：变更配置、安装组件或外发数据前需用户逐项同意；证据分级标注（Observed/Reproduced/Hypothesis 等），安装版本与官方文档版本对比后才应用文档结论。通过 hermes profile install 命令以 git clone 的仓库目录安装，不捆绑任何 provider、模型或凭据。

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

- 18 个技能覆盖 Hermes Agent 各子系统的诊断与分诊
- 只读优先调查，任何变更/外发操作需逐项明确同意
- 证据分级标签与安装版本文档适用性校验
- 不捆绑 provider、模型、凭据或配置文件

## 适用场景

- Hermes Agent 出现内存、网关、插件等故障时进行诊断定位
- 对 Agent 安装版本与官方发布做只读对比分析
- 在一次性测试环境中安全试用诊断配置档

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L11: Its purpose is to diagnose, triage, safely repair, verify, and document Hermes Agent failures across profiles, memo
> L107: The distribution contains exactly eighteen class-level skills. Two untouched v0.1 skills remain at `0.1.0`; sixtee

## 星数曲线

```mermaid
xychart-beta
    title "AtlasOmnia/EMH-A-Hermes-Diagnostic-Profile 星数(近 3 点)"
    x-axis ["2026-10-28", "2026-10-29", "2026-10-30"]
    y-axis "stars" 46 --> 49
    line [47, 48, 48]
```

2026-10-28 47 → 2026-10-30 48（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `baa0ffb6144a` · [字段定义](../../DATASET.md)*
