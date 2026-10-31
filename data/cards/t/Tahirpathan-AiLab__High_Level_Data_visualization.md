# Tahirpathan-AiLab/High_Level_Data_visualization

⭐ 24 · Python · 推送 2026-10-18 · [GitHub](https://github.com/Tahirpathan-AiLab/High_Level_Data_visualization) · 个人维护

**MetaMotion 传感器数据处理管线：为杠铃动作分类准备数据集**

Python 脚本集合，处理 MetaMotion 可穿戴设备的加速度计与陀螺仪原始记录：从文件名提取参与者/动作/重量元数据，合并双传感器流并按时间序列重采样同步，输出箱线图与直方图做探索分析，比较 IQR、Chauvenet 准则、局部离群因子三种异常检测方法，最终导出 Pickle 格式的清洗数据集，供后续杠铃动作分类与次数统计的机器学习流程使用。原始数据由 Dave Ebbelaar 等采集（5 名参与者）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 加速度计/陀螺仪数据合并与时间序列重采样同步
- 三种统计异常检测方法（IQR/Chauvenet/LOF）实现与比较
- 从文件名自动提取参与者、动作标签与重量类别
- 导出可复用的 Pickle 清洗数据集

## 适用场景

- 预处理可穿戴传感器数据用于动作识别建模
- 比较不同统计异常检测方法在传感器数据上的效果
- 为杠铃动作分类与次数统计准备分析就绪的数据集

## 场景标签

 · 领域:数据科学/人体活动识别

## 证据(README 行号)

> L3: This project focuses on processing, visualizing, and preparing accelerometer and gyroscope sensor data collected usi
> L25: Finally, the processed dataset and the cleaned dataset are exported as Pickle files, providing reusable datasets fo

## 星数曲线

```mermaid
xychart-beta
    title "Tahirpathan-AiLab/High_Level_Data_visualization 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-31 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6b6d92014254` · [字段定义](../../DATASET.md)*
