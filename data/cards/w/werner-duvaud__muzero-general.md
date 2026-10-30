# werner-duvaud/muzero-general

⭐ 2,877 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/werner-duvaud/muzero-general) · [官网](https://github.com/werner-duvaud/muzero-general/wiki/MuZero-Documentation) · 组织维护

**面向教学的 MuZero 通用实现：在自定义环境中训练规划智能体**

基于 DeepMind 2019 年 MuZero 论文与原始伪代码的带注释 PyTorch 实现，支持全连接与残差网络、并行自我博弈、优先级回放、重分析，以及单人/双人回合制离散动作游戏。接入新环境只需添加含配置和 Game 适配器的游戏文件（如 CartPole）。提供命令行与 Python API 训练、评估、TensorBoard 监控、断点续训，附 CartPole/Lunar Lander/Breakout 打包检查点，Python 3.12+、MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于原始论文与伪代码的带注释 PyTorch 实现
- 支持并行自我博弈、优先级回放、重分析与残差网络
- 通过 Game 适配器接入自定义环境（CartPole 示例）
- 打包 CartPole/Lunar Lander/Breakout 训练检查点与续训功能

## 适用场景

- 学习 MuZero 算法的结构与实现细节
- 在自定义 Gymnasium 式环境中训练规划智能体
- 复现并评估 CartPole/Lunar Lander/Breakout 训练结果

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L6: An educational and commented implementation of MuZero, based on DeepMind's 2019 paper and original pseudocode, built
> L8: MuZero builds on AlphaZero by learning the dynamics used for planning from experience. Its network represents observ


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `39dac11335f2` · [字段定义](../../DATASET.md)*
