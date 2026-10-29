# ADA-research/VERONA

⭐ 52 · Python · Apache-2.0 · 推送 2026-07-28 · [GitHub](https://github.com/ADA-research/VERONA) · [官网](https://ada-research.github.io/VERONA/) · 组织维护

**神经网络局部鲁棒性验证实验框架**

Python 包，用于搭建神经网络局部鲁棒性验证实验流程：以一个脚本对多种网络、图像与扰动幅度（epsilon）组合运行完整实验，可计算鲁棒性分布、用对抗攻击实证测量鲁棒性，并通过外部 auto-verify 包调用 AB-CROWN 等形式化验证工具。默认安装为 CPU 版本，GPU 版本需显式安装；可选集成 AutoAttack 对抗攻击包。在 MNIST、GTRSB、CIFAR-10 数据集上测试过，并提供教程 notebook 与示例脚本。由跨机构研究团队（莱顿大学、代尔夫特理工、亚琛工业大学）维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单脚本运行多网络/多图像/多 epsilon 的完整验证实验
- 计算鲁棒性分布（Robustness Distributions）
- 通过 auto-verify 集成 AB-CROWN、nnenum、VeriNet、Oval-Bab 验证器
- 支持 SLURM 多节点分布式作业（CPU/GPU 分配）

## 适用场景

- 跑神经网络局部鲁棒性验证实验并生成鲁棒性分布
- 用对抗攻击实证测量网络鲁棒性
- 复现和扩展 ADA 研究组的验证研究论文结果

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L12: VERONA simplifies your experiment pipeline for performing local robustness verification on your networks and datase
> L16: Example use cases of the VERONA package include creating robustness distributions Bosman, Berger, Hoos and van Rijn

## 星数曲线

```mermaid
xychart-beta
    title "ADA-research/VERONA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-29 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d6dca3712fc3` · [字段定义](../../DATASET.md)*
