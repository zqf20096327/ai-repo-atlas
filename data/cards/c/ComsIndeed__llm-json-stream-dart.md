# ComsIndeed/llm-json-stream-dart

⭐ 15 · Dart · MIT · 推送 2026-06-24 · [GitHub](https://github.com/ComsIndeed/llm-json-stream-dart) · [官网](https://pub.dev/packages/llm_json_stream) · 个人维护

**Dart 流式 JSON 解析库：LLM 流式响应边到边解析**

用 Dart 编写的反应式字符级 JSON 状态机库，面向在应用中消费 LLM 流式 JSON 响应的开发者。逐字符解析流式 JSON，可按路径订阅指定属性，以 stream（增量块）或 future（完整值）两种方式获取；列表与映射支持元素/属性开始解析时的回调，用于渐进式渲染 UI。提供 closeOnRootComplete 选项过滤 JSON 后的附加文本、onLog 观测回调，声称通过 504 个测试覆盖转义序列、Unicode、尾逗号、markdown 包裹等边界情况。通过 pub 依赖安装。

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

- 逐字符流式解析，按路径（含嵌套与数组下标）订阅属性
- 每个属性同时提供 stream（增量）与 future（完整值）两种 API
- closeOnRootComplete 过滤 JSON 之后的附加文本
- onLog 事件观测回调支持调试与解析可视化

## 适用场景

- Flutter/Dart 应用中流式渲染 LLM 返回的 JSON 字段
- 列表/表单类 UI 在数据生成过程中渐进式加载
- LLM 流水线中只提取 JSON 部分并跳过附加解释文本

## 场景标签

 · 领域:LLM 应用开发/解析库

## 证据(README 行号)

> L10: Parse JSON reactively as LLM responses stream in. Subscribe to properties and receive values chunk-by-chunk as they
> L20: LLM APIs stream responses token-by-token. When the response is JSON, you get incomplete fragments:
> L34: LLM JSON Stream parses JSON **character-by-character** as it arrives, allowing you to subscribe to specific propert

## 星数曲线

```mermaid
xychart-beta
    title "ComsIndeed/llm-json-stream-dart 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `aaeb220987fc` · [字段定义](../../DATASET.md)*
