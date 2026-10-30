# Noble-Lab/Carafe

⭐ 26 · Java · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/Noble-Lab/Carafe) · 组织维护

**为 DIA 蛋白质组学生成实验特定 in silico 谱图库的深度学习工具**

Carafe2 通过在用户自己的 DIA 数据上直接训练保留时间、碎片离子强度及离子淌度（timsTOF）预测模型，生成实验条件匹配的 in silico 谱图库，供 DIA-NN 检索使用。已在 Thermo、SCIEX、Bruker 质谱仪数据上测试。提供 Windows/Linux/macOS 图形界面（GUI 内一键安装 Python 依赖）、命令行与 Skyline 集成三种使用方式，GUI 支持三条工作流：从 DIA-NN 搜索开始建库、从已有报告建库、端到端分析。CLI 运行需 Java 25.0.2+ 与 Python，工作流 1/3 需另行安装 DIA-NN，Thermo raw 格式需 MSConvert。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在用户 DIA 数据上训练 RT、碎片强度、离子淌度预测模型
- 输出 DIA-NN 兼容的 TSV 谱图库（carafe_spectral_library.tsv）
- Windows/Linux/macOS 图形界面，GUI 内安装全部 Python 依赖
- 支持 mzML、Thermo raw、Bruker raw(.d) 输入格式

## 适用场景

- 为我的 DIA 实验构建匹配实验条件的谱图库
- 用 Carafe2+DIA-NN 完成端到端 DIA 肽段检测与定量
- 基于已有 DIA-NN 报告直接微调模型生成新库

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L7: **Carafe2** is a deep learning-based tool for generating experiment-specific *in silico* spectral libraries for DIA 
> L84: Below is an example of the GUI screenshot for spectral library generation with a DIA-NN search. The input MS/MS fil

## 星数曲线

```mermaid
xychart-beta
    title "Noble-Lab/Carafe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `31497df1f1b1` · [字段定义](../../DATASET.md)*
