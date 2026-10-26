# yeliudev/nncore

⭐ 29 · Python · MIT · 推送 2026-07-09 · [GitHub](https://github.com/yeliudev/nncore) · [官网](https://nncore.readthedocs.io) · 个人维护

**面向科研的轻量机器学习工具库，覆盖训练全流程**

为机器学习与深度学习研究者提供的通用工具库：包含统一 I/O API、PyTorch 未收录的层与损失实现、分布式训练扩展方法、数据加载技术，以及可接管完整训练/测试流程的引擎（阶段控制、优化器配置、lr 调度、checkpoint 管理、指标与 tensorboard 写入均自动完成）。部分方法需 PyTorch 2.0+，但不强制安装 PyTorch。CI 覆盖 Ubuntu/macOS/Windows 下 Python 3.9-3.12，以 pip 包或源码方式安装。

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

- 接管训练/测试全流程的引擎，自动处理 checkpoint、调度与指标记录
- PyTorch 未收录的层与损失的高效实现
- 统一 I/O API 与分布式训练扩展方法
- 部分功能需 PyTorch 2.0+，但安装 PyTorch 非必需

## 适用场景

- 科研中快速搭建训练流程，减少工程性代码
- 复用通用层与损失实现补充 PyTorch 缺口
- 多平台（Ubuntu/macOS/Windows）下的可复现实验环境

## 场景标签

 · 领域:机器学习/深度学习

## 证据(README 行号)

> L5: NNCore is a library that provides common functionalities for Machine Learning and Deep Learning researchers. This pr
> L11: - An engine that can take over the whole training and testing process, with all the baby-sitting works (stage contr

## 星数曲线

```mermaid
xychart-beta
    title "yeliudev/nncore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a9189fd56f1a` · [字段定义](../../DATASET.md)*
