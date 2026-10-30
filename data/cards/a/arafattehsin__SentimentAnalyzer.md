# arafattehsin/SentimentAnalyzer

⭐ 19 · C# · MIT · 推送 2026-10-03 · [GitHub](https://github.com/arafattehsin/SentimentAnalyzer) · [官网](https://www.nuget.org/packages/SentimentAnalyzer.Core/) · 个人维护

**.NET 全离线情感分析库：多引擎、104 种语言**

面向 .NET 开发者的跨平台情感分析库，全部处理在设备本地完成、无需联网。提供四种包：Core（VADER 规则引擎，英文，<1MB）、Onnx（TinyBERT，英文，~18MB）、Onnx.Multilingual（DistilBERT，支持 104 种语言，模型约 270MB 首次使用自动下载并本地缓存）、Legacy（ML.NET 旧 API 兼容）。支持 .NET Standard 2.0/.NET 8/.NET 10/MAUI/Blazor，ONNX 模型依赖原生 C++ 库，不能在 Blazor WebAssembly 运行。通过 NuGet 安装，输出标签、分数、置信度。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种引擎可选：VADER / TinyBERT / DistilBERT（另含 ML.NET 旧 API）
- 支持 104 种语言的多语言情感分析
- 全离线设备端处理，无需联网
- 跨平台：.NET Standard 2.0 / .NET 8 / .NET 10 / MAUI / Blazor

## 适用场景

- 在移动或 IoT 应用中本地分析用户评论情感
- 社交媒体文本（含表情）与客户评价的情感分类
- 在 Blazor / MAUI 应用中集成离线情感分析而不发送数据到云端

## 场景标签

 · 领域:NLP/.NET 库

## 证据(README 行号)

> L7: **On-device (offline) Sentiment Analysis for .NET applications**
> L84: |**SentimentAnalyzer.Core**|<1MB|VADER (rule-based)|English|~80%|⚡⚡⚡⚡⚡|Mobile, IoT, speed-critical apps|
> L86: |**SentimentAnalyzer.Onnx.Multilingual**|~541MB|DistilBERT (transformer)|104 languages|~83%|⚡⚡⚡|Multilingual, highe

## 星数曲线

```mermaid
xychart-beta
    title "arafattehsin/SentimentAnalyzer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f656a088e5be` · [字段定义](../../DATASET.md)*
