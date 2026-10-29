# anahata-os/gemini-java-client

⭐ 22 · Java · Apache-2.0 · 推送 2026-10-01 · [GitHub](https://github.com/anahata-os/gemini-java-client) · [官网](http://gemini-java-client.anahata.uno/) · 组织维护

**JVM 上的自主 AI Agent 引擎：在 Java 运行时内执行代码**

纯 Java 编写的 Agent 引擎，接入 Google Gemini API，使 AI 在应用 JVM 进程内运行：通过 shell、文件、Google 搜索工具执行任务，可在运行时下载 JAR、JIT 编译并执行任意 Java 代码，支持 @AIToolMethod 注解将 Java 方法注册为 AI 可调用工具、基于 Jackson 的 POJO Schema 生成、PAYG 上下文裁剪与 Kryo 会话持久化。提供可嵌入 Swing 应用的 ChatPanel，面向 Java 开发者与 IoT 设备场景。采用面向人类为 Apache 2.0、面向 AI 为自有 ASL 的许可声明。

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

- 运行时下载 JAR、JIT 编译并在 JVM 内执行生成的 Java 代码
- @AIToolMethod 单注解将 Java 方法变为 AI 可调用工具
- PAYG v2 自然语言上下文裁剪与 Kryo 会话持久化
- 可嵌入 Swing UI（ChatPanel），支持任意 classpath

## 适用场景

- 在现有 Java 应用中嵌入自主 Agent 执行诊断、内省与文件操作
- 通过自然语言让 AI 管理上下文窗口与日志级别
- 结合 shell 与网络能力做 IoT 设备编排

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L18: The `gemini-java-client` is a pure-Java engine specially engineered to exploit the full power of the **Google Gemin
> L41: ### 1. Easy Tools: `@AIToolMethod`
> L95: - **Embeddable Swing UI**: Drop the `ChatPanel` into any Swing app.

## 星数曲线

```mermaid
xychart-beta
    title "anahata-os/gemini-java-client 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a07b7df2b5a9` · [字段定义](../../DATASET.md)*
