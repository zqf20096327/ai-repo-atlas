# yuzawa-san/onnxruntime-java

⭐ 36 · Java · MIT · 推送 2026-10-19 · [GitHub](https://github.com/yuzawa-san/onnxruntime-java) · 个人维护

**Java 版 ONNX Runtime 绑定：基于 FFI API 运行 ONNX 模型推理**

面向 Java 开发者的 ONNX Runtime 绑定库，使用 Java 23 稳定的 Foreign Function & Memory API（Project Panama）替代 JNI，封装 C API 细节。要求最低 Java 23。通过 Maven Central 发布多个构件：纯 API 构件（不带原生库，用户可自带共享库或经 java.library.path 加载）、CPU 与 GPU(CUDA) 原生库构件（按 linux-x86_64 等 classifier 选择）。版本号由上游原生库最低版本与仓库自身版本组成，运行时校验共享库次版本兼容性。提供示例库与示例应用，运行需 --enable-native-access JVM 参数。

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

- 基于 Foreign Function & Memory API 的类型安全 Java 绑定，无需 JNI
- Maven Central 发布 CPU 与 GPU(CUDA) 原生库构件，支持 Linux/Windows/macOS 的 arm64 与 x86_64
- 版本字符串指示所支持的最低上游原生库版本并做兼容性校验
- 支持自带 onnxruntime 共享库以使用 C API 暴露的其他 execution provider

## 适用场景

- 在 Java 应用中加载并运行 ONNX 模型做推理
- 构建跨平台（Linux/Windows/macOS, arm64/x86_64）Java 推理服务
- 以自带共享库方式接入非默认的 execution provider

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: This is an **performant** and **modern** Java binding to Microsoft's ONNX Runtime which uses Java's new Foreign Func
> L9: This project's goals are to provide a type-safe, lightweight, and performant binding which abstracts a lot of the na

## 星数曲线

```mermaid
xychart-beta
    title "yuzawa-san/onnxruntime-java 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-26 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `58a0e4696d28` · [字段定义](../../DATASET.md)*
