# RUCAIBox/RecBole

⭐ 4,620 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/RUCAIBox/RecBole) · [官网](https://recbole.io/) · 组织维护 · 中文 README

**面向推荐算法研究的统一 PyTorch 实现库**

基于 Python 与 PyTorch 的推荐系统研究库，实现 94 个推荐算法，覆盖通用、序列、上下文感知与基于知识四大类，统一数据文件格式并支持 44 个基准数据集的处理或下载。提供多种评估协议、串/并行超参自动搜索（loguniform/choice）、多 GPU 与混合精度训练及显著性检验接口；快速启动脚本在 ml-100k 上运行 BPR 模型。支持 Linux/Windows 10/macOS，GPU 加速需 CUDA 9.2+。由中国人民大学等高校开发维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 94 个推荐算法，支持 44 个基准数据集
- 串行与并行两种超参自动搜索方式
- 支持多 GPU 训练与混合精度加速
- 配套 RecBole2.0 的 8 个专题扩展包与数据集仓库

## 适用场景

- 复现与对比推荐算法基准结果
- 在统一框架下开发新推荐模型
- 自动搜索推荐模型最优超参数
- 下载使用已格式化的推荐数据集

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L14: RecBole is developed based on Python and PyTorch for reproducing and developing recommendation algorithms in a unif
> L16: Our library includes 94 recommendation algorithms, covering four major categories:
> L94: |GPU-accelerated execution|Single-GPU utilization|Single-GPU utilization|Multi-GPU and mixed precision training|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `290f21093d42` · [字段定义](../../DATASET.md)*
