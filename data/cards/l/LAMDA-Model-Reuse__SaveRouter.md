# LAMDA-Model-Reuse/SaveRouter

⭐ 26 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/LAMDA-Model-Reuse/SaveRouter) · [官网](https://lamda-model-reuse.github.io/SaveRouter/) · 组织维护 · 中文 README

**稀疏监督的 LLM 路由库：降低路由器训练的反馈获取开销**

南京大学 LAMDA 与 SinapisAI 合作的研究项目，提供 SAVERouter 稀疏监督 LLM 路由方法及 Python 实现。三阶段机制：分组经验贝叶斯 UCB 自适应采集每条查询 K 个候选模型的反馈、结构化组级先验与收缩估计能力、查询级残差修正构建质量-成本路由前沿。在四个路由基准上用约 33-41% 的训练反馈保持竞争性路由质量，并引入 SA-BEP/SA-CR 两个摊销监督成本的指标。PyPI 安装，附论文复现脚本与自定义基准 API；完整复现需 12-15 GB 磁盘，CUDA 推荐、CPU 支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自适应采集仅 K 个候选模型反馈，路由器拟合不接收稠密结果矩阵
- 四个基准上仅用约 33-41% 训练反馈
- SA-BEP/SA-CR 摊销监督开销的评估指标
- 提供 pip 包、smoke-test、复现脚本与在线反馈采集示例

## 适用场景

- 在有限标注反馈预算下训练 LLM 路由器
- 复现论文中四个路由基准的实验结果
- 在自定义基准上评估摊销监督成本后的路由收益

## 场景标签

 · 领域:LLM 基础设施/模型路由

## 证据(README 行号)

> L43: LLM routing can reduce serving cost, but training a router often requires
> L68: 1. **Adaptive acquisition** selects exactly `K` candidate models per training
> L83: python -m pip install saverouter

## 星数曲线

```mermaid
xychart-beta
    title "LAMDA-Model-Reuse/SaveRouter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c72a67b5c9ee` · [字段定义](../../DATASET.md)*
