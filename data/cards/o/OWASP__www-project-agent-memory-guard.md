# OWASP/www-project-agent-memory-guard

⭐ 188 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/OWASP/www-project-agent-memory-guard) · [官网](https://owasp.org/projects/agent-memory-guard) · 组织维护

**OWASP 项目：拦截 AI agent 记忆投毒的运行时防御中间件**

位于 agent 与其记忆存储之间的检查层：对每次读写经检测器流水线（提示注入、密钥/PII 泄露、保护键篡改、大小异常、自我强化循环）与 YAML 声明式策略处理，动作包括 allow/redact/quarantine/block，并输出结构化 SecurityEvent 供 SIEM 关联。无 API key、本地运行。提供 LangChain、OpenAI Agents、AutoGen、CrewAI、mem0 集成及配套基准 amg-bench。映射 NIST AI RMF 与 EU AI Act；strict 预设在自测基准中得 D 级（缺持久化检测器）。

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

- 读写路径上的检测器流水线（提示注入/密钥泄露/保护键篡改等）+ YAML 策略（allow/redact/quarantine/block）
- SHA-256 完整性基线与快照回滚、retire_if 谓词式退役
- 四类来源标注（external_tool/user_input/agent_authored/system）与 OpenTelemetry 导出
- 附带框架中立的记忆安全基准 AMSB，可对 mem0/Letta/Zep 等评分

## 适用场景

- 在 LangChain/AutoGen/CrewAI 等 agent 的记忆读写中拦截投毒载荷
- 对现有记忆系统做投毒生命周期韧性评分
- 满足 NIST AI RMF / EU AI Act 相关合规控制映射

## 场景标签

`Agent 记忆` `网络安全` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L83: Agent Memory Guard sits between the agent and its memory store, screening every operation through a pipeline of det

## 星数曲线

```mermaid
xychart-beta
    title "OWASP/www-project-agent-memory-guard 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 187 --> 190
    line [188, 189, 189]
```

2026-10-18 188 → 2026-10-22 189（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3f3972d07e65` · [字段定义](../../DATASET.md)*
