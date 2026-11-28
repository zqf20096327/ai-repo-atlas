# harshadulshan/lit-review-screener

⭐ 3 · Python · MIT · 推送 2026-10-31 · [GitHub](https://github.com/harshadulshan/lit-review-screener) · 个人维护

**用主动学习与统计停止规则筛选系统综述文献的 Streamlit 应用**

面向系统综述作者的摘要筛选工具：导入 RIS/PubMed/Web of Science/CSV 检索结果并去重后，用 TF-IDF + 主动学习（Naive Bayes、逻辑回归、线性 SVM）按相关性排序逐条呈现，每次标注后重训模型；超几何检验停止规则在 95% 置信度下达到目标召回率后提示停止，并自动生成 PRISMA 2020 流程图、方法学段落与 CSV/RIS/SVG 导出。经 27 个真实综述基准测试。单人筛选，不支持双人独立筛。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 主动学习排序：每次标注后重训并重排剩余记录
- 统计停止规则（Callaghan & Müller-Hansen 2020）给出 95% 召回率保证
- 自动填写 PRISMA 2020 流程图（SVG 可下载）与可编辑方法学段落
- 27 个真实综述基准：中位读 40% 找到 95% 相关文献

## 适用场景

- 为系统综述筛选成千上万条数据库检索记录
- 按 PRISMA 2020 规范生成筛选阶段流程图与报告文本
- 教学或评估不同排序模型与停止规则的筛查效率

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: **Screening thousands of abstracts for a systematic review, without reading all of them.**
> L103: |**Active learning**|Titles, abstracts and keywords become TF-IDF features. After every decision a classifier is r

## 星数曲线

```mermaid
xychart-beta
    title "harshadulshan/lit-review-screener 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-08 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `e942d82722ed` · [字段定义](../../DATASET.md)*
