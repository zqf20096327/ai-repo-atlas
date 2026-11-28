# zou-group/reward_subsystem

⭐ 10 · Python · MIT · 推送 2026-10-08 · [GitHub](https://github.com/zou-group/reward_subsystem) · [官网](https://arxiv.org/abs/2602.00986) · 组织维护 · 中文 README

**研究论文复现代码：定位 LLM 中的稀疏奖励子系统神经元**

NeurIPS 2026 论文 Sparse Reward Subsystem 的官方代码库。提供七步流水线复现论文两条核心曲线：先用 vLLM 对模型在基准上生成带评分的推理响应，再用 TD 损失训练 value probe（价值神经元）、经蒙特卡洛 rollout 估计 TD error 后训练 dopamine probe（多巴胺神经元），最后分别在剪枝比例下计算 AUC 与 Spearman 相关并绘图。支持更换模型、基准（math500/gsm8k/arc）与层号。通过 conda + pip 源码安装，面向可解释性研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 七步脚本流水线：生成响应→训练 value/dopamine probe→剪枝曲线→绘图
- value probe 用 TD 损失追踪响应成功率；dopamine probe 预测段落级 TD error
- 支持 math500、gsm8k、arc 三个基准，可换模型与层号复现论文图表

## 适用场景

- 复现论文中 AUC/相关性随剪枝比例变化的图表
- 在其他 RL 训练的 LLM 上分析是否存在类似的稀疏奖励子系统
- 借鉴 TD 探针与蒙特卡洛 rollout 的可解释性分析方法

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L9: We find sparse sets of neurons in LLM hidden states: **value neurons**, which encode how likely the model is to solv
> L15: - **[October 2026]** The code for training value and dopamine probes and for reproducing the pruning curves is now 
> L42: The two measurements behind these claims are the curves this repository reproduces: **AUC vs. pruning ratio** for t


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `6b8dd9872a3c` · [字段定义](../../DATASET.md)*
