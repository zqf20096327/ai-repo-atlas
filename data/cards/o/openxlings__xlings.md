# openxlings/xlings

⭐ 615 · C++ · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/openxlings/xlings) · [官网](https://index.xlings.org) · 组织维护 · 中文 README

**多版本免 root 的通用软件包基础设施，含类 OS 隔离与 Agent 接口**

面向开发者的跨平台（Linux/macOS/Windows）包管理与环境隔离基础设施：以统一 xpkg 格式从官方、第三方或自建索引安装任意版本软件，多版本并存共享负载，xlings use 切换；SubOS 提供命名环境，从 PATH 切换到无 root 沙箱（Linux 用 bwrap 隔离文件系统/进程/网络，macOS/Windows 仅隔离用户目录，非安全边界）；Luban 在其上提供整个 Linux 用户land、版本回滚与可启动镜像。内置面向 AI agent 的使用指南、XLINGS_AGENT_MODE=1 与 NDJSON 接口，并提供自检修复命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- xpkg 统一格式，多版本并存且 N 环境共享同一份负载
- SubOS 命名环境：PATH 切换到无 root 沙箱（bwrap）
- 面向 AI agent 的指南、agent 模式环境变量与 NDJSON 接口
- Luban：无 root 的完整 Linux 用户land、世代回滚、可导出镜像

## 适用场景

- 同一机器并行管理 gcc@16/gcc@11/node@24 等多套工具链
- 团队用 workspace 声明统一的项目环境版本
- 给 AI agent 或不受信代码提供隔离沙箱执行环境
- 无 root 权限下运行完整 Linux 用户land（Luban）

## 场景标签

 · 领域:开发工具/软件基础设施

## 证据(README 行号)

> L37: Using an AI agent? Tell it to run `xlings agent usage` — a complete guide
> L59: |**Agents**|`xlings subos exec`, exit codes that mean something, `XLINGS_AGENT_MODE=1`, and an NDJSON interface (`x

## 星数曲线

```mermaid
xychart-beta
    title "openxlings/xlings 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 613 --> 616
    line [614, 615, 615]
```

2026-10-18 614 → 2026-10-24 615（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `ee5d28189338` · [字段定义](../../DATASET.md)*
