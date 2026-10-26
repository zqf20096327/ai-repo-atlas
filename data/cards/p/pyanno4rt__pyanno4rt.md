# pyanno4rt/pyanno4rt

⭐ 30 · Python · GPL-3.0 · 推送 2026-08-09 · [GitHub](https://github.com/pyanno4rt/pyanno4rt) · [官网](https://pyanno4rt.readthedocs.io/en/latest/) · 组织维护

**放射治疗逆向计划优化 Python 包，含 ML 预测模型组件**

面向光子与质子治疗计划的逆向优化 Python 包：支持从 DICOM/MATLAB/Python 文件导入患者数据与剂量信息，进行单/多目标（不）约束优化，涵盖字典式、加权和与 Pareto 分析方法，集成 Proxmin/Pymoo/PyPop7/SciPy 的局部与全局求解器。其中数据驱动部分提供 TCP/NTCP 结果预测模型（7 种内部模型类、27 类特征目录、SMBO 调参），支持常规（非模型）优化路径。提供 PyQt5 图形界面与 CLI 两类接口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单/多目标（不）约束治疗计划优化，默认 SciPy L-BFGS-B
- 24 类剂量-体积与结果预测模型优化组件
- 7 种可定制内部预测模型（决策树/神经网络/随机森林等）
- PyQt5 GUI：计划编辑、CT/剂量预览、DVH 评估

## 适用场景

- 科研中进行基于结果预测模型的治疗计划优化实验
- 导入 DICOM 患者数据做剂量统计分析与 DVH 评估
- 用 TG-119 等标准测试体模学习与开发计划优化流程

## 场景标签

 · 领域:医疗/放射治疗

## 证据(README 行号)

> L20:  pyanno4rt is a Python package for conventional and outcome prediction model-based inverse photon and proton treatm
> L67:  27-type feature catalogue for iterative (re)calculation to support model integration into optimization

## 星数曲线

```mermaid
xychart-beta
    title "pyanno4rt/pyanno4rt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-26 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `517aa4af52f2` · [字段定义](../../DATASET.md)*
