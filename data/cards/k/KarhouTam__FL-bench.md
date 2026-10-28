# KarhouTam/FL-bench

⭐ 692 · Python · GPL-3.0 · 推送 2026-10-20 · [GitHub](https://github.com/KarhouTam/FL-bench) · 个人维护 · 中文 README

**联邦学习方法基准测试框架：统一复现 40+ 种 FL 算法**

面向联邦学习研究者的 PyTorch 基准框架：收录 40 余种传统、个性化、域泛化与差分隐私 FL 方法，统一继承 FedAvgServer/FedAvgClient 工作流，通过 generate_data.py 按 Dirichlet 等策略划分数据集，main.py 加 yaml 配置或 CLI 运行实验。支持 Ray 并行训练、visdom/tensorboard 监控，内置 Torchvision 常用模型与 16 种图像/医疗数据集；可继承现有方法类实现自定义算法。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 收录 40+ 种 FL 方法（传统/个性化/域泛化/差分隐私），每条注明论文出处
- Ray 并行模式训练（num_workers 可配置）
- 支持 16 种数据集与多种划分策略生成联邦数据
- 方法类继承式扩展：可从 FedAvg 或高级方法派生自定义算法

## 适用场景

- 统一环境下对比多种联邦学习算法的实验表现
- 复现论文中的 FL 方法并调整超参数
- 快速实现和评测自定义联邦学习算法
- 研究非 IID 数据划分下的模型表现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Benchmarking Federated Learning Methods.
> L84: ALL classes of methods are inherited from `FedAvgServer` and `FedAvgClient`. If you wanna figure out the entire wor
> L170: ## Parallel Training via `Ray` 🚀

## 星数曲线

```mermaid
xychart-beta
    title "KarhouTam/FL-bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 693 --> 695
    line [694, 694]
```

2026-10-18 694 → 2026-10-28 694（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `a54ad545a80a` · [字段定义](../../DATASET.md)*
