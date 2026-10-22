# AMAP-ML/Tree-GRPO

⭐ 407 · Python · Apache-2.0 · 推送 2026-01-26 · [GitHub](https://github.com/AMAP-ML/Tree-GRPO) · 组织维护 · 中文 README

**ICLR 2026 论文代码：树搜索策略强化学习训练 LLM agent**

AMAP（阿里巴巴）联合厦门大学、南方科技大学发布的论文代码库，论文被 ICLR 2026 接收。Tree-GRPO 以树搜索 rollout 策略替代独立链式 rollout，基于 ReAct 步级节点在语义定义的搜索树上采样，特点为更低的 rollout 预算与树级过程监督信号。代码基于 Search-R1 与 veRL 构建，支持 Qwen2.5 与 Llama3.2 系列模型，在多跳 QA、单跳 QA 与 web-agent QA 场景训练；需配置 conda 双环境（RL 与检索）、下载 wiki 语料与索引，通过脚本启动检索服务与训练。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 树搜索 rollout 替代链式 rollout 的 LLM agent RL 训练方法
- 基于 Search-R1 与 veRL 代码库构建
- 支持 Qwen2.5-1.5b~14b 与 Llama3.2-3b-it 模型
- 提供本地检索服务器与 Bing 搜索 API 两种检索后端

## 适用场景

- 复现论文中 Tree-GRPO 的多跳/单跳 QA 训练
- 研究者基于树搜索 rollout 开展 agent RL 实验
- 对比链式与树式 rollout 的预算与效果

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L26: We propose Tree-GRPO, adopting a tree-search rollout strategy in place of independent chain-based rollouts for LLM 
> L86: Run GRPO training with Qwen2.5-3b on multi-hop QA setting.
> L114: The codebase is built upon Search-R1 and veRL.

## 星数曲线

```mermaid
xychart-beta
    title "AMAP-ML/Tree-GRPO 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 406 --> 408
    line [407, 407]
```

2026-10-18 407 → 2026-10-21 407（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `3116fb07bd1b` · [字段定义](../../DATASET.md)*
