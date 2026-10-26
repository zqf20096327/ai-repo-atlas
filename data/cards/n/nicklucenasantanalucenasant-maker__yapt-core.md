# nicklucenasantanalucenasant-maker/yapt-core

⭐ 53 · HTML · 推送 2026-10-25 · [GitHub](https://github.com/nicklucenasantanalucenasant-maker/yapt-core) · 组织维护 · 中文 README

**模块化 PyTorch 训练框架：为研究者与团队提供可组合训练循环**

基于 PyTorch 的训练框架，面向研究生、独立研究者和工程团队：将训练循环各阶段（前向、反向、优化器步进、日志等）实现为可覆写的钩子，配套第一方回调库（早停、梯度裁剪、EMA、混合精度等）、带严格 schema 校验的 YAML 配置、完整状态断点恢复（RNG/优化器/采样器位置）、确定性开关与插件发现机制。附响应式仪表盘与多语言界面（含中文）。README 未给出具体安装命令；性能开销声明为 0.3%-1.1%。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 训练循环各阶段全部钩子化，回调可组合与自定义
- Hydra 风格 YAML 配置带严格 schema 校验
- 断点恢复完整运行状态（RNG、优化器动量、采样器位置、指标历史）
- 7 种语言界面（含中文）与响应式实时监控仪表盘

## 适用场景

- 不再每个项目重写训练脚本，用统一框架管理深度学习训练
- 需要可复现实验（确定性种子、配置随运行记录）的科研工作流
- 从平板或手机远程监控训练运行的损失曲线与梯度直方图

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L24: **YAPT-Redux** is the spiritual successor to the classic *"Yet Another PyTorch Trainer"* pattern — but it refuses t
> L26: Where most trainers hand you a monolithic `train.py` and wish you luck, YAPT-Redux hands you a **composable score**
> L45: It is not a framework that hides PyTorch. It is a framework that *amplifies* PyTorch. You still write your `nn.Modu

## 星数曲线

```mermaid
xychart-beta
    title "nicklucenasantanalucenasant-maker/yapt-core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-26 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7019d252d056` · [字段定义](../../DATASET.md)*
