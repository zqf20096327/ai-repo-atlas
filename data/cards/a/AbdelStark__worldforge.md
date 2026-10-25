# AbdelStark/worldforge

⭐ 108 · Python · MIT · 推送 2026-09-19 · [GitHub](https://github.com/AbdelStark/worldforge) · [官网](https://abdelstark.github.io/worldforge/) · 个人维护 · 中文 README

**面向机器人学的世界模型规划工作流编排与评测框架**

Python 编写的物理 AI 世界模型规划集成层：以行动条件预测世界模型为核心循环，组合 policy、score、predict、embed 等能力适配器，用 LatentMPCController（CEM、滚动时域）对候选动作排序选优。适配器覆盖 mock、LeWorldModel、LeRobot、GR00T、Cosmos-Policy、JEPA 等；凭据、检查点、CUDA 与机器人控制均由宿主自持。提供 eval/benchmark CLI 与预算门禁。版本 0.5.0，pre-1.0 beta，公共 API 可能变动。仅支持 Python 3.13。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- plan→predict/score→选优→执行的潜空间 MPC 规划循环（CEM、滚动时域）
- 按能力契约注册的 provider 体系（mock/leworldmodel/lerobot/gr00t/cosmos-policy/jepa/genie）
- eval 与 benchmark CLI，可将成功率/延迟/吞吐阈值转为非零门禁
- mock provider 无需凭据、GPU、检查点即可运行

## 适用场景

- 机器人为任务选型比较世界模型 provider 与配置组合
- 组合策略模型与评分模型做仿真/回放规划验证
- 对规划循环做可复现的评测与基准测试

## 场景标签

`模型评测` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L13: WorldForge is the application builder's counterpart to model-training stacks like Stable World
> L14: Model. Those stacks *train* world models. WorldForge helps roboticists *compose, evaluate, and
> L230: |An integration layer for provider-backed planning loops|A hosted service, model API, or training framework|

## 星数曲线

```mermaid
xychart-beta
    title "AbdelStark/worldforge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-25 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1930ffd7ea9d` · [字段定义](../../DATASET.md)*
