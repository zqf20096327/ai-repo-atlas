# ZiwayZhao/agent-coworker

⭐ 21 · Python · MIT · 推送 2026-04-04 · [GitHub](https://github.com/ZiwayZhao/agent-coworker) · [官网](https://ziwayzhao.github.io/agent-coworker/) · 组织维护 · 中文 README

**让 Agent 通过 P2P 安全共享 Skill 的协议：代码不传输只给结果**

基于 XMTP 网络的 Agent 协作协议与 Python 工具：一条命令把 SKILL.md 包装为远程可调用的 API，代码与 Prompt 留在本机，调用方仅拿到函数返回值。机制包括四层信任分级与权限自动降级、技能隐藏（返回"未知技能"）、XMTP 端到端加密、异步委托（对方离线时任务在网络上排队）。提供 CLI 与 Python SDK，零依赖，MIT 许可，含在线演示 Bot（icy）。与 MCP/A2A/CrewAI 做了对比表。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Skill-as-API：SKILL.md 留在本机，调用方只拿到返回值
- 四层信任分级 + OKR 结束后权限自动降级
- XMTP 端到端加密与异步委托（离线任务排队）
- 邀请码机制：可重复使用、不含密钥、不过期

## 适用场景

- 把私有方法论做成 SKILL.md 供同事远程调用而不交出代码
- 跨网络/组织的 Agent 之间点对点委托分析任务
- 收回已分享技能的访问权限，避免技能被复制扩散

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L27: 你的 Skill 跑在你的机器上。别人远程调用，只拿到结果。
> L168: ||CoWorker|MCP|A2A|CrewAI|

## 星数曲线

```mermaid
xychart-beta
    title "ZiwayZhao/agent-coworker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f0d1d52d4150` · [字段定义](../../DATASET.md)*
