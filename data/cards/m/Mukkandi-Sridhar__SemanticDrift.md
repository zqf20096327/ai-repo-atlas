# Mukkandi-Sridhar/SemanticDrift

⭐ 10 · Python · CC-BY-4.0 · 推送 2026-11-25 · [GitHub](https://github.com/Mukkandi-Sridhar/SemanticDrift) · 个人维护

**MCP 工具描述措辞变化对 LLM agent 评测排名影响的预注册研究**

针对 IBM AssetOpsBench MCP 工具的预注册实证研究：将同一批 36 个工具的 9 种描述目录（含安慰剂副本、改写、历史版本）发给 10 个模型与 152 条任务，记录 38,304 次工具选择决策，分析总体准确率、排行榜排名与单次决策的漂移。仓库提供数据集、实验运行器与打分分析代码；实验假设与分析在采集数据前固定并登记。重跑需 OpenAI 与 OpenRouter API key；每次试验只计首个动作，不执行任何工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC-BY-4.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 38,304 次工具选择决策覆盖 10 个模型与 9 种描述目录
- 安慰剂目录（字节级相同副本）用于测量运行间噪声基线
- 42 条从 git 历史恢复的开发者原始描述数据集
- 预注册文档、决策日志与 FINDINGS.md 完整结果

## 适用场景

- 评估 LLM benchmark 排名对工具描述措辞的稳定性
- 复现或扩展 agent 工具选择评测实验
- 研究改写工具描述对小型模型写操作行为的影响

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L4: A pre-registered study on the MCP tools of IBM AssetOpsBench,
> L43: |`datasets/tools/`|The 36 tools (29 read, 7 write) and the 9 description catalogs|
> L91: The hypotheses, metrics and analysis were fixed before any data was collected


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `b7c71e222a3a` · [字段定义](../../DATASET.md)*
