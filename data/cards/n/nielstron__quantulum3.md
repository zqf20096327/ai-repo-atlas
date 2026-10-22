# nielstron/quantulum3

⭐ 149 · Python · MIT · 推送 2026-05-19 · [GitHub](https://github.com/nielstron/quantulum3) · 个人维护

**从非结构化文本中抽取数量、度量及其单位的 Python 库**

quantulum3 是 quantulum 的 Python 3 兼容分支，提供从非结构化文本中解析数量、测量值与单位的 API，输出 Quantity 对象（含原文 surface、span、数值与单位名）。内置 290+ 单位与 75 个实体，单位与实体对齐 Wikipedia URI。对相似单位（如英镑货币与质量磅）的歧义消解通过基于 Wikipedia 页面与 GloVe 词向量 k 近邻的 sklearn 分类器完成；分类器依赖需额外安装并可自行训练。支持拼写数字、区间、不确定度解析，可导出/导入 dict 与 JSON，可添加或替换自定义单位与实体，并有语言扩展机制。

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

- 从文本抽取数量并返回 Quantity 对象（surface/span/value/unit）
- 基于 GloVe k 近邻与 Wikipedia 的单位歧义消解分类器，可自行训练替换
- 内置 290+ 单位、75 实体，单位/实体对齐 Wikipedia URI
- 支持自定义单位与实体、dict/JSON 导入导出、语言扩展子模块

## 适用场景

- 从文档或对话文本中提取数量与单位并结构化
- 区分形近单位（如货币磅与质量磅）
- 把解析结果导出为 JSON 供下游处理

## 场景标签

 · 领域:NLP/信息抽取

## 证据(README 行号)

> L9: Python library for information extraction of quantities, measurements
> L11: looking units based on their *k-nearest neighbours* in their GloVe vector representation

## 星数曲线

```mermaid
xychart-beta
    title "nielstron/quantulum3 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 148 --> 150
    line [149, 149]
```

2026-10-18 149 → 2026-10-22 149（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `4b66aa2ee286` · [字段定义](../../DATASET.md)*
