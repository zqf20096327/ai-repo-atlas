# lucidrains/multiscreen

⭐ 19 · Python · MIT · 推送 2026-05-13 · [GitHub](https://github.com/lucidrains/multiscreen) · 个人维护

**Ken Nakanishi 论文 Screening is Enough 的 Multiscreen 注意力 PyTorch 实现**

lucidrains 实现的 Multiscreen：一种非 softmax 注意力机制，采用 ReLU 平方激活、内容相似度阈值筛选与数值的激进归一化。以 PyPI 包 multiscreen 提供，可导入为 PyTorch 模块使用，附带 enwik8 字符级语言建模训练脚本。README 引用 Nakanishi 的 Screening Is Enough 论文及相关 Sparse Attention with Linear Units、ReLU 复活论文。代码量小，无预训练权重，需自训。

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

- 非 softmax 注意力：ReLU 平方激活 + 内容相似度阈值 + 激进归一化
- pip 安装后作为 PyTorch 模块导入使用
- 附带 enwik8 训练脚本

## 适用场景

- 研究/复现 Screening is Enough 的 Multiscreen 注意力
- 作为 PyTorch 注意力模块嵌入自有模型做实验
- 在 enwik8 字符建模任务上训练验证

## 场景标签

 · 领域:深度学习/注意力机制研究

## 证据(README 行号)

> L5: Implementation of Multiscreen proposed by Ken Nakanishi for Screening is Enough
> L7: Basically it is a non-softmax attention with ReLU squared activation, content similarity thresholding, and aggressiv

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/multiscreen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `461a7e2d1300` · [字段定义](../../DATASET.md)*
