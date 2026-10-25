# ddong8/openclaw-kasmvnc

⭐ 39 · Shell · MIT · 推送 2026-05-07 · [GitHub](https://github.com/ddong8/openclaw-kasmvnc) · [官网](https://claw.ihasy.com) · 个人维护 · 中文 README

**OpenClaw + KasmVNC 容器化一键部署：浏览器远程桌面运行 Agent**

为 OpenClaw agent 提供一键容器化部署方案：Docker 镜像或 PowerShell/Bash 脚本安装，内置 KasmVNC 浏览器访问的 XFCE 桌面，可实时观看 OpenClaw 操作 Chromium；通过 systemctl shim 支持容器内 gateway 重启与热升级，内置 Docker-in-Docker（可禁用）与 GPU 自动检测，预装 VS Code、Git、Node.js 22 等工具。面向需要可视化调试与大规摸部署 OpenClaw 的开发者，跨 Windows/macOS/Linux。

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

- systemctl shim 实现容器内 gateway 重启/热升级，无需重建镜像
- KasmVNC 浏览器 XFCE 桌面，可实时观察 Agent 操作浏览器
- Docker-in-Docker（可禁用换 non-privileged 模式）与 GPU 自动检测
- 中文脚本含国内优化镜像，支持代理与大规模部署

## 适用场景

- 一键部署带可视化桌面的 OpenClaw 运行环境
- 实时观察和调试 agent 的浏览器操作
- 标准化容器方式批量部署 OpenClaw 实例

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L13: **Solves the core limitation of official OpenClaw Docker deployment:**
> L34: **This project provides a complete desktop environment:**
> L78: - **One-click deploy** -- install, upgrade, and restart via a single script + Compose

## 星数曲线

```mermaid
xychart-beta
    title "ddong8/openclaw-kasmvnc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-25 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `4904fa5f7269` · [字段定义](../../DATASET.md)*
