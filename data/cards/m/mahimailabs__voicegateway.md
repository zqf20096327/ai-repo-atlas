# mahimailabs/voicegateway

⭐ 54 · TypeScript · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/mahimailabs/voicegateway) · [官网](https://voicegateway.dev) · 组织维护

**LiveKit 语音 Agent 的开源观测与分析面板**

面向 LiveKit 语音通话 Agent 的自托管 profiler：从电话线/SIP 到媒体服务器、Agent 与模型，汇聚 webhooks、指标、spans 与会话上传，形成单次通话视图。提供转写检视、延迟分解（应答时间/回合等待/首 token/首音频）、用量可见性与基础设施观测，位于音频链路之外。组件为单个 Go 二进制（web 与 worker）加 Redis、Postgres、ClickHouse、S3，make up 启动六服务栈。当前为 V1 预览：自托管可用，通知与实时后端仍在建设，云端服务未上线。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 汇聚 webhooks/指标/spans/会话上传为单一通话视图
- 延迟分解：应答时间、end-of-turn 等待、模型首 token、语音首音频
- LiveKit 基础设施视图（房间、参与者、agent worker、SIP、egress/ingress）
- 单个 Go 二进制运行 web 与 worker，make up 启动六服务栈

## 适用场景

- 排查 LiveKit 语音 Agent 通话变慢或出错的具体环节
- 查看通话的转写、逐回合时间与 Agent 活动
- 自托管观测自己的 LiveKit 生产项目

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L10: VoiceGateway profiles **LiveKit voice calls from the phone line to the model**. Inspect the transcript, turn timing
> L35: **VoiceGateway stays outside the audio path.** The V1 platform joins LiveKit webhooks, server metrics, agent spans 

## 星数曲线

```mermaid
xychart-beta
    title "mahimailabs/voicegateway 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-25 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1df08f46ee62` · [字段定义](../../DATASET.md)*
