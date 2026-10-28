# BerriAI/ai-gateway-bench

⭐ 20 · Python · MIT · 推送 2026-10-09 · [GitHub](https://github.com/BerriAI/ai-gateway-bench) · 组织维护

**AI 网关开销的可复现基准测试：测量网关叠加在 LLM 之上的延迟与资源成本**

面向 AI 网关的基准测试工具：所有被测网关指向同一个本地确定性 Rust mock 上游，用『经网关延迟 − 直连延迟』公式剥离供应商延迟与网络噪声，剩余即网关自身开销。场景覆盖流式 TTFT、工具调用延迟、大上下文开销、并发下 p99 尾延迟、密钥洪泛拒绝、故障切换开销、队头阻塞与内存采样；另设 OpenRouter 真实模型单独场景。结果图表由提交的 CSV 生成，禁止硬编码数值。

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

- 确定性 mock 上游 + 直连基线的开销差值公式
- 8 类面向 agent 场景的指标（TTFT/工具调用/大上下文/并发尾延迟等）
- 成本估算模型：由 CPU、峰值 RSS 与吞吐推算每百万请求美元
- 图表由提交 CSV 生成，脚本禁止硬编码数值

## 适用场景

- 为编码 agent 选型 AI 网关前比较开销
- 验证网关在高并发下尾延迟与内存是否漂移
- 了解各网关流式 TTFT 与故障切换路径的实际成本

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A reproducible benchmark for **AI-gateway overhead**: the latency, memory, and resource cost a gateway adds on top o
> L11: Gateways compared: LiteLLM (Rust), LiteLLM (Python v1), Portkey, Bifrost, and OpenRouter (hosted, real-model scenar
> L37: Each scenario is one folder under `scenarios/`. Load/streaming scenarios use Locust; the rest are plain Python scri

## 星数曲线

```mermaid
xychart-beta
    title "BerriAI/ai-gateway-bench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e550099c9ca8` · [字段定义](../../DATASET.md)*
