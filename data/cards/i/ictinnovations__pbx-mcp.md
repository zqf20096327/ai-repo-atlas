# ictinnovations/pbx-mcp

⭐ 19 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/ictinnovations/pbx-mcp) · [官网](https://ictinnovations.com) · 组织维护

**让 AI 助手检查与控制 Asterisk/FreeSWITCH 的 MCP 服务器**

由 ICT Innovations 开发的 MCP 服务器，通过 AMI/ESL 协议连接 Asterisk 与 FreeSWITCH，向 MCP 客户端（如 Claude Desktop）暴露 12 个只读工具（通道、SIP 注册、中继状态、拨号计划查询等），另有 4 个写工具（ originate/hangup）需设置 PBX_MCP_ALLOW_WRITE=true 才注册，以及 6 个可选的 Asterisk 中继/分机开通工具。默认只读，CLI/API 命令按允许前缀列表过滤，屏蔽 shell 元字符与 AMI 头注入，输出截断至 2 万字符。要求 Node 18+，支持 npm 安装、npx 运行与 Docker 镜像，全部配置经环境变量传入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Asterisk/FreeSWITCH 双引擎各 6 个只读工具，按配置自动注册
- 写工具（originate/hangup）默认不注册，需显式开启 PBX_MCP_ALLOW_WRITE
- 命令允许前缀白名单、AMI 头注入防护、输出 2 万字符截断
- 可选的 Asterisk PJSIP 中继/分机开通工具（独立开关，仅操作 mcp- 前缀对象）

## 适用场景

- 让 AI 助手回答'哪些分机离线'、'SIP 中继为何未注册'等运维问题
- 跨 Asterisk 与 FreeSWITCH 双系统统一查询通道与注册状态
- 在开启写模式前用 hangup preview 查看将受影响的通道范围
- 通过 AI 助手开通和管理 PJSIP 中继与 SIP 分机

## 场景标签

 · 领域:通信/电话系统运维工具

## 证据(README 行号)

> L6: An MCP server that lets an AI assistant inspect and control **Asterisk** and **FreeSWITCH**.
> L22: Twelve read-only tools, six per engine, each one described well enough that the model picks the right one without b
> L122: The same shape works for any MCP client that speaks stdio. There's a copy in `examples/claude_desktop_config.json`

## 星数曲线

```mermaid
xychart-beta
    title "ictinnovations/pbx-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d8b89a5df4e4` · [字段定义](../../DATASET.md)*
