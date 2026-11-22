# jamesrosing/your-procedure-is-denied

⭐ 3 · TypeScript · Apache-2.0 · 推送 2026-11-06 · [GitHub](https://github.com/jamesrosing/your-procedure-is-denied) · [官网](https://your-procedure-is-denied.vercel.app) · 个人维护

**医生的公开档案：医疗AI申诉起草实测与LITMUS标准**

一位外科医生的公开记录仓库：收录保险公司AI拒赔的公开案例时间线、其发布的LITMUS医疗AI标准（Zenodo两篇论文，CC BY 4.0），以及用三个Meta模型起草拒赔申诉信的评测。核心机制是fail-closed确定性校验门，对草稿中每条引文、数字、日期逐句核对病历；50例合成拒赔基准显示无伪造引文、8,602项注入损坏全部被捕获。软件仅供医生阅读签署，不给患者建议、不自动发送。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- fail-closed确定性校验门逐句核对草稿与病历
- 50例合成拒赔基准，三个Meta模型对比评测（其中一个开放权重）
- LITMUS标准与架构论文公开发布于Zenodo（CC BY 4.0）
- 数据为纯合成数据，含分级评分键

## 适用场景

- 医生起草保险拒赔申诉信并由本人签署
- 为医疗AI生成内容设置逐句病历校验
- 研究保险AI拒赔的公开案例与监管时间线

## 场景标签

`模型评测` `AI 写作` · 领域:评测与运维

## 证据(README 行号)

> L12:  LITMUS paper DOI
> L22: This repository is the public record of one physician's attempt to change that balance: the evidence, the standard 
> L80: #### Litmus: The Admissible Set

## 星数曲线

```mermaid
xychart-beta
    title "jamesrosing/your-procedure-is-denied 星数(近 2 点)"
    x-axis ["2026-10-30", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-30 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `9e4c5efd8491` · [字段定义](../../DATASET.md)*
