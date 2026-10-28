# jmanhype/ace-playbook

⭐ 37 · Python · 推送 2026-08-11 · [GitHub](https://github.com/jmanhype/ace-playbook) · 个人维护

**自我改进的 LLM 系统：从执行反馈在线学习并维护经验手册**

基于 Generator-Reflector-Curator 模式的自改进 LLM 系统：Generator 用 DSPy ReAct/CoT 模块执行任务，Reflector 分析结果并抽取带标签的经验（Helpful/Harmful/Neutral），Curator 用 FAISS 做语义去重（0.8 余弦阈值）后写入 append-only playbook。支持分阶段发布（shadow→staging→prod）、多租户隔离、性能回归自动回滚与 Prometheus 指标。面向开发与研究人员，需配置 OpenRouter/OpenAI/Anthropic API key，提供 Docker Compose 部署与基准测试脚手架。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Generator-Reflector-Curator 循环从执行反馈在线提炼经验
- FAISS 语义去重（0.8 余弦阈值）防止上下文坍缩
- shadow→staging→prod 分阶段发布与自动回滚（<5 分钟）
- 性能预算：≤10ms P50 检索、≤+15% 端到端开销

## 适用场景

- 让 LLM agent 在线积累领域经验并避免重复错误
- 为金融等新领域 5 步添加护栏与基准数据集
- CI 中周期性跑基准以便回归立即暴露

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: Self-improving LLM system using the Generator-Reflector-Curator pattern for online learning from execution feedback.
> L11: - **Generator**: DSPy ReAct/CoT modules that execute tasks using playbook strategies

## 星数曲线

```mermaid
xychart-beta
    title "jmanhype/ace-playbook 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `409ef7fd86b8` · [字段定义](../../DATASET.md)*
