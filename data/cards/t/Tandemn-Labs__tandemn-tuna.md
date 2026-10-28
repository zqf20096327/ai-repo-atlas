# Tandemn-Labs/tandemn-tuna

⭐ 25 · Python · MIT · 推送 2026-03-13 · [GitHub](https://github.com/Tandemn-Labs/tandemn-tuna) · 组织维护

**混合 GPU 路由器：用 Spot 实例省钱、Serverless GPU 加速冷启动**

面向部署 LLM 推理服务的开发者，Tuna 将廉价但启动慢、可被抢占的 Spot GPU 与秒级启动但昂贵的 Serverless GPU 组合在同一 OpenAI 兼容端点后。路由器以三态机（COLD/WARMING/READY）工作：冷启动与失败回退走 Serverless，Spot 就绪后流量全部切至 Spot，流量停止时缩容到零。支持 Modal、RunPod、Cloud Run、Baseten、Azure、Cerebrium 作为 Serverless 后端，AWS/GCP（经 SkyPilot）作为 Spot 后端，通过 pip 安装并使用 CLI 部署、监控与比价。README 自述处于实验性活跃开发阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Serverless 与 Spot GPU 的单端点混合路由，Spot 被抢占时自动回退 Serverless
- 三态机 COLD→WARMING→READY 管理冷启动与流量切换
- 支持 6 家 Serverless 提供商与 AWS/GCP Spot，自动选择最便宜方案
- CLI 覆盖部署、状态、成本面板、GPU 比价与冷启动/负载基准测试

## 适用场景

- 降低 LLM 推理服务成本：稳态流量走 Spot、冷启动走 Serverless
- 跨云 GPU 提供商比价并自动选择最便宜的部署方案
- 对延迟敏感的服务在 Spot 被抢占时无缝回退

## 场景标签

`推理引擎` `MLOps` · 领域:训练与推理

## 证据(README 行号)

> L7: Tuna is a smart router that combines both behind a single OpenAI-compatible endpoint. It serves requests from server
> L253: tuna deploy --model Qwen/Qwen3-0.6B --gpu L4 --service-name my-first-deploy

## 星数曲线

```mermaid
xychart-beta
    title "Tandemn-Labs/tandemn-tuna 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5117aa618d89` · [字段定义](../../DATASET.md)*
