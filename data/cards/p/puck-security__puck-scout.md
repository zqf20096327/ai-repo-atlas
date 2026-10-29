# puck-security/puck-scout

⭐ 24 · Go · MIT · 推送 2026-07-06 · [GitHub](https://github.com/puck-security/puck-scout) · [官网](https://puck.security) · 组织维护

**经 MCP 的端点自治调查工具：自然语言问询得出安全结论**

面向安全/事件响应团队的端点调查系统：Rust 端点代理执行只读命令，Go 编写的 MCP 服务器加载 YAML 调查技能、经策略引擎校验命令并分发至多台主机，由 Claude Code 等客户端驱动，产出含遏制建议的叙述性报告并保存为 markdown。安全模型为服务端与代理各自独立执行共享类型白名单，越界命令被拒绝；披露 EDR 可能标记代理进程，且 Free/Pro/Max Claude 账号默认用对话数据训练。MIT 许可，另有托管企业服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 工具集：启动调查、并行查询主机、保存 markdown 报告等
- 服务端与代理双重独立执行只读命令白名单策略
- 技能以 YAML playbook 形式定义，可无需写 Rust/Go 贡献
- 原生二进制覆盖 Linux/macOS/Windows（amd64+arm64）

## 适用场景

- 用自然语言对主机群做凭据暴露或入侵迹象排查
- 安全事件中并行调查多台端点并生成遏制建议报告
- 通过 Claude Code 等 MCP 客户端驱动自动化威胁狩猎

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: **Autonomous, read-only endpoint investigation via MCP.** Ask a question about your fleet in plain English; get a na
> L57: - **`mcp/`** — MCP server (Go): loads skills, validates commands against the policy engine, fans out to agents, wri

## 星数曲线

```mermaid
xychart-beta
    title "puck-security/puck-scout 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `df0c2aaec4c3` · [字段定义](../../DATASET.md)*
