# openvang/vanguarstew

⭐ 21 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/openvang/vanguarstew) · [官网](https://openvang.github.io/vanguarstew/) · 组织维护

**仓库维护者智能体与基于 GitHub 历史的维护决策基准**

OpenVang 的维护者智能组件：给定冻结在某一时刻的仓库，agent 推断项目的维护哲学、读取 issue/PR/提交等现场信息，规划下一步维护动作（merge/拒绝/分诊/发版）并在需要时产出补丁；随后用真实 GitHub 历史做评分，包含客观锚点（merge/标签/版本号等硬事实）与成对裁判的主观层，输出 composite_mean 及各分项分解。面向 Bittensor subnet 工作流中的维护者角色，提供离线 dry-run、私有本地服务运行方式，评分路径使用验证者提供的推理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 四步维护者 agent：推断维护哲学→读取现场→规划决策→按需产出补丁
- 基于真实 GitHub 历史的 replay 基准，客观锚点+成对裁判双层评分
- composite_mean 分解为 judge/objective/foresight 各自独立可核验的分项
- 离线确定性 stub LLM dry-run 与私有 restart-safe 运行时

## 适用场景

- 评估 agent 能否做出与真实维护者一致的仓库决策
- 在 Bittensor subnet 中作为维护者专家组件运行
- 本地私有地对仓库做维护决策回放评测

## 场景标签

`模型评测` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L8: `vanguarstew` is OpenVang's maintainer-intelligence component: a repository-maintainer agent,
> L61: The maintainer agent lives in `agent/`. Given a repository frozen at a moment in time,
> L141: **Active development.** The current foundation includes history-derived replay, objective and

## 星数曲线

```mermaid
xychart-beta
    title "openvang/vanguarstew 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `76e0d71d70fe` · [字段定义](../../DATASET.md)*
