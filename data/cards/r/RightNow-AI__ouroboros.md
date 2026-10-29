# RightNow-AI/ouroboros

⭐ 37 · Python · NOASSERTION · 推送 2026-04-02 · [GitHub](https://github.com/RightNow-AI/ouroboros) · [官网](https://runinfra.ai/) · 组织维护

**为递归 Transformer 生成动态权重的超网络研究库**

PyTorch 研究项目：在递归 transformer 块上挂载 CompactController 超网络，根据隐藏状态为每步递归生成对角调制向量，作用于冻结的 SVD 初始化 LoRA 基，使各递归步执行不同变换；配合门控递归（初始保留 88%）、逐步 LayerNorm 等机制压缩模型（Qwen2.5-3B 从 36 层保留 17 层，新增 0.6% 可训练参数）。README 报告了 FineWeb-edu 训练分布上的对比结果，并声明留出文本上尚未超过 17 层基线。提供训练脚本、Python API 与 66 项测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Controller 超网络按输入生成逐步 LoRA 对角调制
- 应用于 Qwen2.5-3B：保留 17 层，新增 9.2M 可训练参数（0.6%）
- 门控递归（初始保留 88% 隐状态）与 SVD 初始化 LoRA 基
- 提供 66 项 pytest 测试覆盖全部组件

## 适用场景

- 研究递归 Transformer 的动态权重生成与模型压缩
- 复现 Controller 与静态 LoRA 的对比实验
- 在 Qwen 3B 上做递归化改造训练实验

## 场景标签

 · 领域:深度学习研究/Transformer 架构

## 证据(README 行号)

> L9: Ouroboros attaches a compact Controller hypernetwork to a recursive transformer block. The Controller observes the c
> L121: delta_W_k = (alpha / rank) * B_k @ diag(f_theta(h_bar, step)) @ A_k

## 星数曲线

```mermaid
xychart-beta
    title "RightNow-AI/ouroboros 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-29 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `987bd9127564` · [字段定义](../../DATASET.md)*
