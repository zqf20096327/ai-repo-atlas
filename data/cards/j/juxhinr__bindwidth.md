# juxhinr/bindwidth

⭐ 112 · JavaScript · MIT · 推送 2026-08-02 · [GitHub](https://github.com/juxhinr/bindwidth) · [官网](https://juxhinr.github.io/bindwidth/) · 个人维护

**面向私有化本地 LLM 部署的约束测算与 TCO 计算器**

纯前端 JavaScript 网页计算器，无构建步骤、无服务端、无遥测，全部计算在浏览器内完成。针对单一常驻文本模型，显式评估三项约束（KV 缓存内存、合并 prefill/decode 服务能力、运行时会话上限）并指出哪个约束在起作用，据此给出机器数量建议；成本侧计算 CapEx、电费（按电价与 PUE）、管理人力、支持与更换储备等。对比自有硬件、主权租赁与企业订阅三种方案，区分实测与估算数据（data/profiles.json 中的实测配置可覆盖带宽估算），可导出 Markdown 决策记录与 JSON 场景。定位为方向性敏感度估算，非采购报价。

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

- 三约束（KV 内存/服务容量/会话上限）显式评估并标出绑定约束
- 区分交互用户与自主 agent 两类负载，分别建模峰值系数
- 六个模型架构参数（含 MoE 活跃参数、投机解码等）参与测算
- 纯前端零依赖，数据以 JSON 文件维护，实测配置可覆盖估算值

## 适用场景

- 规划私有化 LLM 推理集群时确定最小硬件规模
- 对比自购、主权租赁与企业订阅三种方案的 TCO
- 导出 Markdown 决策记录供采购或架构评审留档

## 场景标签

 · 领域:LLM 基础设施/容量规划

## 证据(README 行号)

> L15: Three limits decide the technical minimum for one resident text model:
> L16: memory for the KV cache, combined prefill/decode serving capacity, and the runtime session ceiling. They are
> L21: Frontend only. No build step, no server, no database, no account, no telemetry.

## 星数曲线

```mermaid
xychart-beta
    title "juxhinr/bindwidth 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 110 --> 113
    line [111, 112, 112]
```

2026-10-18 111 → 2026-10-31 112（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7f44e54682b1` · [字段定义](../../DATASET.md)*
