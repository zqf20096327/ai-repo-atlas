# iamgooold/malicious-url-detection-using-ml

⭐ 13 · Python · Apache-2.0 · 推送 2026-05-15 · [GitHub](https://github.com/iamgooold/malicious-url-detection-using-ml) · 个人维护

**机器学习恶意 URL 检测系统：判定 URL 安全或恶意**

基于 Python 与 Scikit-learn/XGBoost 的网络安全分类系统，通过 30 余个结构化与统计特征（长度、字符熵、域名、安全维度）分析 URL 并判定其是否恶意，不检查网页内容。提供 Streamlit Web 界面、Python API 与 Flask REST API（单条与批量预测），支持 Docker 部署。README 报告多模型对比指标，集成模型准确率 97.1%（XGBoost 96.5%）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 30+ 工程 URL 特征，覆盖长度/熵/域名/安全等类别
- 不检查网页内容的 URL 分析方式
- 提供 Web 界面、Python API 与 REST API（含批量预测）
- 多模型对比（Random Forest/XGBoost/SVM/集成）

## 适用场景

- 对可疑 URL 做安全或恶意的判定
- 批量检测 URL 列表中的钓鱼/恶意链接
- 通过 REST API 集成到现有安全流程

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L14: A machine learning-based cybersecurity system that detects and classifies malicious URLs by analyzing structural an
> L26: |Machine Learning|Scikit-learn, XGBoost|

## 星数曲线

```mermaid
xychart-beta
    title "iamgooold/malicious-url-detection-using-ml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `f4b0ffab4067` · [字段定义](../../DATASET.md)*
