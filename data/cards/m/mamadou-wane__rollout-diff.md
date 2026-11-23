# mamadou-wane/rollout-diff

⭐ 4 · Python · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/mamadou-wane/rollout-diff) · 个人维护

**检测 RL 训练过程中模型输出行为变化的 CLI 工具**

面向强化学习训练的分析工具：读取本地 TRL 或 verl 训练 dump，按步骤对生成代码与文本的特征变化做序贯检测与事件排序，并将事件链接回原始数据中的样本，输出 JSON 与 HTML 报告。普通分析无需 GPU、模型 API 或安装训练框架；支持窗口对比、工具调用对比、本地回环调查应用、按步监视与通知，另提供 Python API（extract/featurize/analyze_rollouts）与 TRL/verl 回调接入。回放功能需要 Docker 与明确授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取本地 TRL/verl dump，无需 GPU、模型 API 或训练器安装
- 序贯变化检测（15 步基线、连续三次观测）与实验性回溯检测器
- rollout diff 支持窗口/轨迹对比及 agent 工具调用差异分析
- 提供 Python 适配器与 TRL 1.18.0 GRPO、verl 0.9.1 回调接入

## 适用场景

- 检测 RL 训练中 reward hacking 导致的输出行为漂移
- 对比训练前后两个步骤窗口的生成差异
- 分析 SWE-rebench/OpenHands/Inspect 录制的 agent 日志
- 训练时按步监视 dump 并向指定端点发送通知

## 场景标签

`模型评测` `强化学习` · 领域:评测与运维

## 证据(README 行号)

> L3: Rollout Diff finds changes in generated code and prose across RL training steps. It reads a TRL or verl dump locally
> L104: - **Connect a producer.** `AsyncRolloutProducer.submit` accepts complete, planned groups into a bounded queue. A r

## 星数曲线

```mermaid
xychart-beta
    title "mamadou-wane/rollout-diff 星数(近 3 点)"
    x-axis ["2026-10-22", "2026-10-25", "2026-11-23"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-22 3 → 2026-11-23 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `ccce684333cb` · [字段定义](../../DATASET.md)*
