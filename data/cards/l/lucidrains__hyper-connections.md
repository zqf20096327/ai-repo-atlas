# lucidrains/hyper-connections

⭐ 189 · Python · MIT · 推送 2026-05-13 · [GitHub](https://github.com/lucidrains/hyper-connections) · 个人维护

**把 Hyper-Connections 论文的多残差流实现为易用 PyTorch 库**

lucidrains 对字节跳动 Hyper-Connections 论文的 PyTorch 实现：提供 init/expand/reduce stream 函数，将多条残差流接入 nn.Module 网络；支持 disable=True 对照普通残差连接，支持后续论文提出的分数化特征维度（num_fracs>1，可混合流与特征维分数）。面向想复现或跟进该研究方向的深度学习研究者与开发者，通过 pip 安装，README 引用多篇后续论文（Frac-Connections、mHC 等）。

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

- Hyper-Connections 多残差流的 PyTorch 实现
- disable=True 可在不改代码的情况下对照普通残差连接
- 支持 Frac-Connections 的分数化特征维度（num_fracs 参数）
- README 收录多篇后续研究引用（mHC、Frac-Connections 等）

## 适用场景

- 在自己的 PyTorch 网络中替换普通残差连接为多残差流
- 复现或跟进 Hyper-Connections 方向的研究
- 对照实验比较多残差流与普通残差的效果

## 场景标签

 · 领域:深度学习/模型架构

## 证据(README 行号)

> L5: Attempt to make multiple residual streams, proposed in Hyper-Connections paper out of Bytedance AI lab, accessible a
> L48: @article{Zhu2024HyperConnections,

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/hyper-connections 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 188 --> 190
    line [189, 189]
```

2026-10-18 189 → 2026-10-26 189（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `013856b245ba` · [字段定义](../../DATASET.md)*
