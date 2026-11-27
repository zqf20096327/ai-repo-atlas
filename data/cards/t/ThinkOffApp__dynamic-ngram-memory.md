# ThinkOffApp/dynamic-ngram-memory

⭐ 15 · Python · Apache-2.0 · 推送 2026-11-13 · [GitHub](https://github.com/ThinkOffApp/dynamic-ngram-memory) · [官网](https://doi.org/10.5281/zenodo.23604600) · 组织维护

**为语言模型推理引擎提供可编辑显式笔记记忆的模块**

面向运行语言模型的开发者：通过 token n-gram、IDF 权重与主题匹配为笔记排序，将检索块按模型分词器截断后放入提示，经 HTTP 支持笔记的增改回滚擦除，并用持久日志与索引版本发布支持并发读取。仓库是 TensorFold Notes 模块的独立发布点，当前为预发布固定快照，需在固定版本的 TensorFold 宿主内运行，尚不能独立构建；擦除不构成完整隐私保证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- n-gram + IDF + 主题匹配的笔记检索与 token 上限适配
- HTTP 接口支持笔记的添加、修改、回滚与擦除
- 持久变更日志与索引版本发布支持并发读者
- 随附论文测量数据、Lean 规则册与测试套件

## 适用场景

- 给本地推理引擎接入可编辑的外部笔记记忆
- 维护多 agent 团队共享的持久化笔记与变更日志
- 复现论文中的 memory benchmark 与擦除实验

## 场景标签

`RAG` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L13: Explicit, editable memory for language models: retrieve relevant notes using token n-grams, place a bounded block i
> L17: This is the Notes module created by Petrus Pennanen and the ThinkOff team for TensorFold. This repository is its se


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `5da08d897506` · [字段定义](../../DATASET.md)*
