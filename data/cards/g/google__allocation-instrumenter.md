# google/allocation-instrumenter

⭐ 491 · Java · Apache-2.0 · 推送 2026-08-05 · [GitHub](https://github.com/google/allocation-instrumenter) · 组织维护

**Java 字节码插桩库：记录程序中每次对象分配并回调**

基于 java.lang.instrument API 与 ASM 的 Java agent，通过改写字节码对 Java 程序中的每处对象分配进行插桩，在每次分配时调用用户定义的回调。使用方式为实现 Sampler 接口并传给 AllocationRecorder.addSampler()，可获取分配对象计数、类描述、对象与大小；另支持对指定类的构造器插桩（ConstructorInstrumenter.instrumentClass）。以 Maven Central 依赖形式发布，面向需要在 Java 程序中做内存分配分析或监控的开发者。

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

- 对每处对象分配插桩并触发用户回调
- Sampler 回调提供对象计数、类描述、对象与大小信息
- 支持对指定类的构造器插桩（ConstructorCallback）

## 适用场景

- 分析 Java 程序的对象分配行为与内存热点
- 在分配发生时执行自定义监控或采样逻辑
- 跟踪特定类（如 Thread）的构造调用

## 场景标签

 · 领域:Java 开发工具/性能分析

## 证据(README 行号)

> L1: The Allocation Instrumenter is a Java agent written using the [java.lang.instrument][] API and
> L2: [ASM][]. Each allocation in your Java program is instrumented; a user-defined callback is invoked

## 星数曲线

```mermaid
xychart-beta
    title "google/allocation-instrumenter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 490 --> 492
    line [491, 491]
```

2026-10-18 491 → 2026-10-30 491（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `181b35c9d55d` · [字段定义](../../DATASET.md)*
