# besoeasy/airlock

⭐ 108 · Shell · 推送 2026-10-26 · [GitHub](https://github.com/besoeasy/airlock) · 个人维护

**用一次性 Podman 容器隔离运行代码与 AI agent 的 CLI**

Airlock 是一个 Bash 编写的单脚本 CLI，将项目放入预配置的无根 Podman 容器中运行：工作目录挂载到 /workspace，容器退出即销毁，宿主机上的 SSH 密钥、环境文件等不受污染。提供 26 种预配置运行时（编程语言、Linux 发行版、安全工具、AI coding agent），支持通过 .airlock 文件配置运行时、端口、环境变量与安装命令，也可创建跨会话保留的持久 devbox。支持 Linux、macOS 和 WSL2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 26 种预配置运行时，含 AI coding agents 与安全工具
- 一次性容器默认退出即删，工作目录实时挂载到 /workspace
- 无根 Podman、自动 SELinux 重标记与进程限制
- 单 Bash 脚本实现，无框架或第三方运行时依赖

## 适用场景

- 在隔离沙箱中运行不信任的项目脚本和构建
- 需要保留环境的跨会话持久开发容器
- 避免在宿主机安装各语言 SDK 与扫描工具

## 场景标签

 · 领域:开发工具/容器沙箱

## 证据(README 行号)

> L14: Airlock puts your project inside a preconfigured rootless Podman container. Your working directory stays available 
> L47: - **26 preconfigured runtimes** across programming languages, Linux distributions, security tools, and AI coding ag

## 星数曲线

```mermaid
xychart-beta
    title "besoeasy/airlock 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-30 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b3d3248ea85f` · [字段定义](../../DATASET.md)*
