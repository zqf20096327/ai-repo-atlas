# SJTU-DENG-Lab/LightningRL

⭐ 33 · Python · MIT · 推送 2026-04-25 · [GitHub](https://github.com/SJTU-DENG-Lab/LightningRL) · [官网](https://sjtu-deng-lab.github.io/LightningRL/) · 组织维护 · 中文 README

**用强化学习后训练突破分块 dLLM 速度-质量权衡的训练框架**

面向分块扩散大语言模型（block-wise dLLMs）的强化学习后训练框架：基于 GRPO 引入逐奖励解耦归一化、token 级 NLL 正则与 TPF 感知过滤三项修改，同时优化生成速度与质量。应用于 SDAR-8B 时报告在 GSM8K/MATH500/MBPP/HumanEval 等基准上的 TPF/AUP/准确率数字，README 称在单张 H100 上以 SGLang 部署时达到 336.03 TPS。安装采用 git clone 源码加 uv sync，训练与评测通过 scripts 脚本执行，模型路径需在 YAML 配置中以绝对路径指定。由上海交通大学团队以 ICML 论文配套代码形式发布。

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

- 对 GRPO 的三项修改：逐奖励解耦归一化、token 级 NLL 正则、TPF 感知过滤
- 提供 RL 训练脚本（train_rl.sh）与评测脚本（eval.sh）
- 数据集通过 download_data.py 按需下载（MATH500、MATH_train 等）
- 价值模型为可选组件，当前不参与训练

## 适用场景

- 对 SDAR 类分块 dLLM 做速度-质量联合优化的 RL 后训练
- 复现论文中数学与代码基准上的评测结果
- 研究多目标 RL 训练中奖励归一化与轨迹过滤方法

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L28: We propose **LightningRL**, a reinforcement learning framework that breaks the accuracy–parallelism trade-off of bl
> L39: We advocate a post-training approach for pre-trained block-wise dLLMs that directly optimizes the speed–quality fro

## 星数曲线

```mermaid
xychart-beta
    title "SJTU-DENG-Lab/LightningRL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2afac9eddd9f` · [字段定义](../../DATASET.md)*
