# eric-m-cardozo/TorchSystem

⭐ 21 · Python · Apache-2.0 · 推送 2026-08-02 · [GitHub](https://github.com/eric-m-cardozo/TorchSystem) · [官网](https://eric-m-cardozo.github.io/TorchSystem/) · 个人维护

**面向 PyTorch 的 DDD/事件驱动训练系统框架**

基于 PyTorch 的 Python 框架，按领域驱动设计（DDD）原则组织训练代码：用 Aggregate 聚合神经网络、损失函数、优化器与指标；用无状态 Service 编排训练与评估；通过事件与 Producer/Consumer 解耦日志、指标与检查点等副作用；内置依赖注入（Provider/Depends）、Pub/Sub 工具、模型注册表（哈希标识）与 Compiler 构建管线（设备迁移、权重恢复、可选 torch.compile）。面向需要构建模块化、可测试训练系统的深度学习开发者，纯 Python 实现，pip 安装，无基础设施要求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Aggregate 聚合模型组件，封装数据与行为
- 无状态 Service + 领域事件解耦训练编排与副作用
- 内置依赖注入系统（Provider/Depends）
- Compiler 构建管线：设备迁移、检查点恢复、可选 torch.compile

## 适用场景

- 构建模块化、可测试的 PyTorch 训练系统
- 通过事件解耦训练中的日志、指标与检查点逻辑
- 用依赖注入在训练、评估等上下文中切换实现

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: This framework will help you to create powerful and scalable systems using the PyTorch library. It is designed under
> L19: While aggregates are in charge of data, in order to perform actions, we need to define services. Services are state
> L92: Let's now train our aggregate. The training process involves orchestrating data, batching, and optimization steps, 

## 星数曲线

```mermaid
xychart-beta
    title "eric-m-cardozo/TorchSystem 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `cc0f0f5ffc0e` · [字段定义](../../DATASET.md)*
