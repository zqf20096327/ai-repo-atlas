# yash-jha-888/aurelius

⭐ 13 · C++ · MIT · 推送 2026-08-26 · [GitHub](https://github.com/yash-jha-888/aurelius) · 个人维护

**从零用现代 C++ 实现的深度学习框架**

个人开发者以理解 PyTorch 等库内部机制为动机、从数学到工程手工实现的 C++ 深度学习框架。各子系统（激活函数、初始化器、优化器、调度器、损失、全连接层、训练循环、日志）设计为可独立扩展的抽象接口，支持 SGD/Adam、Dropout、L2 正则、早停与检查点恢复，附 MNIST IDX 解析器与训练指标 CSV/JSON 记录及 Python 可视化脚本。当前为全连接网络，自动微分、卷积层、CUDA 后端等仍在 Roadmap 未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 激活/初始化/优化器/调度器等子系统均为可插拔抽象接口
- 支持 SGD/Adam、四种学习率调度器、Dropout 与 L2 正则、早停与最佳模型恢复
- IDX 格式 MNIST 解析与官方 60k/10k 划分
- 时间戳实验日志、CSV 指标与 JSON 配置 sidecar，Python 脚本生成可视化

## 适用场景

- 学习深度学习框架底层实现原理
- 在 C++ 环境中训练小型全连接网络（如 MNIST）
- 作为可扩展骨架实现自定义优化器或初始化策略

## 场景标签

`模型训练` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: Aurelius is a deep learning framework written in modern C++ from first principles.
> L11: Each major subsystem, including activations, weight initialization, loss functions, logging, and optimization, is d

## 星数曲线

```mermaid
xychart-beta
    title "yash-jha-888/aurelius 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `a1beecc5ad45` · [字段定义](../../DATASET.md)*
