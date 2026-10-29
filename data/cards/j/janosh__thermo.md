# janosh/thermo

⭐ 18 · Python · MIT · 推送 2026-07-31 · [GitHub](https://github.com/janosh/thermo) · 个人维护

**机器学习驱动的风险感知热电材料发现流水线**

科研代码库：用机器学习模型预测大量晶体结构的无量纲热电优值 zT 及各预测的不确定度，按在可容忍不确定性下最大化 zT 筛选候选结构，再通过贝叶斯优化与主动学习指导实验合成与表征，目标是发现高 zT（>1）、无铅无稀土的热电材料。以源码仓库形式提供，需 git clone 后 pip 安装依赖，通过 VS Code 交互式运行 src/notebooks 中的文件复现结果，支持 Python 3.8+。

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

- ML 模型预测 zT 及每次预测的不确定度
- 贝叶斯优化与主动学习指导昂贵实验的候选选择
- 目标为无铅、无稀土的高 zT（>1）热电材料

## 适用场景

- 科研人员复现数据驱动热电材料发现结果
- 在高机会成本、低通量验证场景下筛选候选材料
- 在此基础上贡献新的最优数据获取算法

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L8: The aim is to discover high-figure–of-merit ($zT > 1$) and sustainable (lead-free and rare earth-free) bulk thermoel
> L12: Consequently, searches have been unable to effectively guide experimentalists in the selection of exploring or expl

## 星数曲线

```mermaid
xychart-beta
    title "janosh/thermo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `035d76ca3f95` · [字段定义](../../DATASET.md)*
