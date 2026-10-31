# ungaaaabungaaa/predictive-maintenance

⭐ 18 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/ungaaaabungaaa/predictive-maintenance) · 个人维护

**NASA C-MAPSS FD001 剩余寿命预测的可复现实验**

在 NASA 模拟 C-MAPSS FD001 发动机数据上进行的可复现剩余使用寿命（RUL）实验：按引擎划分 80/20 训练验证集，比较均值基线、Ridge、随机森林与可选 XGBoost，按验证 RMSE 选模型后在官方测试端点上评估。首次记录运行选中随机森林，未截断测试 RUL 上 RMSE 20.21 周期、MAE 14.92 周期。CPU 即可运行，无需 GPU 或 API key，训练在离线状态完成，输出 HTML 报告、指标与预测图。README 明确这是教育性基准，使用模拟数据，不构成故障保证或运维安全系统。

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

- 按引擎分组验证的模型选择流程（均值基线/Ridge/随机森林/XGBoost）
- SHA-256 数据校验与记录式可复现运行，输出 HTML 报告
- CPU 即可运行，无需账号、API key 或 GPU，训练离线完成
- 提供 inspect/plan/monitor 启发式维护标签带（非校准故障概率）

## 适用场景

- 复现 NASA C-MAPSS FD001 上的 RUL 基准实验
- 比较不同回归模型在剩余寿命预测任务上的表现
- 学习按引擎分组的验证方法与截断 RUL 处理

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: A reproducible remaining-useful-life experiment on NASA's **simulated C-MAPSS FD001 engine data**. It compares basel
> L9: The first recorded run selected Random Forest: **20.21 cycles RMSE and 14.92 cycles MAE** against uncapped test RUL,

## 星数曲线

```mermaid
xychart-beta
    title "ungaaaabungaaa/predictive-maintenance 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-28 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `bd52adc274ee` · [字段定义](../../DATASET.md)*
