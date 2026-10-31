# Biohub/octopi

⭐ 19 · Python · NOASSERTION · 推送 2026-10-07 · [GitHub](https://github.com/Biohub/octopi) · 组织维护

**Cryo-ET 断层扫描中蛋白质 3D 颗粒挑选的深度学习框架**

面向冷冻电子断层扫描（cryo-ET）研究的深度学习流水线：训练与执行 3D 自编码器/3D U-Net 模型，在复杂细胞环境中自动识别与提取蛋白质颗粒。基于存储无关 API copick 读取本地或远程的断层图与分割结果；通过 Optuna 贝叶斯优化自动探索模型架构配置，支持 SLURM 集群运行与 MLflow 实验跟踪，提供命令行与 Python API 双接口。以 pip 安装的 Python 包形式发布，附论文预印本供引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3D U-Net 模型训练与评估，用于颗粒分割
- Optuna 贝叶斯优化自动搜索模型配置
- 基于 copick 的本地/远程数据访问
- SLURM 集群支持与 MLflow 实验跟踪

## 适用场景

- 从大量 cryo-ET 断层图中自动挑选蛋白质颗粒
- 训练自定义 3D 分割模型并自动调优架构
- 在 HPC 集群上运行颗粒挑选流水线

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L8: **O**bject dete**CT**ion **O**f **P**rote**I**ns. A deep learning framework for Cryo-ET 3D particle picking with aut
> L18: - **3D U-Net Training**: Train and evaluate custom 3D U-Net models for particle segmentation

## 星数曲线

```mermaid
xychart-beta
    title "Biohub/octopi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `622cc2290a49` · [字段定义](../../DATASET.md)*
