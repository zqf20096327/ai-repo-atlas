# sadia-sigma-lab/BLINDSPOT

⭐ 16 · Python · MIT · 推送 2026-09-16 · [GitHub](https://github.com/sadia-sigma-lab/BLINDSPOT) · [官网](https://arxiv.org/abs/2609.16305) · 组织维护

**长程工具调用 agent 的安全与拒绝校准基准**

轨迹级安全评测基准：以完整多轮交互（含工具调用、状态转移、授权历史）为评测单元，捕捉累积上下文、过期授权与环境注入攻击中逐渐出现的安全失败。数据集含 3,024 条轨迹、65 个场景、7 个领域、22 个攻击家族，轨迹标注为安全完成/正确拒绝/不安全完成/过度拒绝/不确定五类。提供场景、攻击家族与新领域的扩展 API，依赖 Python≥3.10 与 AWS Bedrock 凭证用于 LLM 生成与裁决。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3,024 条轨迹、65 场景、7 领域、22 攻击家族的轨迹级安全基准
- 五类轨迹结局标注（含过度拒绝与不安全完成）
- 自适应对手：用户 agent 依据目标 agent 实际回复生成后续攻击消息
- 可扩展的场景/攻击家族/领域插件 API

## 适用场景

- 评测长程工具调用 agent 能否全程维持安全边界
- 度量 agent 的拒绝校准（正确拒绝 vs 过度拒绝）
- 研究环境注入攻击与过期授权下的安全失败

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: **BLINDSPOT** is a trajectory-level safety benchmark for long-horizon tool-using agents. Rather than evaluating isol
> L22: |Total trajectories|**3,024**|

## 星数曲线

```mermaid
xychart-beta
    title "sadia-sigma-lab/BLINDSPOT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5b94729161bc` · [字段定义](../../DATASET.md)*
