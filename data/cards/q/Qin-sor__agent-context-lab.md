# Qin-sor/agent-context-lab

⭐ 41 · Python · 推送 2026-10-28 · [GitHub](https://github.com/Qin-sor/agent-context-lab) · 个人维护 · 中文 README

**量化 coding-agent 上下文管理代价的最小实验 harness**

纯 Python 标准库实现的最小 coding-agent harness，配 5 个多步任务与双层测量（约束文本存活探针 + 行为层检查器），对 compaction / 工具结果清除 / 保约束摘要三种上下文策略做消融实验；另含 default-FAIL 验收器实验（拦截虚假完成）与 KV-cache 前缀设计对照实验。后端支持 OpenAI 兼容 API（DeepSeek/OpenAI/Kimi/Qwen）及零成本 MockLLM 自测。作者明确声明多项诚实边界：行为违规率 0%、任务规模刻意做小、run_python 无网络隔离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三种上下文策略消融：约束文本存活率 8%→83%（保约束摘要修复）
- default-FAIL 验收器：只用可观测证据，拦截 2/2 虚假完成、零误拦
- KV-cache 前缀对照：易变信息位置不同导致命中率 21% vs 90%
- 纯标准库零第三方依赖，MockLLM 端到端自测

## 适用场景

- 研究 compaction 后初始指令丢失的量化影响
- 为长程 agent 设计约束保留的摘要 prompt
- 验证 agent 完成声明是否属实（产物/过程/越界检查）
- 优化 harness 的 prompt 缓存前缀设计以降低成本

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: **最小 harness**（`harness/`，纯标准库、零第三方依赖）：
> L23: **双层测量**是本实验的关键设计——每条约束同时有：
> L72: 把长程实践中的双 Agent 监督协议泛化成可插拔组件 `harness/verifier.py`：**完成声明不算证据**，每条证据默认判失败，只用可观测证据（产物检查 / 从输入独立重算 / 测试重跑 / 工具调用审计），不接

## 星数曲线

```mermaid
xychart-beta
    title "Qin-sor/agent-context-lab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-30 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4d5c44303cef` · [字段定义](../../DATASET.md)*
