# sisinflab/elliot

⭐ 298 · Python · Apache-2.0 · 推送 2026-10-08 · [GitHub](https://github.com/sisinflab/elliot) · 组织维护

**面向科研的推荐系统实验评测框架：从数据到统计报告全流程**

配置文件驱动的推荐系统评测框架：加载、过滤、划分数据（含时序划分与嵌套 K 折交叉验证），对多种推荐算法做超参数优化（如网格搜索），选择最优模型并与基线对比，计算从准确率到偏差、公平性等指标，并执行 Wilcoxon 与配对 t 检验统计，以保证实验可复现。面向推荐系统研究者，提供 Python API 的 run_experiment 入口。依赖 TensorFlow，需 Python 3.6+，支持 Linux/Windows 10/macOS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一配置文件驱动从数据划分到报告生成的完整实验流程
- 覆盖准确率、beyond-accuracy、偏差与公平性指标，含 Wilcoxon 与配对 t 检验
- 多种划分与过滤策略（时序划分、嵌套 K 折交叉验证等）
- 支持多算法超参数优化与基线对比

## 适用场景

- 科研中可复现地评测与对比推荐算法
- 一键完成数据划分、调参、训练与统计检验的完整实验
- 按配置文件快速搭建 MovieLens 等数据集上的对照实验

## 场景标签

`推荐系统` `模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L9: Elliot is a comprehensive recommendation framework that analyzes the recommendation problem from the researcher's pe
> L20: Elliot optimizes hyperparameters for several recommendation algorithms, selects the best models, compares them with
> L21: baselines providing intra-model statistics, computes metrics spanning from accuracy to beyond-accuracy, bias, and f

## 星数曲线

```mermaid
xychart-beta
    title "sisinflab/elliot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 297 --> 299
    line [298, 298]
```

2026-10-18 298 → 2026-10-25 298（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `871aa6de9950` · [字段定义](../../DATASET.md)*
