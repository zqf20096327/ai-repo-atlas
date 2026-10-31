# lucidrains/survival-rl

⭐ 15 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/lucidrains/survival-rl) · 个人维护

**生存分析用于强化学习的探索库：预测事件到达时间并提取策略**

基于 PyTorch 的研究库，实现 Tiofack 等人提出的 Survival RL 思路：HazardCritic 接收状态、动作与事件批次，按时间分箱预测事件首次到达，采用最大似然训练并处理右删失（未观测到事件）；训练后可从 critic 提取趋向或避开事件（negate=True）的策略，支持多 critic 悲观最小化、竞争性 softmax 变体、驻留时间课程（EMA 跟踪与特征化）。面向强化学习研究者，pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HazardCritic 按时间分箱预测事件到达，支持右删失处理
- PolicyExtractor 从多个 critic 提取趋向/避开事件的策略
- HazardCriticCompetitive softmax 竞争变体
- DwellCurriculum 用 EMA 跟踪并特征化事件驻留时间

## 适用场景

- 训练预测事件到达时间分箱的 critic 并处理删失数据
- 从已训练 critic 提取趋向或避开某事件的策略
- 用驻留课程引导事件学习进度

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L5: Explorations into an application of survival analysis to RL, proposed by Tiofack et al. of Inria earlier this year
> L15: `HazardCritic` takes a batch of states, actions and events, and predicts the time bin in which the event is first r

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/survival-rl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0b197390e452` · [字段定义](../../DATASET.md)*
