# ReclaimedNode/LLM-Super-Bench

⭐ 3 · TypeScript · MIT · 推送 2026-11-09 · [GitHub](https://github.com/ReclaimedNode/LLM-Super-Bench) · [官网](https://www.reclaimednode.com/llm-super-bench) · 个人维护

**本地 LLM 服务器同场竞技基准工具：公平计时对比推理性能**

基于 Bun 的本地模型服务器竞速基准工具，源自 NetworkChuck 的 mac-studio 项目测试框架。向两到四台运行 OpenAI 兼容服务器的机器同时发送相同提示，并排流式展示回复并生成记分板；支持提示长度与并发数扫描、图表展示、可分享的运行数据文件。附带的 lanes 命令可通过 ssh 批量启停各机器上的模型服务器，并处理 Mac 休眠唤醒。无第三方依赖，需 Bun 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 2-4 台机器同一时刻发送相同提示并排竞速
- SWEEP 模式批量扫描提示长度与流数
- bun run lanes 通过 ssh 批量启停各机器的模型服务器并按 pid 精确停止
- 运行前校验端点模型 id，图表与可分享数据文件

## 适用场景

- 对比家里多台跑本地模型机器的推理速度
- 对不同提示长度和并发数做基准扫描
- 把测试结果数据文件发给别人比较

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: Send the same prompt to two, three or four computers running local AI models at the same
> L19: - One or more computers running a local model behind an **OpenAI-compatible server**. That is the thing being teste
> L136: Two to four lanes. Any OpenAI-compatible streaming chat endpoint works

## 星数曲线

```mermaid
xychart-beta
    title "ReclaimedNode/LLM-Super-Bench 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-08 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `ef61a0312e7b` · [字段定义](../../DATASET.md)*
