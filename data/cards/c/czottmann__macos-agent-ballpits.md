# czottmann/macos-agent-ballpits

⭐ 20 · Shell · 推送 2026-06-02 · [GitHub](https://github.com/czottmann/macos-agent-ballpits) · 个人维护

**macOS 上沙箱化运行 Claude Code 等 agent 的示例配置集**

个人 showcase（作者自称非完整项目）：提供两种在 macOS 上限制 LLM agent 文件写入权限的方案——基于 OrbStack Docker 容器的 claude-containered（启动约 1-2s，隔离更强）与基于 macOS 原生 sandbox-exec 的 claude-sandboxed（即时启动，原生性能）。机制上 MCP 服务器经 supergateway 运行在宿主机，agent 在沙箱内通过 HTTP/SSE 连接，从而可在沙箱内构建 Xcode 项目。以 fish 脚本形式提供，依赖 jq、gum、npx 等工具，脚本有文档说明，作者声明不保证安全强度。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 两种方案：OrbStack 容器隔离与 macOS sandbox-exec 原生沙箱
- MCP 服务器跑在宿主机、agent 在沙箱内经 HTTP/SSE 连接，规避嵌套沙箱问题
- 沙箱内 agent 可构建 Xcode 项目，无需整套 macOS VM
- 提供 --init-mcp 生成项目级 MCP 配置

## 适用场景

- 在 macOS 上限制 Claude Code 等 agent 的文件写入范围
- 需要 agent 在沙箱内构建 Xcode 项目又保留 MCP 工具能力
- 参考脚本搭建自己的 agent 沙箱方案

## 场景标签

 · 领域:开发者工具/agent 安全

## 证据(README 行号)

> L5: This is my personal take on sandboxing Claude Code and similar AI agents.
> L31: 1. **MCP servers run on the host** (outside the sandbox) via supergateway
> L32: 2. **Claude runs inside the sandbox** with restricted write access

## 星数曲线

```mermaid
xychart-beta
    title "czottmann/macos-agent-ballpits 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `739cb59c4cad` · [字段定义](../../DATASET.md)*
