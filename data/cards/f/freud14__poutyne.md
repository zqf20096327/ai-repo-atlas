# freud14/poutyne

⭐ 579 · Python · LGPL-3.0 · 推送 2026-06-07 · [GitHub](https://github.com/freud14/poutyne) · [官网](https://poutyne.org/) · 组织维护

**PyTorch 简化训练框架：省去训练神经网络的样板代码**

Poutyne 是基于 PyTorch 的深度学习训练框架，定位与 Keras 类似：用户照常定义 PyTorch 模块，训练时交给 Poutyne 的 Model 处理训练循环、统计与回调。提供回调机制（保存最优模型、早停、日志）、ModelBundle 自动检查点与日志、evaluate/predict 方法。要求环境预先安装最新版 PyTorch，支持 Python >= 3.10。以 pip/uv 安装，另提供 Docker 镜像；附教程 notebook、Google Colab 示例与 Université Laval 的演讲材料。LGPLv3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Model 封装 PyTorch 训练循环、统计与回调
- 回调机制支持最优模型保存、早停、日志
- ModelBundle 提供自动检查点与日志
- 提供 pip/uv 安装与 Docker 镜像

## 适用场景

- 用 PyTorch 训练神经网络时省去样板训练代码
- 通过回调做检查点保存、早停与训练日志
- 跟随 notebook 示例学习分类、回归、迁移学习等任务

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L13: Poutyne is a simplified framework for PyTorch and handles much of the boilerplating code needed to train neural net
> L39: How Poutyne works is that you create your PyTorch module (neural network) as usual but when comes the time to train

## 星数曲线

```mermaid
xychart-beta
    title "freud14/poutyne 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 578 --> 580
    line [579, 579]
```

2026-10-18 579 → 2026-10-22 579（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `470424671225` · [字段定义](../../DATASET.md)*
