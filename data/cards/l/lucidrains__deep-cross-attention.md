# lucidrains/deep-cross-attention

⭐ 107 · Python · MIT · 推送 2026-04-03 · [GitHub](https://github.com/lucidrains/deep-cross-attention) · 个人维护

**DeepCrossAttention 注意力机制的 PyTorch 实现，供研究者使用**

Heddes 等人在 Google Research 提出的 DeepCrossAttention（DCA）的 PyTorch 实现：允许 queries、keys、values 从过去不同层路由，作为对 value residual learning 的泛化。提供 DCAGPT 模型类，通过 pip 安装为 Python 库；另附示例训练流程（pip install .[examples] 后运行 train.py）。README 引用 2025 年论文，作者同时说明其在探索该思路与 Hyper Connections 的关系。

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

- 实现 DeepCrossAttention：QKV 可从过去不同层路由
- 提供 DCAGPT 模型与使用示例
- 附示例训练脚本（train.py）与论文引用

## 适用场景

- 研究 Transformer 残差连接改进机制
- 在自有实验中替换标准注意力进行对比
- 复现 DeepCrossAttention 论文思路

## 场景标签

 · 领域:深度学习/模型架构

## 证据(README 行号)

> L5: Implementation of the proposed DeepCrossAttention by Mike Heddes while at Google research, in Pytorch
> L7: My analysis is although I still prefer Hyper Connections, they have an important idea here that I have been trying c

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/deep-cross-attention 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 106 --> 108
    line [107, 107]
```

2026-10-18 107 → 2026-10-28 107（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `982ccbfba84e` · [字段定义](../../DATASET.md)*
