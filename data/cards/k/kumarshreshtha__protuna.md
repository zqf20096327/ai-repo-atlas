# kumarshreshtha/protuna

⭐ 36 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/kumarshreshtha/protuna) · [官网](https://protuna.org) · 个人维护

**面向蛋白质工程的迭代优化框架：提出下一批待测变体**

用于迭代式蛋白质工程实验活动的优化框架：从历史诱变数据或单个命中序列出发，生成下一批建议测试的变体。Pipeline 分为设计空间定义、采样器生成候选、预测器评估目标属性与约束、获取策略按预算（适应度/不确定性/多样性）选择候选四步；支持奖励引导生成（Feynman–Kac steering、分类器引导、束搜索）与 Ray 分布式推理。以 pip 包提供，要求 Python 3.12+，protuna.train 模块标注尚未发布。

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

- Pipeline 组合设计空间、采样器、预测器与获取策略四类可替换组件
- 奖励引导生成：Feynman–Kac steering、分类器引导与束搜索
- Ray 分布式流式 API 支持本地加速器或集群上的大规模筛选
- 支持多目标优化：主目标加其余属性的不等式约束

## 适用场景

- 从历史诱变数据出发规划下一轮实验的变体批次
- 利用蛋白质语言模型先验并按设计目标引导序列生成
- 在集群上对大规模候选序列做分布式筛选与评估

## 场景标签

 · 领域:生命科学/蛋白质工程

## 证据(README 行号)

> L10: Protuna is an optimization framework for iterative protein engineering campaigns. Starting from historical mutagene
> L14: - **Guided generation:** Steer protein language models towards your design objectives with reward-guided generation
> L75: Selection is limited to the candidates proposed by the sampler. Protein language models provide a useful prior over


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7dfba8479387` · [字段定义](../../DATASET.md)*
