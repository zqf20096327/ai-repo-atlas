# anahata-os/anahata-asi

⭐ 28 · Java · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/anahata-os/anahata-asi) · [官网](http://asi.anahata.uno) · 个人维护

**纯 Java 的气隙 ASI/AGI 容器与 agent 运行时**

面向 Java 企业环境的自托管 agent 执行容器：提供会话级 AGI 容器（CwGC 上下文窗口垃圾回收、模型生成 Java 代码的 JIT 执行与子优先类加载、Kryo 二进制序列化与零丢失恢复、PENDING 状态的人工审批工具执行），并内置跨 23 个工具包的 160 个工具（NetBeans 集成、屏幕/音频、Chromium/Firefox 自动化）。模型接入通过适配器模块支持本地 Ollama/vLLM 及 Gemini、OpenAI、Anthropic、DeepSeek、HuggingFace 等云端端点。交付形态含 Swing 桌面应用、NetBeans 插件（IntelliJ 插件开发中），经 Maven Central 分发。人类使用 Apache 2.0，另设面向 AI 的 Anahata ASL 108 许可并出售企业 SLA。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CwGC 上下文窗口垃圾回收与 JIT 执行模型生成的 Java 代码
- Kryo 事务级序列化与零丢失状态恢复（Flight Recorder）
- 工具执行以 PENDING 暂存，支持人工审查、改参与授权（HITL）
- 23 个工具包共 160 个工具，含 NetBeans IDE 集成与浏览器自动化

## 适用场景

- 在完全离线/气隙环境运行自有 agent 会话并保留状态
- 在 NetBeans 内使用自主编码 agent
- 对 agent 工具调用逐条人工审批后执行

## 场景标签

`Agent 框架` `浏览器自动化` · 领域:Agent 开发

## 证据(README 行号)

> L14: Anahata is to AGI what **Tomcat** is to Web Apps or **Kubernetes** is to Containers. It is a stateful, air-gapped e
> L31: - **Universal Alliance Adapters**: Run 100% locally with Ollama/vLLM, or connect to Google Gemini, OpenAI, Anthropi
> L37: 3. **`anahata-asi-openai-compatible`**: Universal OpenAI Chat Completions wire adapter for Hugging Face, Modal, Nov

## 星数曲线

```mermaid
xychart-beta
    title "anahata-os/anahata-asi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `012ef88ebcbe` · [字段定义](../../DATASET.md)*
