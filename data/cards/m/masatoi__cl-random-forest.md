# masatoi/cl-random-forest

⭐ 61 · Common Lisp · MIT · 推送 2026-08-07 · [GitHub](https://github.com/masatoi/cl-random-forest) · 个人维护

**Common Lisp 实现的随机森林分类/回归库**

用 Common Lisp 编写的随机森林库，支持多类分类与一元回归，可构建单棵决策树与随机森林并做预测。包含全局精炼算法（CVPR2015 论文方法），用线性分类器 AROW 利用树间全局信息改进预训练森林；还有全局剪枝以压缩模型体积，剪枝后叶节点可减至约 1/10 而精度基本不变。支持训练与预测的多线程并行（SBCL、CCL 上测试），并附 packed 推理子系统（5-8 倍加速、可序列化）。多变量回归尚未实现。通过 quicklisp 或 Roswell 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多类分类与一元回归的随机森林实现
- Global Refinement（AROW 线性分类器）与 Global Pruning 压缩模型
- packed 推理子系统：5-8 倍加速、多线程安全、可序列化
- 基于 lparallel 的训练/预测并行化

## 适用场景

- 在 Common Lisp 项目中做分类或回归任务
- 需要模型体积压缩的场景（剪枝后叶节点减至约 1/10）
- 训练好的模型需序列化保存并多线程在线推理

## 场景标签

 · 领域:机器学习

## 证据(README 行号)

> L6: Cl-random-forest is a implementation of Random Forest for multiclass classification and univariate regression writte
> L133: Cl-random-forest has a way to improve pre-trained random forest using global information between each decision tre

## 星数曲线

```mermaid
xychart-beta
    title "masatoi/cl-random-forest 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-25 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `91337f53cb28` · [字段定义](../../DATASET.md)*
