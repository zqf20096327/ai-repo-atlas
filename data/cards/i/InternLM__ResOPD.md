# InternLM/ResOPD

⭐ 67 · Python · Apache-2.0 · 推送 2026-10-09 · [GitHub](https://github.com/InternLM/ResOPD) · [官网](https://arxiv.org/abs/2610.04882) · 组织维护 · 中文 README

**稀疏在线策略蒸馏的尾部残差化训练方法实现**

ResOPD 是一种在线策略蒸馏（OPD）梯度估计方法的研究实现，基于 verl 框架构建：从教师模型 Top-k 概率与学生采样 token 分数估计全词表 reverse-KL 梯度，对可观测的粗粒度梯度精确解析计算，仅对未分解的尾部分布残差进行采样，无需额外教师前向。面向 LLM 蒸馏研究人员与工程师，提供 DeepMath 数据示例、启动脚本与单元/集成测试；本版本支持 vLLM 教师打分与 FSDP/FSDP2 学生 logits，Megatron 学生、SGLang 教师等路径未启用，完整 GPU 训练运行不在已记录的发布验证内。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 精确解析教师 Top-k 粗梯度 + 仅采样尾部残差的估计器
- 无需额外教师前向，复用同一稀疏教师负载
- 提供与 verl 集成的启动脚本与 DeepMath 数据（1,024 训练样本）
- 22 项独立检查 + 13 项集成检查的发布验证

## 适用场景

- 在 verl 中用稀疏教师反馈做在线策略蒸馏训练
- 复现论文中的数学推理蒸馏实验
- 以 loss_mode: resopd 将估计器接入现有 verl OPD 配置

## 场景标签

`模型训练` `微调` · 领域:训练与推理

## 证据(README 行号)

> L31: **ResOPD** estimates the full-vocabulary reverse-KL gradient from the teacher's
> L36: This repository provides the core implementation and its integration with
> L180: **Supported path:** vLLM teacher scoring and eager FSDP/FSDP2/VeOmni student

## 星数曲线

```mermaid
xychart-beta
    title "InternLM/ResOPD 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 65 --> 68
    line [66, 67, 67]
```

2026-10-18 66 → 2026-10-26 67（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `81f14a75fb4b` · [字段定义](../../DATASET.md)*
