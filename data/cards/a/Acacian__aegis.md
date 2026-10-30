# Acacian/aegis

⭐ 18 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/Acacian/aegis) · [官网](https://acacian.github.io/aegis/) · 组织维护

**AI agent 治理层：一行代码为 12 个框架注入防护栏与审计**

面向 Python AI agent 应用的治理与安全库：通过 auto_instrument() 自动探测已安装的 LangChain、CrewAI、OpenAI Agents SDK、Anthropic API、LiteLLM、Google ADK 等 12 个框架并注入钩子，提供确定性正则防护栏（提示注入、PII 检测/脱敏、提示泄露、毒性，2.65ms 冷启动/<1µs 热检查）、声明式 YAML 策略、Merkle 防篡改审计链（映射 EU AI Act/NIST AI RMF/SOC2）。另提供预生产扫描 CLI（aegis scan）、策略 CI/CD（plan/test）、多 agent 治理服务器（37 个 REST 端点）。无 LLM 调用、无网络依赖；对无阻断钩子的 SDK 采用 monkey-patch 方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- auto_instrument() 零代码改动覆盖 12 个 agent 框架
- 确定性正则防护栏：109 个注入模式 9 语言、13 类 PII，无 LLM 调用
- Merkle 链防篡改审计 + Ed25519 签名，映射 EU AI Act/NIST AI RMF/SOC2
- 策略生命周期工具：aegis scan / plan / test 与 GitHub Actions 集成

## 适用场景

- 为生产环境 agent 应用统一注入提示注入阻断与 PII 脱敏
- 在 CI 中扫描未治理的 AI 调用并做策略回归测试
- 满足合规审计要求，留存防篡改的 agent 行为记录
- 多 agent 部署下集中管理策略与审计

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5:  Aegis is to agent governance what Redis is to data structures — one runtime that unifies prompt-injection blocking,
> L39: |**2. Adapters**|Auto-instrument any framework through its own hooks|LangChain callbacks, CrewAI `BeforeToolCallHoo
> L45: aegis.auto_instrument()    # 12 frameworks governed. No other code changes.

## 星数曲线

```mermaid
xychart-beta
    title "Acacian/aegis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `dbc4e5e2a8ad` · [字段定义](../../DATASET.md)*
