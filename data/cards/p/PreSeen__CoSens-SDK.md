# PreSeen/CoSens-SDK

⭐ 17 · Python · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/PreSeen/CoSens-SDK) · [官网](https://cosens.ai) · 组织维护

**面向 Agent 开发者的 CoSens SDK：将执行记录转为可复用 Recipe**

提供 Python 与 TypeScript 双语言的 RSIClient SDK，用于把已确认的任务执行证据提交给 CoSens RSI。支持云模式（经网关，需 COSENS_RSI_BASE_URL 与 API key）和本地模式（本机 Worker + 本地 SQLite 队列 + 自备工具调用模型）。工作流：execution_create 提交上下文与文件路径，Worker 提取用户反馈与修正归因，生成 Rubrics 与 Recipe，并通过 recipe_test 在测试输入上按 Rubrics 评分验证。生成阶段可选接入 Exa 网络搜索（最多三次查询/次尝试），两套运行时需使用独立数据目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Python 与 TypeScript 双 SDK，方法与结果一致
- 云/本地双模式：网关发送或本机 Worker + SQLite 队列
- 反馈提取→归因→Recipe 生成的结构化流水线
- recipe_test 按 Rubrics 评分，未验证条件标记 unverified

## 适用场景

- 把用户修正沉淀为可复用的任务 Recipe
- 为 Agent 执行记录做证据引用与学习审计
- 本地用自己的模型运行 Worker 生成 Recipe

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: CoSens turns confirmed task evidence into reusable Recipes. The SDK is available in TypeScript and Python. Both prov
> L5: - **Cloud (default)**: `RSIClient()` sends the evidence files you name to the configured CoSens RSI gateway. Set `CO
> L9: Host Hook → SDK → (cloud service | local SQLite queue) → worker


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `d74a84ce2d86` · [字段定义](../../DATASET.md)*
