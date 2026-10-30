# christopherkarani/Terra

⭐ 19 · Swift · Apache-2.0 · 推送 2026-06-16 · [GitHub](https://github.com/christopherkarani/Terra) · [官网](https://christopherkarani.github.io/Terra/) · 个人维护

**Swift 遥测 SDK：追踪 Apple 平台 AI 推理并导出 OpenTelemetry**

面向 Swift 开发者的遥测 SDK，将 AI 工作流（推理调用、工具执行、流式生成、嵌入、安全检查）转为 OpenTelemetry trace，可导出到 Jaeger/Grafana/Honeycomb 等收集器，或用内嵌本地 OTLP 服务器浏览。提供 CoreML、MLX、Apple Foundation Models 的零代码/一行自动埋点，以及 GPU/内存/热/功耗/ANE 等系统性能分析器，用于调试硬件状态对模型推理的影响。支持 macOS 14+/iOS 13+ 等平台，另暴露 C ABI 与 Rust/Python/Kotlin 等绑定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 工作流转为 OpenTelemetry trace，可导出任意 OTLP 后端或本地浏览
- CoreML/MLX/Foundation Models 的零代码与一行自动埋点
- Metal/系统内存/热/功耗/Apple Neural Engine 性能分析器
- @Traced 宏与 TerraMLX.traced 等多层级埋点方式

## 适用场景

- 调试 iOS/macOS 端上 AI 应用的延迟、token 消耗与工具调用序列
- 分析设备硬件状态（GPU/内存/热/ANE）对模型推理的影响
- 将端上 AI 遥测接入 Jaeger/Grafana 等现有可观测体系

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5: Terra is a Swift-native telemetry SDK that traces AI workflows — inference calls, tool executions, streaming generat
> L133: |**1. Zero-code**|`try await Terra.start()`|CoreML predictions, HTTP AI API calls|

## 星数曲线

```mermaid
xychart-beta
    title "christopherkarani/Terra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d091ca2458d9` · [字段定义](../../DATASET.md)*
