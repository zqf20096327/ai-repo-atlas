# Lomnus-ai/TokenBurner

⭐ 173 · MIT · 推送 2026-05-03 · [GitHub](https://github.com/Lomnus-ai/TokenBurner) · 组织维护

**Claude Code 技能：按需在扩展思考中消耗 token 的负载工具**

面向 Claude Code CLI 的一个 skill：激活后模型在每次回复前的扩展思考中求解数学难题（矩阵行列式、TSP、高斯消元等 50 种题库），从而消耗额外 token，可见输出不变。提供 small/medium/large/xlarge 四档负载（1-10 题），负载由消息 Unicode 码点和决定的种子确定性生成，跨轮次无缓存。README 给出各档位的时长、token 数与成本基准（基于 Claude Opus 4.6）。安装方式为 git clone 后复制或符号链接技能目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四档负载（1-10 题），基准数据：xlarge 约 32 倍成本、平均 514s
- 50 种参数化数学题库，种子由消息确定性推导，同消息可复现
- 消耗发生在扩展思考中，可见输出不受影响

## 适用场景

- 对 LLM 后端做压力测试
- 需要提高 token 用量指标的场景
- 观察不同负载档位下的响应时长与成本变化

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A Claude Code skill that burns tokens on demand. Stress test your LLM backend, inflate your AI adoption metrics, or 
> L19: Activate the skill, and Claude quietly solves hard math problems (matrix determinants, TSP, Gaussian elimination, e

## 星数曲线

```mermaid
xychart-beta
    title "Lomnus-ai/TokenBurner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 172 --> 174
    line [173, 173]
```

2026-10-18 173 → 2026-10-23 173（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1dbe6398888d` · [字段定义](../../DATASET.md)*
