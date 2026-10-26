# aspectrr/deer

⭐ 405 · Go · MIT · 推送 2026-04-21 · [GitHub](https://github.com/aspectrr/deer) · [官网](https://trydeer.sh/product) · 个人维护

**调试与运维 Elasticsearch 的 AI agent，沙箱验证后生成 Ansible 变更**

面向 Elasticsearch 及周边数据栈的 AI agent 工具：通过 SSH 只读受限 shell 排查集群问题，经 daemon 创建 microVM 隔离沙箱（qcow2 overlay、Cloud-init 供给服务），把脱敏后的 Kafka 数据重放到沙箱内 Redpanda 供 agent 验证修复方案，最终生成 Ansible playbook 由人工审核后应用。提供终端 TUI、MCP 集成（Claude Code/Cursor/Windsurf）、内置 19 个领域技能（ES/Kibana/安全/可观测性）。工具输出双层 PII 脱敏，沙箱默认无生产网络路由。通过 curl 脚本或 go install 安装，需 LLM API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 只读受限 shell 排查 + microVM 沙箱验证的双模式工作流
- Kafka 生产数据捕获、PII 脱敏后重放到沙箱 Redpanda
- 自动生成 Ansible playbook，人工审核后才可应用生产
- 19 个内置技能覆盖 Elasticsearch/Kibana/安全告警/SIEM 等，可从 GitHub 安装扩展

## 适用场景

- 让 agent 只读排查 ES 集群健康、分片与日志问题
- 在隔离沙箱中用真实数据形态验证 Logstash 管道修复
- 由 agent 生成并经人工审核的 Ansible 变更应用到生产
- 通过 Claude Code/Cursor/Windsurf 的 MCP 调用 deer 工具

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L10: deer.sh is an AI agent purpose-built for debugging and managing Elasticsearch and the data infrastructure around it
> L25: The agent investigates your cluster through a read-only shell, then spins up an isolated sandbox to test changes ag
> L36: |**Interactive TUI**|Natural language interface in your terminal — describe the problem, watch the agent work|

## 星数曲线

```mermaid
xychart-beta
    title "aspectrr/deer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 404 --> 406
    line [405, 405]
```

2026-10-18 405 → 2026-10-26 405（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `cfa343792782` · [字段定义](../../DATASET.md)*
