# teerthsharma/Alcyone-W

⭐ 3 · Python · NOASSERTION · 推送 2026-11-22 · [GitHub](https://github.com/teerthsharma/Alcyone-W) · [官网](https://huggingface.co/teerthsharma/Alcyone-W) · 个人维护

**以拓扑不变量为预测目标的 JEPA，用于质子对撞事例分析**

W-JEPA 将质子-质子对撞事例的横向动量铺成 (η,φ) 地形，随机遮蔽窗口后要求网络预测该窗口的分水岭拓扑量（盆地数、H0 持续性、盆地能量），该目标由 Lean 4 定理驱动的 union-find 洪水精确计算而非网络生成，共 1,818 个无 sorry 声明。训练部分仅 5.9M 参数编码器/预测器，配合冻结的 Galactica-6.7B 嵌入粒子描述。数据为 CMS 开放数据 4M 事例。报告结果同时列出未通过的预注册指标（电荷、运动学 MLP 基线仍更优）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 预测目标为精确计算的拓扑不变量，无 EMA teacher/stop-gradient/方差正则
- Lean 4 证明 1,818 个声明，配套 Haskell 镜像经 QuickCheck 验证
- 5.9M 训练参数 + 冻结 Galactica-6.7B，附带仅 4 个确定性工具的问答 agent
- 预注册指标，结果包括未达标项一并报告

## 适用场景

- 高能物理事例的喷注多重数等性质研究
- 带地形/高度函数数据（图像、点云、图）的拓扑表示学习实验
- 形式化验证与机器学习结合的方法探索

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: **W-JEPA: a joint-embedding predictive architecture whose target is a topological invariant, not a learned embedding
> L74: 3. **Mask.** A random $8 \times 16$ window is hidden. A convolutional encoder on the cylinder sees the complement.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `debdd763b909` · [字段定义](../../DATASET.md)*
