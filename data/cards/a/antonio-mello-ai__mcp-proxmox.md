# antonio-mello-ai/mcp-proxmox

⭐ 17 · Python · MIT · 推送 2026-09-21 · [GitHub](https://github.com/antonio-mello-ai/mcp-proxmox) · 个人维护

**供 AI 助手管理 Proxmox VE 集群的 MCP 服务器**

通过 Model Context Protocol 向 Claude Desktop、Claude Code、Cursor、Cline 等 AI 助手暴露 Proxmox VE 集群管理能力的 MCP 服务器。以 API Token 认证连接 Proxmox，提供约 35 个工具：节点/VM/LXC 容器发现、生命周期启停、创建/克隆/删除、备份恢复、快照、存储浏览、防火墙规则、迁移、cloud-init 配置、VNC 控制台截图与按键输入等。破坏性操作需两次 confirm 确认。限制：exec_command 需 guest agent 且不支持 LXC；控制台工具仅支持 QEMU VM，文本输入仅 US 键盘布局 ASCII。

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

- 约 35 个工具覆盖 Proxmox 集群发现、生命周期、备份、快照、防火墙、迁移与 cloud-init
- 破坏性操作采用两段式 confirm 确认机制
- 纯标准库实现的 VNC websocket 隧道，支持 VM 截图与控制台按键/文本输入
- 支持 uvx 免安装运行与 pip 安装

## 适用场景

- 用自然语言让 AI 助手创建、启停和迁移 Proxmox 上的虚拟机与容器
- homelab 环境通过对话查询集群资源、任务与监控指标
- 让 AI 在升级前打快照、出问题后回滚

## 场景标签

 · 领域:虚拟化/基础设施管理

## 证据(README 行号)

> L7: MCP server for managing Proxmox VE clusters through AI assistants like Claude, Cursor, and Cline.
> L9: Provision, manage, and monitor your entire Proxmox infrastructure through natural language. Create VMs and container

## 星数曲线

```mermaid
xychart-beta
    title "antonio-mello-ai/mcp-proxmox 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3c3518afee44` · [字段定义](../../DATASET.md)*
