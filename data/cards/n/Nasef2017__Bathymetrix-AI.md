# Nasef2017/Bathymetrix-AI

⭐ 23 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/Nasef2017/Bathymetrix-AI) · 个人维护

**QGIS 卫星反演水深研究工具包：多光谱影像+ICESat-2 激光测深自动建模**

面向科研用户的 QGIS 研究工具包，从经大气校正的多光谱卫星影像出发，结合 ICESat-2 (ATL24) 激光测深数据，通过五阶段工作流（预处理、鲁棒过滤、Auto-ML 建模、空间细化、验证报告）生成水深图。支持评估 15+ 种机器学习算法、7 种模型选择策略、超参数优化与空间交叉验证，另提供多时相/多景 Masterflow、海岸动态分析与潮汐基准转换等模块，输出 IHO S-44 合规评估与 HTML 交互报告。要求影像为地表反射率且栅格值为 Float。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五阶段端到端 SDB 工作流：预处理→过滤→Auto-ML→空间细化→验证报告
- 自动评估 15+ 种 ML 算法与 7 种模型选择策略（含蒙特卡洛 Winner Stability）
- 多方法光学浅水区提取引擎（Knee-Point/Multi-Otsu/GMM/拓扑清洗）
- IHO S-44 Order 1a/2 TVU 合规评估与交互式 HTML 验证面板

## 适用场景

- 从单景卫星影像自动生成水深图并评估精度
- 多景/多年联合建模与海岸冲淤动态分析
- 下载并准备 ICESat-2 测深训练数据，转换潮汐基准

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: **Bathymetrix-AI (v7.9)** is a professional QGIS research toolkit for high-precision Satellite-Derived Bathymetry (S
> L7: The toolkit integrates multispectral satellite imagery with ICESat-2 (ATL24) LiDAR bathymetry through a modular and 
> L62: #### Phase 03: Global Auto-ML & Feature Analysis

## 星数曲线

```mermaid
xychart-beta
    title "Nasef2017/Bathymetrix-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a00522ea9035` · [字段定义](../../DATASET.md)*
