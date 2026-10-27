# callstackincubator/evals

⭐ 112 · TypeScript · MIT · 推送 2026-09-30 · [GitHub](https://github.com/callstackincubator/evals) · [官网](https://rn-evals.vercel.app) · 组织维护

**评测编码模型解决真实 React Native 任务的基准套件**

由 Callstack 孵化器维护的基准测试集：包含 134 个评测项，按动画、异步状态、Expo Router/SDK/UI、列表、导航、React Native API、Skia 等 9 组组织。每项评测定义固定任务上下文与可判定需求，用 runner 调用模型生成实现，再用 judge 模型基于文件级证据对照需求打分，按需求结果加权计算单项得分与汇总指标。通过 bun 运行，求解与评审在 Docker 中执行，方法学详见白皮书。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 134 个评测项，按 9 个 React Native 生态分组组织
- runner/judge 流程：模型生成实现，judge 按需求与文件证据打分
- 支持 --agent-logs 与 --verbose 调试输出
- 评测方法学与评分细节有白皮书文档

## 适用场景

- 对比编码模型在真实 React Native 任务上的表现
- 为新模型或 agent 做基准评测打分
- 为常用生态库贡献或申请新评测项

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A benchmark suite for evaluating how coding models solve real React Native tasks.
> L41: The benchmark evaluates model-generated React Native implementations using requirement-based assessment. Each eval 

## 星数曲线

```mermaid
xychart-beta
    title "callstackincubator/evals 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 110 --> 113
    line [111, 112, 112]
```

2026-10-18 111 → 2026-10-27 112（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `6227f18855a7` · [字段定义](../../DATASET.md)*
