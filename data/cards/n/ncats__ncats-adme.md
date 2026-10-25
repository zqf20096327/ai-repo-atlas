# ncats/ncats-adme

⭐ 43 · Python · 推送 2026-09-03 · [GitHub](https://github.com/ncats/ncats-adme) · 组织维护

**托管 ADME 性质 QSAR 预测模型的 Web 应用（NCATS）**

美国 NCATS 维护的药物 ADME（吸收/分布/代谢/排泄）性质预测应用：内置 QSAR 模型覆盖人/大鼠肝微粒体稳定性、PAMPA 渗透性、溶解度、肝细胞质稳定性及 CYP2C9/2D6/3A4 抑制等终点，面向药物化学与药代动力学研究场景。采用 client/server 结构，依赖 chemprop 作为子模块；模型首次运行时从 NCATS 服务器加载（也可手动下载）。本地部署需 conda 创建环境后运行 app.py，经浏览器访问 127.0.0.1:5000。

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

- 覆盖肝微粒体稳定性、PAMPA 渗透性、溶解度、CYP450 抑制等多个 ADME 终点的 QSAR 模型
- 模型可从 NCATS 服务器在线加载，也可离线下载
- client/server 结构，基于 chemprop 子模块
- 提供 Windows/Mac/Linux 的 conda 环境配置步骤

## 适用场景

- 预测候选化合物的 ADME 性质以辅助药物筛选
- 在本地部署并复现 NCATS 的 QSAR 预测模型
- 批量评估化合物的 CYP450 抑制与溶解度等性质

## 场景标签

 · 领域:药物研发/计算化学

## 证据(README 行号)

> L3: This repository contains the code for the application ADME@NCATS which hosts QSAR models for different ADME endpoint
> L22: - Human Liver Microsomal Stability

## 星数曲线

```mermaid
xychart-beta
    title "ncats/ncats-adme 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-25 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `8c46aa74e1e9` · [字段定义](../../DATASET.md)*
