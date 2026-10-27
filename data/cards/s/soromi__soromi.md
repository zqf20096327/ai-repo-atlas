# soromi/soromi

⭐ 32 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/soromi/soromi) · [官网](https://soromi.dev) · 个人维护

**AI 编程 agent 的桌面工作台：多项目终端、账号隔离与远程查看**

基于 Rust daemon + Electron 的开源桌面应用，为 AI 编程 agent CLI 提供统一运行环境：每个项目文件夹获得独立工作区、终端与账号，daemon 持有全部状态，关闭窗口后 agent 继续运行。支持 Claude Code、Codex、Grok Build 三类 provider，通过环境变量（如 CLAUDE_CONFIG_DIR、CODEX_HOME、GROK_HOME）实现多账号隔离，并借助 agent 自身 hook 事件触发通知。提供端到端加密的配对设备远程查看能力（XChaCha20-Poly1305，中继为可自部署的 Cloudflare Worker），手机客户端处于开发中未发布。macOS/Windows/Linux 提供安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每工作区独立终端、多标签并行运行多个 agent，重启后可恢复
- 通过环境变量为每个 agent 分配独立账号配置目录，实现多登录隔离
- 端到端加密中继支持远程设备接入，中继可自部署到自己的 Cloudflare 账号
- daemon 为唯一状态权威，所有 UI（桌面/移动）均为无状态 viewport

## 适用场景

- 同时管理多个项目的 AI 编程 agent，像切换 Slack 工作区一样切换
- 为工作、个人、客户账号分别运行同一 agent 且互不混淆
- 离开电脑时收到 agent 请求权限或完成的通知
- 在 Linux 服务器上安装 daemon，从手机远程查看和接管终端会话

## 场景标签

 · 领域:开发者工具/AI agent 运行环境

## 证据(README 行号)

> L165: A provider is a coding-agent CLI Soromi can run, isolate per account, and listen to. Adding one
> L174:  &nbsp; Claude&nbsp;Code
> L180:  &nbsp; Codex

## 星数曲线

```mermaid
xychart-beta
    title "soromi/soromi 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 30 --> 33
    line [31, 32, 32]
```

2026-10-18 31 → 2026-10-27 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `1051682118b2` · [字段定义](../../DATASET.md)*
