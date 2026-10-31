# tenurehq/precisionMemBench

⭐ 18 · TypeScript · MIT · 推送 2026-09-17 · [GitHub](https://github.com/tenurehq/precisionMemBench) · [官网](https://tenureai.dev/benchmark) · 组织维护

**LLM 记忆系统检索基准：测精度/噪声隔离/延迟/可变性**

面向 LLM 长期记忆系统的多维检索基准，定位为暴露具体检索失败模式的诊断工具而非排行榜。基于 35 条 belief 的种子语料，测量检索精度、噪声隔离、会话轮延迟与 belief 可变性四个属性，共 89 个计分用例（77 单轮 + 12 轮级会话断言），覆盖别名解析、作用域消歧、 supersession 链排除、模糊匹配、跨用户隔离等类别。已对 mem0、zep、cognee、supermemory 等多家系统提交基线报告，用户可对自有 provider 运行并与基线对比。运行需 Node.js 20+，向量基线另需 Docker 与 Ollama 实例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 测量检索精度、噪声隔离、会话轮延迟、belief 可变性四个正交属性
- 89 个计分用例覆盖别名解析/作用域消歧/supersession 排除/跨用户隔离等 14 类
- 提供全部参考系统的逐例基线报告供直接对比
- 对三种嵌入模型做了不变性测试

## 适用场景

- 诊断我的记忆系统在检索精度与噪声隔离上的失败模式
- 对比 mem0/zep/cognee 等记忆系统的检索表现
- 验证 mid-session 更新的 belief 是否即时生效

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: PrecisionMemBench is a multi-dimensional retrieval benchmark for LLM memory systems, designed primarily as a diagnos
> L108: The benchmark contains 77 single-turn cases and 12 scored turn-level assertions across two session scenarios, for 
> L193: ## Running the benchmark

## 星数曲线

```mermaid
xychart-beta
    title "tenurehq/precisionMemBench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `834c08c2020e` · [字段定义](../../DATASET.md)*
