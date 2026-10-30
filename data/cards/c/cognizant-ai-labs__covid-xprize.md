# cognizant-ai-labs/covid-xprize

⭐ 38 · Python · NOASSERTION · 推送 2026-04-14 · [GitHub](https://github.com/cognizant-ai-labs/covid-xprize) · 组织维护

**XPRIZE 疫情响应挑战赛的示例代码与参赛文档仓库**

Cognizant 维护的 XPRIZE Pandemic Response Challenge 官方起步仓库：提供参赛所需的 predict 与 prescribe API 示例实现（线性 Lasso 预测器、LSTM 预测器、zero/random/NEAT 处方器）、样本干预计划数据，以及训练好的标准预测器供处方器训练使用；README 说明本地运行步骤（Python ≥3.6 虚拟环境 + pip + Jupyter）与 XPRIZE 沙箱提交规范（predict.py/prescribe.py 命令行参数与输出格式）。Windows 不在官方支持范围。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 predict/prescribe API 的示例实现（Lasso、LSTM、NEAT）
- 附带样本干预计划（IP）数据用于测试提交
- 提供训练好的标准预测器供处方器训练
- 说明 XPRIZE 沙箱提交的脚本命名与调用规范

## 适用场景

- 参赛者学习如何实现并提交预测器与处方器
- 在本地用 Jupyter 复现示例模型训练与预测流程
- 用标准预测器生成预测以训练自定义处方器

## 场景标签

 · 领域:流行病学/机器学习竞赛

## 证据(README 行号)

> L4: Welcome to the XPRIZE Pandemic Response Challenge! This repository contains what you need to get started in creating
> L8: * Sample predictors and prescriptors provided by Cognizant, in the form of Jupyter notebooks and python scripts

## 星数曲线

```mermaid
xychart-beta
    title "cognizant-ai-labs/covid-xprize 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-30 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `7dbec124bcf7` · [字段定义](../../DATASET.md)*
