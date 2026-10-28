# SCAI-Lab/VitalPy

⭐ 24 · Python · GPL-3.0 · 推送 2026-09-16 · [GitHub](https://github.com/SCAI-Lab/VitalPy) · 组织维护

**PPG 生命体征信号分析与特征提取库（400+ 特征）**

Python 3.9+ 编写的生命体征信号分析包，当前支持 PPG 信号预处理与特征提取：信号质量度量、基线提取、时间域/频率域/统计特征（超过 400 个），兼容 128–500 Hz 采样率的 PPG 数据，已在本地设备与大型数据集上测试。流水线最初为 AuroraBP 数据库分析实现。用户以 PPGSignal 类载入包含时间与信号列的 DataFrame，调用 check_keypoints 与 extract_features 获得关键点与特征，GPL-3.0 许可。

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

- PPG 预处理：信号质量度量、基线提取等
- 时间域/频率域/统计特征提取（>400 个特征）
- 兼容 128–500 Hz 采样率的 PPG 信号
- 配套 IEEE JBHI 论文（无袖带血压监测特征选择）

## 适用场景

- 从 PPG 波形中批量提取特征用于血压估计等研究
- 对 PPG 信号做质量评估与预处理
- 复现 AuroraBP 数据库分析流水线

## 场景标签

 · 领域:生物医学信号分析

## 证据(README 行号)

> L3: Currently, the package supports PPG preprocessing and extraction of more than 400 features. The PPG pipeline was ori
> L7: - PPG feature extraction: time-domain, frequency-domain, statistical features ( >400 features)
> L54: A. Cisnal, Y. Li, B. Fuchs, M. Ejtehadi, R. Riener and D. Paez-Granados, "Robust Feature Selection for BP Estimatio

## 星数曲线

```mermaid
xychart-beta
    title "SCAI-Lab/VitalPy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f3487e28d9fa` · [字段定义](../../DATASET.md)*
