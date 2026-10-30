# materialyzeai/matpes

⭐ 61 · Jupyter Notebook · BSD-3-Clause · 推送 2026-10-27 · [GitHub](https://github.com/materialyzeai/matpes) · [官网](http://matpes.ai) · 组织维护

**材料势能面（PES）数据集：覆盖周期表，训练机器学习原子间势**

由 Materialyze.AI 实验室与 Materials Project 发布的周期性材料势能面数据集，基于静态 DFT 计算（PBE 与 r2SCAN 泛函），通过 DIRECT 两阶段采样从 MD 结构中取样，2025.2 版含约 40 万结构并新增 Bader/DDEC6 电荷。面向训练机器学习原子间势（MLIP）的研究者。数据以 JSONL 格式经 Hugging Face datasets 分发，配套 pip 可装的 matpes 工具包支持下载、化学体系筛选与自建 MongoDB；另发布 M3GNet/CHGNet/TensorNet 架构的预训练势模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 静态 DFT 计算，提供 PBE 与 r2SCAN 两种泛函数据
- 约 40 万结构，近完整覆盖周期表，含 Bader/DDEC6 电荷（2025.2）
- JSONL 流式格式，支持 datasets.load_dataset 与 matpes CLI 下载/筛选
- 配套发布 M3GNet/CHGNet/TensorNet 预训练基础势（经 MatGL/MatCalc 使用）

## 适用场景

- 用高质量 PES 数据训练机器学习原子间势
- 按化学体系筛选 DFT 结构与能量数据
- 直接加载预训练基础势计算材料弹性等性质

## 场景标签

 · 领域:材料科学/材料信息学

## 证据(README 行号)

> L4: MatPES (Materials Potential Energy Surface) is a potential energy surface dataset with near-complete coverage of the
> L5: periodic table, designed to train foundation potentials (FPs), i.e., machine learning interatomic potentials (MLIPs)
> L6: for materials. MatPES is an initiative by the [Materialyze.AI lab] and the [Materials Project] to address

## 星数曲线

```mermaid
xychart-beta
    title "materialyzeai/matpes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-30 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7a4b80c94548` · [字段定义](../../DATASET.md)*
