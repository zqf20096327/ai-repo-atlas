# fraunhoferportugal/tsfel

⭐ 1,109 · Python · BSD-3-Clause · 推送 2026-10-22 · [GitHub](https://github.com/fraunhoferportugal/tsfel) · [官网](https://tsfel.readthedocs.io) · 组织维护

**时间序列特征提取库：从信号自动提取 60+ 统计/时域/频域/分形特征**

TSFEL 是 Fraunhofer Portugal 维护的开源 Python 库，面向时间序列分析与机器学习流水线，从统计、时域、频域、分形四个域自动提取 65 种以上特征，覆盖 ECG/EEG 等生物信号场景。支持以配置文件保存提取流程以保证可复现，可为每个特征预估计算耗时，并允许添加自定义特征；分形域特征默认关闭，需较长信号才有意义。通过 pip 安装，conda-forge 版本尚未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 65+ 特征覆盖统计/时域/频域/分形四个域
- 配置文件保存提取流程以保证可复现
- 预先估算特征提取的计算耗时
- 支持添加自定义特征并提供单元测试

## 适用场景

- 为时间序列分类/回归任务做特征工程
- 从 ECG/EEG 等生物信号中提取统计与频域特征
- 对较长信号做分形维度与熵分析

## 场景标签

 · 领域:机器学习/信号处理

## 证据(README 行号)

> L15: `TSFEL` is an open-source Python library for time series analysis. It centralizes a large and powerful feature set 
> L55: `TSFEL` automatically extracts more than 65 distinct features across statistical, temporal, spectral, and fractal

## 星数曲线

```mermaid
xychart-beta
    title "fraunhoferportugal/tsfel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 1106 --> 1110
    line [1107, 1109]
```

2026-10-18 1,107 → 2026-10-24 1,109（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `0344a6b66c5e` · [字段定义](../../DATASET.md)*
