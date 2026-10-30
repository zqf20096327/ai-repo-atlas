# stanislavkozlovski/dclaude

⭐ 15 · Python · 推送 2026-10-28 · [GitHub](https://github.com/stanislavkozlovski/dclaude) · 个人维护

**在 Docker 容器内全权限运行 Claude Code / Codex 的封装器**

由两个薄 Docker 封装脚本 dclaude 与 dcodex 组成：在目标仓库目录下运行时，将 Claude Code 或 OpenAI Codex CLI 启动到 Docker 容器内并 bind-mount 当前仓库，容器内改动实时反映到宿主机。面向希望给编码 agent 完全自主权限同时限制影响半径的开发者：可配置只读挂载目录（如 ~/Desktop）、路径与宿主机一致、认证与缓存跨运行持久化、SSH agent 转发按需启用且不复制私钥。容器预装 Python 与 Node，首次运行自动构建镜像（约 60 秒），并附带 macOS Docker 磁盘空间诊断与镜像保留策略。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- dclaude/dcodex 两条封装命令，容器内改动实时同步宿主机仓库
- 可配置只读挂载目录，容器无法写入
- 认证与缓存挂载自宿主机，跨运行持久化
- 默认不挂载 docker.sock、不提权、不复制 SSH 私钥；附带 Docker 磁盘空间管理与镜像保留策略

## 适用场景

- 让 Claude Code / Codex 在沙箱内全自主执行长命令链而无需逐条审批
- 限制编码 agent 的文件访问范围，降低全权限运行的安全风险
- 在容器内使用与宿主机一致的绝对路径引用文件
- macOS 上诊断并清理频繁构建累积的 Docker 镜像与缓存

## 场景标签

 · 领域:开发工具/AI agent 运行环境

## 证据(README 行号)

> L61: This repo ships two simple, thin Docker wrappers:
> L63: - `dclaude` - a wrapper on top of Claude Code
> L66: When ran from a folder, `dclaude` runs the coding CLI inside a docker container with the folder bind-mounted. Any c

## 星数曲线

```mermaid
xychart-beta
    title "stanislavkozlovski/dclaude 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5c7d6cec9686` · [字段定义](../../DATASET.md)*
