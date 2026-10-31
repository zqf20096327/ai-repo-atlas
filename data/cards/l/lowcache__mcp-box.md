# lowcache/mcp-box

⭐ 15 · Go · MIT · 推送 2026-08-29 · [GitHub](https://github.com/lowcache/mcp-box) · 个人维护

**用 Docker 沙箱隔离运行 MCP server 的 Go CLI 工具**

单一 Go 二进制，为 Model Context Protocol 服务器提供严格隔离的 Linux 容器沙箱：只读根文件系统、tmpfs 临时状态、drop 全部 Linux capabilities、no-new-privileges、默认无网络、按 profile 的网络策略、显式挂载的工作区、宿主 UID/GID 映射。预置 sqlite/shell/filesystem/fetch 四种沙箱，提供 run/ps/inspect/logs/config 等 CLI 命令，可生成粘贴即用的 Claude Desktop/Claude Code 配置。硬依赖仅为 Docker；Nix 可选，缺省时从 GHCR 拉取固定镜像；也可用 Nix flake 或 Go 1.22+ 从源码构建。部分平台特性（policy profiles、compose 规格、append-only 审计日志）标注为 planned。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个 MCP server 独立 Docker 沙箱：只读根、cap-drop=ALL、默认无网络
- 宿主 UID/GID 映射，挂载工作区文件归属当前用户
- mcp-box config 生成可直接粘贴进 claude_desktop_config.json 的 JSON
- 无 Nix 时自动从 GHCR 拉取固定摘要的预构建 OCI 镜像

## 适用场景

- 让 AI agent 的 MCP 工具执行无法触及宿主 home、SSH 密钥与云凭据
- 为 sqlite/shell/filesystem/fetch 等服务器快速起隔离沙箱
- 通过 inspect/logs 审计沙箱规格与运行事件

## 场景标签

 · 领域:AI 工具链/容器安全

## 证据(README 行号)

> L11: `mcp-box` puts every MCP server inside a locked-down Docker sandbox with a read-only root filesystem, explicit writ
> L16: **mcp-box** is a single, portable **Go** binary that launches turnkey, immutable, strictly-isolated
> L117:  - **Docker Engine** (Must be active and running locally on the host system).

## 星数曲线

```mermaid
xychart-beta
    title "lowcache/mcp-box 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `84fae23334fd` · [字段定义](../../DATASET.md)*
