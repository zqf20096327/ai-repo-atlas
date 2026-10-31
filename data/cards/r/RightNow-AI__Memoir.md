# RightNow-AI/Memoir

⭐ 15 · Python · Apache-2.0 · 推送 2026-09-18 · [GitHub](https://github.com/RightNow-AI/Memoir) · [官网](https://www.rightnowai.co/) · 组织维护

**持续学习快权重架构及其预注册证伪实验代码**

Memoir 是一个持续学习 transformer 架构的 PyTorch 研究实现：四级权重时间尺度（快/情景/慢/冻结核）、可变步数的 pondering 循环块、基于能量的世界模型信号、经元优化发现的更新规则。仓库同时发布预注册证伪实验：在等参数等 FLOPs、12 种子的配对测试中，pondering 时写入快权重相对只在 pass 间写入平均回忆率低 13.5 点（固定预算下的速度惩罚，960 步时差距闭合）。当前为早期阶段，81k–236k 参数、单一任务族，需 CUDA 单 GPU 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 四级权重时间尺度 + 自定步数 pondering 核 + 能量头世界模型信号
- 预注册证伪实验：配对 t=3.23（11 df），快权重写入组在固定预算下慢 13.5 点
- 所有数字可溯源到 results/falsify/summary.json 的逐种子原始分数
- 提供完整复现命令（pip 可编辑安装 + pytest + 实验运行脚本）

## 适用场景

- 复现或审查该持续学习架构的证伪实验
- 研究快权重写入时机与写入量对学习速度的影响
- 作为四级权重/pondering 架构的代码起点做后续实验

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: Memoir is an architecture with weights that keep moving. We are building it in
> L111: Needs PyTorch with CUDA. Built against torch 2.11 and CUDA 12.8. Everything here
> L138: Early. 81k to 236k parameters. One task family. None of this transfers to a

## 星数曲线

```mermaid
xychart-beta
    title "RightNow-AI/Memoir 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ca15f32c882a` · [字段定义](../../DATASET.md)*
