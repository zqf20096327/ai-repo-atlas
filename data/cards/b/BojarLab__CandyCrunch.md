# BojarLab/CandyCrunch

⭐ 37 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/BojarLab/CandyCrunch) · 组织维护

**从 LC-MS/MS 数据预测聚糖结构的深度学习工具包**

包含 CandyCrunch 模型及推理管线与下游谱图处理工具的 Python 包，从 Thermo .raw、Bruker timsTOF .d、mzML、mzXML、mgf 或 xlsx 文件预测 N/O/lipid 类聚糖结构，方法发表于 Nature Methods（Urban et al. 2024）。提供 CLI（candycrunch_predict）、wrap_inference 函数、免安装的 Google Colab 笔记本，以及无需 Python 环境的 Windows/macOS 桌面应用（含 GUI 安装、SNFG 结构绘图、特征表汇总与手工整理）。限制：diaPASEF 与无离子迁移的 .tsf 数据不支持；macOS 应用未公证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 深度学习模型从 LC-MS/MS 谱图预测聚糖结构（N/O/lipid 类）
- 直接读取 Thermo .raw 与 Bruker timsTOF .d（DDA-PASEF）数据，无需厂商软件转换
- 提供 CLI、Python API、Colab 笔记本与 Windows/macOS 桌面应用四种使用方式
- 多文件批处理并汇总为带相对丰度的特征表，输出含 SNFG 结构图与注释 MS² 谱

## 适用场景

- 从我的质谱数据预测 N-或 O-连接聚糖结构
- 不写代码、用桌面应用处理 .raw/mzML 文件并获得聚糖注释
- 多个样品批量处理并生成跨运行一致的特征表

## 场景标签

 · 领域:生物信息学/糖组学

## 证据(README 行号)

> L9: **CandyCrunch** is a package for predicting glycan structure from LC-MS/MS data. It contains the CandyCrunch model, 

## 星数曲线

```mermaid
xychart-beta
    title "BojarLab/CandyCrunch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-28 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ecd127b6efe2` · [字段定义](../../DATASET.md)*
