# ctala/ai-benchmarks-alternativos

⭐ 14 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/ctala/ai-benchmarks-alternativos) · [官网](https://benchmarks.cristiantala.com) · 个人维护

**面向西语创业者/Agent 开发者的 LLM 西语基准测试与选型数据集**

由个人维护的西班牙语 LLM 基准测试项目：对 177 个模型（227 个编目）在推理、编码、内容营销、Agent 操作四类任务上运行 70,000+ 次测试，用本地 Phi-4（vLLM FP16 于 DGX Spark）做 LLM-as-Judge 评分。质量指数采用 0-10 绝对分，价格与延迟单独列出，Agent 能力、安全（prompt injection 抗性）、长上下文、工具调用作为独立维度。提供交互式选型计算器网站，按预算/任务/速度自定义权重筛选。声明不替代学术基准，仅作为应用场景的补充信息。代码 MIT、数据 CC BY 4.0。

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

- 177 个模型、70,000+ 次成功 run、186 个测试（31 套件）的评测数据
- Phi-4 本地 LLM-as-Judge（vLLM FP16，声明避免利益冲突）
- 质量指数为绝对分（0-10），价格/延迟独立报告不混入评分
- Agent 长程多轮、凭证泄漏抗性、可用上下文等独立维度测评

## 适用场景

- 为 N8N/Hermes 中的 Agent 选型：按质量、成本、延迟权衡模型
- 西语内容/客服等西语应用场景下比较模型表现
- 用交互式计算器按预算和任务类型筛选模型

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: Benchmark de modelos AI para emprendedores y equipos que usan agentes (N8N, Hermes). Evalua modelos en los 4 pilare
> L13: **Cobertura actual**: 177 modelos con ≥20 runs ( 227 catalogados, incluido **Claude Fable 5** medido el día 1), jue
> L112: **https://benchmarks.cristiantala.com/** — encuentra el modelo IA perfecto en 30 segundos.

## 星数曲线

```mermaid
xychart-beta
    title "ctala/ai-benchmarks-alternativos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `ec8f9ada42d6` · [字段定义](../../DATASET.md)*
