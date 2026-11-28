# ranajahanzaib/interaction-cost

⭐ 3 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/ranajahanzaib/interaction-cost) · 个人维护

**从初始请求预测人-AI 对话轮次与追问概率的本地研究平台**

本地优先的研究平台：从初始 prompt 中提取 22 个确定性句法/结构信号，用 Scikit-Learn 基线模型（HistGradientBoosting，GroupShuffleSplit 防泄漏划分）预测两个目标——用户消息数与追问概率。后端 FastAPI（Pydantic 校验、批量与对比路由），分析层用 DuckDB 零拷贝查询 Parquet 数据集，前端 Next.js 提供交互式预测实验室与特征对比界面。含 CLI 管线：JSONL 对话规范化（自动脱敏邮箱/电话）、Parquet 落盘、流式拉取 WildChat-1M 等数据集、训练与留出评估。默认合成演示模式，训练后切换为本地模型推理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 22 个透明确定性特征直接从初始请求提取（词数、词汇密度、约束标记、标点比等）
- 防泄漏训练管线：GroupShuffleSplit 保证重复 prompt 不跨训练/测试集泄漏
- 双推理模式：确定性合成演示或本地拟合的 Scikit-Learn 模型（带指纹校验）
- 隐私治理：对话规范化时自动脱敏邮箱/电话、字段白名单、不持久化转录

## 适用场景

- 研究初始请求结构与后续对话轮次/追问概率的关系
- 对比两种 prompt 措辞的结构性特征差异
- 训练本地基线模型并查看留出集评估指标
- 将 WildChat 等对话数据集规范化为脱敏 Parquet 做分析

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: InteractionCost is a local-first research platform for studying how the structure of an initial user request relates
> L19: - **Dual Inference Modes**: Runs seamlessly in deterministic synthetic demonstration mode or against locally fitted
> L26: Test initial requests interactively. The laboratory predicts expected user turns and follow-up probability while re


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `b2d4ea75d1fb` · [字段定义](../../DATASET.md)*
