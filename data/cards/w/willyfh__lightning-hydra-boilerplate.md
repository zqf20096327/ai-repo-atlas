# willyfh/lightning-hydra-boilerplate

⭐ 10 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/willyfh/lightning-hydra-boilerplate) · 个人维护

**面向深度学习科研的项目模板：管理配置、训练、评估与调参**

基于 PyTorch Lightning 与 Hydra 的深度学习实验项目模板，通过 GitHub 模板方式启动新项目。内置 Hydra YAML 配置管理、TensorBoard 日志、Optuna 超参搜索、早停与检查点回调，以及预配置的训练、评估、预测脚本和结构化输出目录。依赖用 Poetry 管理，附 pre-commit 钩子与自动化测试设置。面向需要快速搭建可复现实验流程的深度学习研究者。

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

- Hydra YAML 配置管理，支持命令行覆盖实验设置
- Optuna 超参数自动搜索，结果按 trial 存档
- 预配置训练/评估/预测脚本与结构化 outputs 目录
- Poetry 依赖管理，含 pre-commit 钩子与自动化测试

## 适用场景

- 快速搭建一个新的深度学习实验项目骨架
- 用 Hydra 管理多组实验配置并做命令行覆盖
- 用 Optuna 自动搜索模型超参数并留存结果

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: A project boilerplate for deep learning experiments using PyTorch Lightning and Hydra, designed for rapid prototypin
> L15: |📝 **Configurable Setup**|Model, dataset, and training configuration using `Hydra`.|

## 星数曲线

```mermaid
xychart-beta
    title "willyfh/lightning-hydra-boilerplate 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-24 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `9cc0c1297e8f` · [字段定义](../../DATASET.md)*
