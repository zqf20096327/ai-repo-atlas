# eaims/EAIMS

⭐ 15 · Python · NOASSERTION · 推送 2026-09-12 · [GitHub](https://github.com/eaims/EAIMS) · [官网](https://eaims.org) · 个人维护

**企业 AI 成熟度评估的开放标准与可执行参考实现**

面向企业的开放、厂商中立的 AI 成熟度标准：8 个维度、30 项能力、5 级成熟度、206 项规范化要求与 G0–G3 门控；1.1 版增加对抗与代理治理覆盖层（9 项 ADV 要求、特权代理凭据、爆炸半径等控制）。附带 Python 参考实现，验证结构化评估、评估证据与门控，产出确定性结果与报告；另提供三个合成参考案例与 Docker 验证器。标准自述为 field-informed 而非 field-validated，不构成认证或合规声明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 8 维度 / 30 能力 / 5 成熟度级别 / 206 项规范化要求的标准体系
- 1.1 版新增对抗与代理治理（ADV）要求及 G3 门控扩展
- Python 包执行评估（validate-fixture/assess/review），产出确定性结果
- Docker 验证器以最小权限容器配置运行

## 适用场景

- 企业开展 AI 成熟度自评估并定位整改项
- 治理团队审计 AI 自主权边界与人类问责保留决策
- 对标规范要求建立 AI 治理与风控体系

## 场景标签

 · 领域:AI 治理/企业评估标准

## 证据(README 行号)

> L3: > An open, vendor-neutral, evidence-grounded and executable framework for assessing and improving enterprise AI matu
> L20: - **8 dimensions** and **30 capabilities**
> L41: The Python package validates structured assessments, evaluates evidence and requirements, applies anchor eligibilit

## 星数曲线

```mermaid
xychart-beta
    title "eaims/EAIMS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3a0ca2ab782b` · [字段定义](../../DATASET.md)*
