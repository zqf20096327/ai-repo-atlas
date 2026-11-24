# felhen-ai/mcp-proxmox

⭐ 19 · Python · MIT · 推送 2026-11-12 · [GitHub](https://github.com/felhen-ai/mcp-proxmox) · 组织维护

**让 AI 助手通过自然语言管理 Proxmox VE 集群的 MCP server**

一个 MCP server，将 Proxmox VE 集群操作暴露为工具供 AI 助手调用，通过 Claude Desktop、Claude Code、Cursor、Cline 接入。提供约 40 个工具，覆盖节点/虚拟机/容器查询、生命周期控制、存储浏览、VM 与 LXC 供应、备份恢复、快照、防火墙、在线迁移、模板与 cloud-init、VNC 截图与按键注入、guest agent 命令执行及指标监控。破坏性操作需二次 confirm 确认。连接需配置 Proxmox 主机地址与 API Token 三项环境变量；1.2.2+ 版本固定 mcp SDK 为 2.x 以下以规避 fastmcp 模块移除问题。

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

- 约 40 个 MCP 工具覆盖 Proxmox 查询、供应、备份、快照、防火墙、迁移等操作
- 破坏性操作要求显式 confirm=true 二次确认，首次调用返回影响警告
- vm_screenshot 通过 VNC websocket 隧道实现，仅用标准库（自实现 WebSocket + DES）
- 提供 uvx 免安装运行、pip 安装及 Docker 镜像发布

## 适用场景

- 在 Claude Desktop 里用自然语言查看和管理家庭实验室的 Proxmox 虚拟机
- 让 AI 助手批量创建、克隆、备份 VM 和 LXC 容器
- 通过对话截取 VM 控制台画面或在控制台输入按键排查启动问题
- 查询集群节点资源、存储占用与近期任务状态

## 场景标签

 · 领域:基础设施管理/运维

## 证据(README 行号)

> L7: MCP server for managing Proxmox VE clusters through AI assistants like Claude, Cursor, and Cline.
> L9: Provision, manage, and monitor your entire Proxmox infrastructure through natural language. Create VMs and container

## 星数曲线

```mermaid
xychart-beta
    title "felhen-ai/mcp-proxmox 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-14", "2026-11-24"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-11-08 18 → 2026-11-24 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `5ebc9b411b11` · [字段定义](../../DATASET.md)*
