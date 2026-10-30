# OrderLab/TrainCheck

⭐ 75 · Python · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/OrderLab/TrainCheck) · [官网](http://orderlab.io/TrainCheck/) · 组织维护

**AI 训练可观测性框架：学习健康运行的不变量并检测静默错误**

面向 PyTorch 训练脚本的可观测性工具，通过追踪 PyTorch API 调用与模型状态变化，从已知正常的参考运行中推断不变量（invariants），再据此检查新训练运行是否违反这些不变量，从而在损失曲线或最终指标显示异常之前发现训练行为问题。工作流分四步：采集参考轨迹、推断不变量、采集目标轨迹、在线或离线检查，结果输出失败日志与 report.html 摘要。以 pip 包提供，支持 CUDA/conda/源码安装（详见安装指南）。项目处于活跃开发阶段，有 OSDI 2025 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 从参考运行自动推断训练不变量
- 追踪 PyTorch API 调用与模型状态变化
- 支持 traincheck-onlinecheck 在线检查与离线检查
- 输出失败日志与 report.html 结果摘要

## 适用场景

- 训练前先用正常脚本学习不变量，再检测新运行中的静默错误
- 在损失曲线显示异常前检查训练行为
- 为深度学习训练流程添加可观测性检查

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L8: TrainCheck catches silent training bugs by learning what a healthy run does, then checking a new run against those l
> L100: @inproceedings{TrainCheckOSDI2025,

## 星数曲线

```mermaid
xychart-beta
    title "OrderLab/TrainCheck 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 74 --> 76
    line [75, 75]
```

2026-10-18 75 → 2026-10-30 75（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `94992f7551e6` · [字段定义](../../DATASET.md)*
