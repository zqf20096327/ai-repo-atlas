# google-deepmind/dm_env

⭐ 411 · Python · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/google-deepmind/dm_env) · 组织维护

**给 RL 环境实现者的 Python 环境接口规范**

DeepMind 发布的 Python 强化学习环境接口包：定义 Environment 抽象基类、表示每步转移输出的 TimeStep 容器、描述动作/观测/奖励/折扣格式的 specs 模块，以及验证具体环境实现是否符合接口的 test_utils 测试工具。示例目录含用该接口实现的 RL 环境。从 PyPI 或 GitHub 仓库以 pip 安装，1.6 版本起仅支持 Python 3.7+。

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

- dm_env.Environment 抽象基类统一 RL 环境接口
- specs 模块描述动作、观测、奖励、折扣的数据格式
- test_utils 工具检验环境实现是否符合接口
- 提供示例 RL 环境实现与 API 文档

## 适用场景

- 为自研 RL 环境实现统一的 Python 接口
- 用 test_utils 校验环境实现是否符合规范
- 在 RL 训练框架中以 dm_env 接口对接多种环境

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L6: This package describes an interface for Python reinforcement learning (RL)
> L9: * `dm_env.Environment`: An abstract base class for RL environments.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `df00e5391601` · [字段定义](../../DATASET.md)*
