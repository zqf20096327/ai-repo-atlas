# kisonho/torchmanager

⭐ 14 · Python · BSD-2-Clause · 推送 2026-10-26 · [GitHub](https://github.com/kisonho/torchmanager) · 个人维护

**PyTorch 通用深度学习训练/测试框架**

面向使用 PyTorch 的开发者提供通用训练与测试循环：核心 Manager 类接收模型、优化器、损失函数与指标，通过 fit/test 方法完成训练测试，支持多损失字典组合与权重控制、自动设备选择（CUDA/MPS 优先）、多 GPU 训练、TensorBoard/Checkpoint 回调与实验信息保存。可继承各类 Manager 覆写 train_step/test_step 定制算法，Configs 类从终端参数读取配置，训练后的模型可用 torch.save 单独保存并在框架外加载。以 pip/conda 包形式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Manager 类提供通用训练/测试管线，支持继承覆写 train_step/test_step 定制
- 自动识别 CUDA/MPS 设备并支持多 GPU 训练
- 多损失组合（字典传参）与权重系数平衡
- Experiment 回调整合 TensorBoard 记录与 Last/Best Checkpoint

## 适用场景

- 为自己的 PyTorch 模型快速搭建训练与测试流程
- 通过继承定制训练/测试算法并保留通用管线
- 统一管理实验日志与模型检查点

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L2: ### A generic deep learning training/testing framework for PyTorch

## 星数曲线

```mermaid
xychart-beta
    title "kisonho/torchmanager 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `71b1fd682f03` · [字段定义](../../DATASET.md)*
