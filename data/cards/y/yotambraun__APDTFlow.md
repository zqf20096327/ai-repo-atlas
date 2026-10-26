# yotambraun/APDTFlow

⭐ 44 · Python · MIT · 推送 2026-06-14 · [GitHub](https://github.com/yotambraun/APDTFlow) · [官网](https://github.com/yotambraun/APDTFlow) · 个人维护

**连续时间概率时序预测库：Neural ODE 回答何时越限**

PyTorch 时序预测框架，用 Neural ODE（可选 Transformer/TCN/Ensemble）把时间建模为连续过程，单一训练模型支持三类 API：predict 输出未来 k 步值、predict_at 在任意实值时间点查询、predict_when 给出跨越阈值的时间并附带共形校准时间窗与 act_by 调度边。提供车队级 predict_when_fleet 生成按 act-by 排序的维护计划，以及多变量传感器融合、回流测试、TorchScript 导出、FastAPI 服务示例等工程功能。面向研究者和运维/预测性维护从业者。限制：序列需约 500 点以上，零样本能力不提供，1.0 前 API 可能变动，≤0.3.x 检查点全部失效。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- predict_at 支持在任意实值时间戳（含训练视野外）查询预测
- predict_when 输出带共形校准时间窗的越限时刻，含 act_by 调度字段
- predict_when_fleet 车队级 API 生成按 act-by 排序的维护计划并导出 CSV
- 支持 Neural ODE/Transformer/TCN/Ensemble 四种架构与自适应共形预测

## 适用场景

- 预测设备退化并安排按 act-by 排序的维护计划（电池寿命、涡扇发动机）
- 在任意时间点（如 14:37、3.6 天后）查询序列值而非固定步长
- 回答何时跨越某阈值的业务问题并附带校准不确定性

## 场景标签

 · 领域:时序预测/预测性维护

## 证据(README 行号)

> L24: Forecasting tools tell you *what the value will be*. APDTFlow models time as **continuous**
> L32: |What are the next k values?|`model.predict()`|
> L33: |What is the value at **any** moment (14:37, in 3.6 days, beyond the trained horizon)?|`model.predict_at(timestamps
> L34: |**When** will the value cross a threshold, with uncertainty on the time itself?|`model.predict_when(threshold)`|

## 星数曲线

```mermaid
xychart-beta
    title "yotambraun/APDTFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-26 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b19100357f8b` · [字段定义](../../DATASET.md)*
