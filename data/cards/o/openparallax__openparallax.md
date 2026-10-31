# openparallax/openparallax

⭐ 14 · Go · Apache-2.0 · 推送 2026-07-04 · [GitHub](https://github.com/openparallax/openparallax) · [官网](https://docs.openparallax.dev) · 组织维护

**以安全架构为核心的个人 AI agent：思考与执行进程分离**

Go 实现的本地个人 AI agent，宣称遵循 Parallax 范式：LLM 推理进程不具执行能力，所有工具调用经引擎侧 Shield 四级安全流水线（YAML 策略、启发式规则、独立 LLM 评估、人工审批）评估后由引擎执行，agent 进程运行于内核级沙箱（Landlock/seccomp、sandbox-exec、Job Objects）。连接 Anthropic、OpenAI 兼容 API、Google、Ollama 等提供商，提供 69 种工具动作、语义记忆、SHA-256 审计链与多消息渠道。以单一静态二进制分发，零运行时依赖、零 CGo。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 认知-执行分离：推理进程与特权引擎进程分离，经 gRPC 通信
- 4 级 Shield 安全流水线，全部 fail-closed
- 内核级沙箱隔离（Landlock/seccomp、sandbox-exec、Job Objects）与 SHA-256 哈希链审计
- 各模块为独立 Go 包，提供 Python/Node.js JSON-RPC 桥接

## 适用场景

- 在本地机器上运行带强制安全层的 AI agent 执行文件、git、shell 等操作
- 处理敏感数据时要求 agent 即使被完全攻陷也无法直接执行动作
- 将 Shield、Sandbox、Audit 等安全模块引入自己的项目

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: A personal AI agent where the LLM is structurally incapable of executing anything. Every action is proposed, evaluat
> L54: OpenParallax is an AI agent that runs on your machine — under your control, with your data staying local. It connec

## 星数曲线

```mermaid
xychart-beta
    title "openparallax/openparallax 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `dc8b7264afe3` · [字段定义](../../DATASET.md)*
