# sandeshbhatjr/energy-prediction

⭐ 40 · Python · GPL-3.0 · 推送 2026-03-21 · [GitHub](https://github.com/sandeshbhatjr/energy-prediction) · 个人维护

**德国电力日前/日内市场价格预测项目：统计与深度模型**

面向德国电力批发市场，预测日前与日内市场价格：包含 Jupyter 分析笔记本（/docs）、Python 后端预测服务（/backend，默认端口 8080）与 React+d3.js 前端可视化（/energy-viz-app）。方法分数据提取理解、统计模型、深度模型（LSTM）与分析讨论四部分，另含 Facebook Prophet 预测引擎的附加实验。数据来自 ENTSOE 透明平台 API。README 声明项目已停滞一段时间、计划重启，在线版本暂不可用，PyPI 包为未来计划。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 日前与日内市场价格预测，预测窗口至少提前一天
- 统计模型与 LSTM 深度模型结合，含 Fourier 分析
- Python 后端以服务形式管理预测任务，前端 d3.js 可视化
- 数据来源为 ENTSOE 透明平台 API

## 适用场景

- 研究德国电力市场价格预测方法
- 对比统计模型与深度模型的时间序列预测效果
- 复用数据提取与时序分析流程做能源价格预测

## 场景标签

 · 领域:能源/时间序列预测

## 证据(README 行号)

> L15: We are interested in the prediction of day-ahead and intra-day prices; the prediction window is at minimum one day 
> L22: 3. Deep models

## 星数曲线

```mermaid
xychart-beta
    title "sandeshbhatjr/energy-prediction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-27 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `9dfca03ed009` · [字段定义](../../DATASET.md)*
