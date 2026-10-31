# datacompose/datacompose

⭐ 14 · Python · MIT · 推送 2026-05-17 · [GitHub](https://github.com/datacompose/datacompose) · [官网](https://www.datacompose.io/) · 组织维护

**给数据工程师的可复制 PySpark 数据清洗转换器集**

面向使用 PySpark 的数据工程师，提供电话、地址、邮箱标准化与模糊匹配（Levenshtein、Soundex、Jaccard、n-gram、余弦相似度）等清洗转换器。核心机制为 copy-to-own：通过 CLI 将转换器代码复制进用户自己的仓库，成为可自由修改的本地代码，零外部依赖，只要 Spark 可运行即可运行，避免库更新破坏管道。以 pip 包分发，文档见 datacompose.io。本体为确定性规则代码，不含模型调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- copy-to-own：转换器代码复制到用户仓库，可自由修改删除
- 零依赖，仅依赖 PySpark 本身
- 覆盖电话/地址/邮箱标准化与多种模糊匹配算法

## 适用场景

- 在 PySpark ETL 管道中标准化脏数据字段
- 需要可审计、可改动的清洗代码而非黑盒库
- 对客户数据做模糊匹配与去重前的预处理

## 场景标签

 · 领域:数据工程/ETL

## 证据(README 行号)

> L3: PySpark transformations you can actually own and modify. No black boxes.
> L24: datacompose add phones
> L80: - **Zero dependencies** - Just PySpark code that runs anywhere Spark runs

## 星数曲线

```mermaid
xychart-beta
    title "datacompose/datacompose 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `df855d1312c0` · [字段定义](../../DATASET.md)*
