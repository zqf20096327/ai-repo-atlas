# VirtusLab/sandcat

⭐ 199 · Shell · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/VirtusLab/sandcat) · 组织维护

**安全运行 AI 编码 agent 的 Docker 沙箱容器方案**

面向在 `--dangerous` 等高风险模式下运行 AI 编码 agent（Claude Code、Cursor CLI、Codex CLI、GitHub Copilot CLI）的开发者：以 Docker/dev container 构建沙箱环境，全部容器流量经 WireGuard 透明路由到 mitmproxy，按 allow/deny 列表规则放行 HTTP/S 与 DNS 查询、丢弃无法匹配主机名的原始 TCP/UDP；凭据在代理层注入做密钥替换，容器内不接触真实值。提供 CLI 安装脚本，需 docker compose 与 yq，可作为 devcontainer 或独立 shell 使用。

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

- 透明 mitmproxy + WireGuard 路由全部容器流量，无需逐工具配代理
- allow/deny 列表控制 HTTP/S 与 DNS，其余 TCP/UDP 一律丢弃
- 代理层密钥替换，容器内不可见真实凭据
- 提供 1Password 与 Proton Pass 两种 mitmproxy 镜像变体

## 适用场景

- 在隔离沙箱中运行具备较高权限的 AI 编码 agent
- 限制 AI agent 的网络访问范围并审计其请求
- 在容器内注入凭据而不暴露真实密钥值
- 在 VS Code devcontainer 中保留 IDE 便利的同时做安全隔离

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: Sandcat is a Docker & dev container setup for securely
> L4: running AI agents (Claude Code, Cursor CLI, Codex CLI, GitHub Copilot CLI). The
> L9: All container traffic is routed through a transparent

## 星数曲线

```mermaid
xychart-beta
    title "VirtusLab/sandcat 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 195 --> 200
    line [196, 198, 199]
```

2026-10-18 196 → 2026-10-22 199（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `83cffc20f672` · [字段定义](../../DATASET.md)*
