# SamurAIGPT/pixelrelay

⭐ 19 · Python · NOASSERTION · 推送 2026-08-02 · [GitHub](https://github.com/SamurAIGPT/pixelrelay) · 组织维护

**自托管生成式媒体统一网关：跨35+模型路由任务**

面向开发者的开源（Apache 2.0）自托管 API 网关，用单一 webhook 优先端点统一接入 Fal、Replicate、OpenAI、Google AI Studio 等图像/视频生成提供商，自带密钥（BYOK），无计费层。核心机制：任务状态持久化（SQLite/Postgres，重启可恢复）、提供商故障自动冷却与切换、35+ 已验证模型注册表、对应用回调的 HMAC-SHA256 签名。同步型提供商（OpenAI/Google）以后台任务桥接为 webhook 形态。提供 Docker 与 pip 安装，另含进程内轮询的库模式（README 标注不建议生产使用）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一异步端点跨多个提供商路由生成任务，webhook 回调免轮询
- 任务状态 DB 持久化，支持重启恢复与多副本共享
- 提供商故障自动冷却与透明切换
- 35+ 图像模型注册表，slug 经提供商页面验证

## 适用场景

- 应用统一接入多家图像生成 API 并自带密钥
- 生产环境获得持久任务与自动故障切换
- 用 webhook 接收生成结果而无需客户端轮询
- 脚本/笔记本中用库模式直接调用生成

## 场景标签

`模型网关` `图像生成` `视频生成` · 领域:Agent 开发

## 证据(README 行号)

> L8: **Route AI image and video generation across 35+ models with one webhook-native, BYOK API. Self-hosted, open source.
> L44: |**Unified API**|One endpoint, one auth header — talks to Fal, Replicate, and (soon) RunPod, Stability, Runway. Sam

## 星数曲线

```mermaid
xychart-beta
    title "SamurAIGPT/pixelrelay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bfdac091e128` · [字段定义](../../DATASET.md)*
