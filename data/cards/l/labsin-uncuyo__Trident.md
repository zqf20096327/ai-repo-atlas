# labsin-uncuyo/Trident

⭐ 14 · Python · MIT · 推送 2026-09-27 · [GitHub](https://github.com/labsin-uncuyo/Trident) · [官网](http://labsin.org/Trident/) · 组织维护

**评测自主 LLM 攻防 agent 的 Docker 网络靶场**

面向自主网络安全 agent 研究的容器化实验环境：将攻击方（coder56）、防御方（SLIPS IDS + 自动响应）与良性流量 agent 作为一等组件同时运行。所有流量强制经单一路由器，实现确定性全流量 PCAP 捕获；每次运行以 RUN_ID 组织，产出 JSONL 时间线、PCAP 归档与 IDS 告警日志。需配置 LLM API key（OpenAI/Anthropic/Gemini/OpenRouter 等预设），提供 Web 配置界面与 FastAPI+React 监控面板。明确警告仅限实验环境，容器带 NET_ADMIN 特权、含默认凭据且无出口防火墙。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 攻击/防御/良性三类 agent 同时运行的容器靶场
- 全部流量经单一路由器做确定性 PCAP 捕获
- 每次运行产出结构化 JSONL 时间线、PCAP 归档与 IDS 告警
- Web 配置应用支持多 LLM 提供商预设与连接测试

## 适用场景

- 评测 LLM 攻击与防御 agent 的对抗行为
- 捕获可复现实验产物供下游分析与 ML 管线使用
- 通过仪表盘实时观察靶场流量与告警

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L3: A minimal Docker-based cyber range for benchmarking autonomous LLM attack and defense agents — with deterministic fu
> L14: - **Agent-first design.** Attacker (coder56), defender (SLIPS + auto-responder), and benign traffic agents are firs
> L16: - **Reproducible experiment output.** Every run is scoped to a `RUN_ID` and produces structured JSONL timelines, ro

## 星数曲线

```mermaid
xychart-beta
    title "labsin-uncuyo/Trident 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a4c179109708` · [字段定义](../../DATASET.md)*
