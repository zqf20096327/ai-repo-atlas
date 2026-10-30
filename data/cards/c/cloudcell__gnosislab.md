# cloudcell/gnosislab

⭐ 21 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/cloudcell/gnosislab) · [官网](https://loop.cloudcell.workers.dev/docs) · 个人维护

**面向 AI agent 的科学方法运行时：假设、实验、证据、结论全程可审计**

以五个 MCP 服务（Episteme 实验记录、Anamnesis 证据图、Zetesis 检索调查、Arete 改进比较、Agora 协调观测）构成的基础设施，把 hypothesis→experiment→evidence→conclusion 的科研流程转为显式软件对象，各服务独立持久化状态并暴露本地观测 GUI。支持 MCP 客户端接入、daemon 驱动 CLI agent 并以独立 checker 裁决回合、bubblewrap/strace 密封试验执行（仅 Linux，其他平台需显式关闭沙箱）。Python 3.10+，PyPI 或源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五个 MCP 服务按科研职责分离，状态独立持久化
- daemon 驱动 agent 并以独立 checker 验证完成（不信任 agent 自称完成）
- bubblewrap/strace 密封试验执行，非 Linux 平台默认 fail closed
- gnosislab init 一键生成隔离实验工作区

## 适用场景

- 让自主研究 agent 的实验过程可被人审查与复现
- 机器学习实验管理与证据溯源
- 构建需要可审计结论的研究或评测系统

## 场景标签

`科研工具` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L35: Instead of leaving an agent's reasoning, experiments, and evidence scattered across prompts, shell history, noteboo
> L145: GnosisLab is composed of five MCP services.
> L234: This means an MCP-capable agent or client can work with the scientific process as a set of tools rather than requi

## 星数曲线

```mermaid
xychart-beta
    title "cloudcell/gnosislab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3dd8817e3ea3` · [字段定义](../../DATASET.md)*
