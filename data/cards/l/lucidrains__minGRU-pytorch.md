# lucidrains/minGRU-pytorch

⭐ 327 · Python · MIT · 推送 2025-12-10 · [GitHub](https://github.com/lucidrains/minGRU-pytorch) · 个人维护

**论文 minGRU 的 PyTorch 实现（log-space 数值稳定版）**

实现论文《Were RNNs All We Needed?》提出的 minGRU 循环网络单元，仅包含 log-space 数值稳定版本，附带 minLSTM 贡献。以 PyTorch 库形式提供，pip 安装后导入 minGRU_pytorch 使用，README 含用法示例与 sanity check 代码，另提供 enwik8 数据集上的训练测试脚本 train.py。引用 Yannic 的论文评述视频，并附 minGRU 与 Hymba 论文的 BibTeX 引用。面向复现与实验该架构的研究者和开发者。

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

- minGRU 的 log-space 数值稳定实现
- 含 minLSTM 贡献
- 提供用法示例与 sanity check 代码
- enwik8 数据集训练测试脚本

## 适用场景

- 复现或实验 minGRU 架构
- 在序列建模任务中替换传统 GRU 进行对比实验
- 研究 RNN 类架构的数值稳定训练

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: Implementation of the proposed minGRU in Pytorch, only the log-space numerically stable version.
> L47:     title   = {Were RNNs All We Needed?},

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/minGRU-pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 326 --> 328
    line [327, 327]
```

2026-10-18 327 → 2026-10-25 327（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `51a865ce15fe` · [字段定义](../../DATASET.md)*
