# rajfirke/provena

⭐ 19 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/rajfirke/provena) · [官网](https://rajfirke.github.io/provena) · 个人维护

**面向 AI agent 的上下文治理库：防篡改审计与合规**

为 AI agent 上下文输入层提供治理的 Python 库：通过 ContextTrail 装饰器为每次检索调用记录 SHA-256 内容哈希、哈希链式防篡改审计记录（支持 HMAC 签名）、来源验证与新鲜度检查；提供 LOG/WARN/BLOCK 三级策略引擎，BLOCK 级在记录持久化后抛出 PolicyViolation。支持 LangChain、LlamaIndex、CrewAI、AutoGen、OpenAI Agents SDK、Google ADK 六个框架适配器与 OpenTelemetry 导出，CLI 可校验链完整性并生成 EU AI Act 合规 PDF 报告。核心包零依赖，需 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SHA-256 哈希链审计记录，支持 HMAC 签名与链完整性校验
- 来源验证、新鲜度检查与 LOG/WARN/BLOCK 策略引擎
- 6 个框架适配器（LangChain/LlamaIndex/CrewAI/AutoGen/OpenAI Agents/Google ADK）
- EU AI Act 合规映射与 PDF 合规报告生成

## 适用场景

- 为 RAG 或多 agent 系统的检索上下文建立可审计的溯源记录
- 在受监管场景下满足 EU AI Act 的日志留存与数据谱系要求
- 通过 BLOCK 策略拦截不可信或过期的数据源进入 agent 上下文

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L17: Provena adds tamper-evident audit trails to any AI agent's context pipeline — in one decorator:
> L58: pip install provena[langchain]     # LangChain callback
> L59: pip install provena[llamaindex]    # LlamaIndex postprocessor

## 星数曲线

```mermaid
xychart-beta
    title "rajfirke/provena 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-28 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e11163a7d077` · [字段定义](../../DATASET.md)*
