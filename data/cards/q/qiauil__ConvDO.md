# qiauil/ConvDO

⭐ 26 · Python · MIT · 推送 2026-06-02 · [GitHub](https://github.com/qiauil/ConvDO) · [官网](https://qiauil.github.io/ConvDO/) · 组织维护

**PyTorch 可微卷积微分算子库，用于物理深度学习研究**

基于 PyTorch 的卷积微分算子库，以可微方式计算空间导数，供物理驱动的深度学习研究使用。目前仅支持 2D 场；支持 GPU 与自动微分；Dirichlet 与 Neumann 边界条件支持二阶精度，周期边界条件最高八阶；域内可包含障碍物。通过 pip 或本地脚本安装，README 列出使用该库的下游项目（翼型流场预测 DBFP）及 PhiFlow、Exponax 等相关框架供进一步参考。

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

- 卷积神经网络计算空间导数，可微且支持 GPU
- Dirichlet/Neumann 边界二阶精度，周期边界最高八阶
- 支持域内障碍物
- 基于 PyTorch，当前仅支持 2D 场

## 适用场景

- 物理深度学习研究中以可微方式计算空间导数
- 构建含 PDE 约束的可微仿真流程
- 翼型流场预测等 CFD 相关研究任务

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L18: * PyTorch-based and only supports 2D fields at the moment.
> L19: * Powered by convolutional neural network.
> L41: For more research on physics based deep learning research, please visit the website of our research group at TUM.

## 星数曲线

```mermaid
xychart-beta
    title "qiauil/ConvDO 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `48fa8cd12d63` · [字段定义](../../DATASET.md)*
