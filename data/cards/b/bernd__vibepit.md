# bernd/vibepit

⭐ 23 · Go · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/bernd/vibepit) · [官网](https://vibepit.dev) · 个人维护

**在隔离容器中运行 AI 编程代理并做网络过滤的 CLI 工具**

面向使用 AI 编程代理的开发者的沙箱 CLI 工具：以只读根文件系统与削减 capabilities 的容器启动开发环境，经 DNS/HTTP(S) 过滤代理以域名白名单控制代理可访问的网络范围；内置针对 GitHub、Anthropic、包管理器等常见服务的网络预设，可通过 CLI 命令或交互式 TUI 监视器在运行中管理白名单，支持 Docker 与 Podman，home 卷跨会话持久化。需 Linux 或 macOS。README 明确声明容器隔离弱于 VM 隔离，不应视为硬安全边界。以 curl 脚本下载二进制安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 只读根文件系统与 dropped capabilities 的容器隔离
- DNS/HTTP(S) 过滤代理与域名白名单
- 常见服务网络预设与运行中白名单管理（CLI/TUI 监视器）
- 支持 Docker 与 Podman，home 卷跨会话持久化

## 适用场景

- 在受控网络环境下运行 AI 编程代理
- 限制代理只能访问指定域名或服务预设
- 通过 SSH 以守护进程模式连接沙箱会话并实时查看代理日志

## 场景标签

 · 领域:开发者工具/沙箱安全

## 证据(README 行号)

> L3: Run AI coding agents in isolated containers with network filtering.
> L15: - Isolated containers with read-only root filesystem and dropped capabilities
> L16: - DNS and HTTP/HTTPS filtering proxy with domain allowlist

## 星数曲线

```mermaid
xychart-beta
    title "bernd/vibepit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `92ec36886450` · [字段定义](../../DATASET.md)*
