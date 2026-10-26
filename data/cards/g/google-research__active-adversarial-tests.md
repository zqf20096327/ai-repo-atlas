# google-research/active-adversarial-tests

⭐ 26 · Python · 推送 2026-06-20 · [GitHub](https://github.com/google-research/active-adversarial-tests) · [官网](https://zimmerrol.github.io/active-tests/) · 组织维护

**论文官方实现：主动测试提升对抗鲁棒性评估置信度**

Zimmermann 等人 2022 年论文 Increasing Confidence in Adversarial Robustness Evaluations 的官方实现仓库。提出主动测试（active test）方法，参考实现位于 active_tests/decision_boundary_binarization.py，case_studies 目录包含复现实验结果的代码；评估各防御时使用防御作者的参考实现，仅做最小修改以集成该测试。面向科研人员，供复现论文与开展对抗鲁棒性评估研究。README 未给出安装命令或依赖说明，仓库声明非官方 Google 产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 主动测试（active test）的参考实现
- case_studies 提供论文实验复现代码
- 对被评估防御采用其参考实现并最小化集成修改

## 适用场景

- 复现论文实验结果
- 对防御方法进行对抗鲁棒性评估研究
- 在自有防御代码中集成该主动测试

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L3: This is the official repository of the paper _Increasing Confidence in Adversarial Robustness Evaluations_
> L6: The reference implementation of our proposed active test is in
> L8: and the code to reproduce our experimental findings is in case_studies. Note, that when evaluating

## 星数曲线

```mermaid
xychart-beta
    title "google-research/active-adversarial-tests 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-26 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3e231b4f1318` · [字段定义](../../DATASET.md)*
