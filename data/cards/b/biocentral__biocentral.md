# biocentral/biocentral

⭐ 20 · Dart · GPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/biocentral/biocentral) · [官网](https://app.biocentral.cloud/) · 组织维护

**面向生物医学数据与机器学习连接的科研平台（Web+Python API）**

Biocentral 提供连接生物医学数据与机器学习的生态系统：浏览器端集成研究环境（app.biocentral.cloud）与 Python API 两种使用方式。API 支持 mode=api 或 mode=local（本机执行），可调用蛋白质语言模型（如 Rostlab/ProstT5）生成序列嵌入。主题标签涉及蛋白质、蛋白质相互作用、active-learning 与可视化，基于 Flutter 构建。GPL-3.0 许可，子项目许可可能不同。有发表于 Journal of Molecular Biology 的论文可引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器端研究环境与 Python API 双入口
- 调用 ProstT5 等蛋白质语言模型生成序列嵌入
- 支持 local 模式在本机执行

## 适用场景

- 为蛋白质序列生成语言模型嵌入
- 在统一环境中连接生物医学数据与机器学习流程
- 在浏览器中使用集成研究环境处理生物医学数据

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L9: Biocentral provides a rich ecosystem for connecting biomedical data and machine learning.
> L27: embeddings = biocentral.embed(embedder_name="Rostlab/ProstT5", sequence_data={"Seq1": "PRTEIN"})

## 星数曲线

```mermaid
xychart-beta
    title "biocentral/biocentral 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `d3fa51826230` · [字段定义](../../DATASET.md)*
