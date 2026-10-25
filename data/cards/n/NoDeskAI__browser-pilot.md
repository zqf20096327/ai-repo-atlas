# NoDeskAI/browser-pilot

⭐ 37 · Python · Apache-2.0 · 推送 2026-09-22 · [GitHub](https://github.com/NoDeskAI/browser-pilot) · 组织维护

**为 AI Agent 提供隔离远程浏览器会话的基础设施**

每个浏览器会话运行在独立 Docker 容器中，包含 Chrome、Selenium WebDriver、反检测 stealth（指纹伪装、拟人输入）与 noVNC 实时查看，通过 REST API、零依赖 CLI（bpilot）或内置 Web UI 控制。面向 AI Agent 集成设计：CLI 支持 --json 机器可读输出，浏览器操作返回含执行/副作用/审计状态的 agentDevice 契约，副作用命令需独占 DeviceLease；目前仅支持 Device Governance Level 1，不支持控制转移与人工接管。支持设备预设（桌面/移动模拟）、Clash/OpenVPN 网络出口配置与 S3 兼容文件存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每会话独立 Docker 容器：Chrome + Selenium + 反检测 stealth + noVNC
- REST API / CLI / Web UI 三种控制方式，CLI 输出 --json 供 Agent 读取
- agentDevice 契约返回 executionStatus/sideEffectStatus/auditStatus 等状态，副作用命令需独占 DeviceLease
- 网络出口可在 Direct/Clash/OpenVPN 间切换，支持桌面与移动设备模拟

## 适用场景

- 为 AI Agent 提供可审计的隔离浏览器运行环境
- 需要反检测浏览能力的自动化任务执行
- 实时观看和调试 Agent 的浏览器操作

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: Remote browser automation for AI Agents. Each session runs in an isolated Docker container with Chrome, Selenium, an
> L34: Install the zero-dependency `bpilot` command-line tool served by the Browser Pilot backend to drive the browser fro
> L53: For Agent integrations, open **Docs > Agent CLI Access** in the web UI. Browser Pilot exposes each Session as an Ag

## 星数曲线

```mermaid
xychart-beta
    title "NoDeskAI/browser-pilot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-25 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6837cfa05ca3` · [字段定义](../../DATASET.md)*
