# johnsonfarmsus/openwebui-ab-mcts-pipeline

⭐ 16 · Python · AGPL-3.0 · 推送 2026-07-04 · [GitHub](https://github.com/johnsonfarmsus/openwebui-ab-mcts-pipeline) · [官网](http://ataary.com) · 个人维护

**为 Open WebUI 提供 AB-MCTS 推理与多模型协作的管道服务**

该项目将 Sakana AI 的 AB-MCTS（自适应分支蒙特卡洛树搜索）与多模型协作系统集成到 Open WebUI，作为可选 AI 模型对外提供 OpenAI 兼容 API。AB-MCTS 用 LLM-as-judge（1-2 个评判模型）按准确性/完整性/清晰性/相关性四准则评估候选答案，支持迭代次数与树深度配置，并记录 SQLite+JSONL 实验日志与 D3.js 树可视化。通过 docker-compose 部署约 9 个服务（含 Prometheus/Grafana 监控），依赖本地 Ollama 提供模型。已知问题：单次查询可能耗时 30-120 秒，偶发幻觉。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AB-MCTS 树搜索推理，LLM-as-judge 四准则多评判共识评估
- OpenAI 兼容 API，在 Open WebUI 中作为可选模型（ab-mcts / multi-model）
- SQLite + JSONL 运行日志与 D3.js 交互式搜索树可视化
- Prometheus 指标与 Grafana 预配置仪表盘监控

## 适用场景

- 在 Open WebUI 中用树搜索推理处理多步推理与数学证明类问题
- 让多个本地模型协作生成多视角综合回答
- 研究分析：回看每次运行的搜索树、逐节点质量评分与模型表现

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: This project implements **Sakana AI's AB-MCTS (Adaptive Branching Monte Carlo Tree Search)** algorithm and a **Multi
> L16: - **OpenAI-Compatible API**: Native integration with Open WebUI's model system

## 星数曲线

```mermaid
xychart-beta
    title "johnsonfarmsus/openwebui-ab-mcts-pipeline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bdf0400bc133` · [字段定义](../../DATASET.md)*
