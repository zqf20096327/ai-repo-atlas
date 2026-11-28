# arunangshu01/ask-the-multiverse

⭐ 3 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/arunangshu01/ask-the-multiverse) · [官网](https://multiverse.arunangshupramanik.com) · 个人维护

**漫威多元宇宙问答机器人：每个回答都附数据来源引用**

基于 Marvel Database、MCU Wiki 与 Wikidata 构建的知识图谱问答应用：覆盖 5,531 个现实、106,838 个角色、985,849 条故事出场记录。LLM 将自然语言问题转为带类型的图查询或只读 DuckDB SELECT，回答仅由查询返回的行构建，并展示所执行查询及引用的 wiki 页面与修订版本；数据无法回答时明确说明。每周 GitHub Actions 同步数据，本地运行可用规则规划器替代 LLM key。

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

- LLM 生成带类型图查询或受检只读 DuckDB SQL
- 回答仅由返回行构建并附精确页面与修订引用
- 每周自动数据同步，Coverage 页列出未收录页面及原因
- 含 80 题评测集，规则规划器与 LLM 规划器均可达 100%

## 适用场景

- 用自然语言查询漫威角色、团队与跨故事关系
- 查证某角色出场/击杀等关系对应的原始出处页面
- 学习 LLM 转图查询与 DuckDB 校验的 RAG 之外的实现方式

## 场景标签

`数据分析` `知识图谱` · 领域:效率与自动化

## 证据(README 行号)

> L24: Ask "Who has fought both Thanos and Galactus?" and an LLM turns the question into a typed graph query or a checked,
> L25: read-only DuckDB SELECT. The answer is built only from the returned rows, shows the query it ran, and links to the
> L76:  100% plan / 100% answer with the rule planner and with the LLM planner (`python -m eval.run [--llm]`).


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `899c021af790` · [字段定义](../../DATASET.md)*
