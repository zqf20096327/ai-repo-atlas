# SuperdeMan/cockpit-agent

⭐ 26 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/SuperdeMan/cockpit-agent) · 个人维护 · 中文 README

**云边协同的智能座舱 AI Agent 系统，语音入口办车控与出行任务**

面向智能座舱的 Multi-Agent 系统：端侧 T0 快路径毫秒级执行车控与媒体指令（离线可用、零 LLM），云端 Planner 将复杂请求规划为 DAG 或有界 Agentic 循环，由 14 个声明式接入的领域 Agent（导航、行程、充电、深调研、车书 RAG 等）执行。LLM 只产意图与计划，确定性 Executor 经权限、能力契约与 VAL 下发车控，写操作有持久准入与一次性确认绑定。提供座舱 HMI 与 Android 陪伴端两个客户端，S2S 全双工语音、声纹区分乘员记忆。当前为 Phase 1 工程化 PoC，车控由模拟 VAL 验证，未接实车总线。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- T0/T1/T2 三层运行模型：端侧毫秒级车控断网可用，云端 DAG 规划与有界再规划
- LLM 只负责理解与规划，车控经权限/确认/VAL 确定性执行，车态 Ed25519 签名带溯源
- Agent 声明式接入（gRPC + Manifest + Registry），新增 Agent 不改编排核心
- 一个后端大脑两个端：座舱 HMI 与 Android 陪伴端共享记忆与判据

## 适用场景

- 在座舱内用一句话完成车控、导航、多日行程与充电规划等混合任务
- 通过 Android 陪伴端在车外延续会话、记忆与提醒
- 借鉴其规划/执行分离与确认绑定机制构建安全敏感的 Agent 系统

## 场景标签

`多智能体` `语音 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L12: > 云边协同的智能座舱 AI Agent 系统。喊一声「小舟小舟」，从毫秒级车控、多日行程与补能规划、车书问答，到商户点单和分钟级深度调研，一个语音入口办完。座舱屏上是 HMI，手机上是 Android 陪伴端「小舟随行」，两个端
> L27: 2. **快慢双系统。** 高频、确定、安全敏感的指令留在端侧（T0），毫秒级执行、断网可用；复杂、跨域、多轮的请求上云，由 Planner 一次规划成 DAG（T1）或在预算内循环再规划（T2）。一句话里混着车控和慢意图时按语义
> L206: - **LLM**：MiMo / MiniMax / DeepSeek / 通义千问四家进程内注册表，HMI 设置页运行时热切换并持久化；每个业务帧带请求级 provider/model pin；429 与流式故障分类降级、跨厂

## 星数曲线

```mermaid
xychart-beta
    title "SuperdeMan/cockpit-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-29 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2902b79f0baa` · [字段定义](../../DATASET.md)*
