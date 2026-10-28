# Zhuang-Zhuang-Liu/DeepUplift

⭐ 27 · Jupyter Notebook · 推送 2026-04-14 · [GitHub](https://github.com/Zhuang-Zhuang-Liu/DeepUplift) · 组织维护 · 中文 README

**PyTorch 深度学习异质处理效应/uplift 建模库**

基于 PyTorch 的深度学习 uplift 建模项目，实现 TarNet、CFRNet、DragonNet、DESCN、EFIN、CEVAE、GANITE 等 10 余种异质处理效应估计模型，提供 model.fit()/model.predict() 的 sklearn 风格调用方式。附 QINI/AUUC 曲线等评估指标、倾向得分匹配（PSM）、训练器与 TensorBoard 可视化工具。面向做因果推断与营销增益建模的开发者/科研用户，要求 Python 3.8-3.11，依赖通过 pip 指定版本安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 10 余种深度 uplift 模型（TarNet/CFRNet/DragonNet/DESCN/EFIN/CEVAE/GANITE 等）
- model.fit()/model.predict() 风格 API
- QINI/AUUC 曲线与因果效应评估指标
- 提供 PSM、模型训练器与 TensorBoard 可视化工具

## 适用场景

- 营销场景估计个体处理效应，定位增益人群
- 复现与对比多种深度 uplift 模型
- 用 QINI/AUUC 曲线评估 uplift 模型表现

## 场景标签

 · 领域:因果推断/机器学习库

## 证据(README 行号)

> L4: DeepUplift is a **PyTorch-based** project of deep-learning heterogeneous causal effect models along with common eval
> L29: - Evaluation Metrics：
> L30:  - ✅ QINI/AUUC Curves

## 星数曲线

```mermaid
xychart-beta
    title "Zhuang-Zhuang-Liu/DeepUplift 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d24559e4be85` · [字段定义](../../DATASET.md)*
