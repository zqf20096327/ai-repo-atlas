# olegpustovit/agentpack

⭐ 16 · Go · MIT · 推送 2026-10-29 · [GitHub](https://github.com/olegpustovit/agentpack) · [官网](https://olegpustovit.github.io/agentpack) · 个人维护

**为编程 agent 固定 skills 与插件版本的项目清单/锁文件工具**

面向使用 Claude Code、Cursor、OpenCode、Codex、Grok、Antigravity 等编程 agent 的开发者：用项目级 manifest（agentpack.toml）声明 skills 与插件依赖，解析包后在锁文件（pack.lock）中记录 commit 与内容哈希，并按各 agent 适配方式将产物 staged 到项目。提供各 agent 的启动器命令转发参数；校验依赖哈希缓存，哈希不判定内容安全性。以 Go 编写，提供 GitHub releases 二进制（macOS/Linux/Windows）、Homebrew 与源码构建方式，当前为 pre-release，行为与锁文件格式可能变化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 项目 manifest + 锁文件记录 commit 与内容哈希
- 支持 Claude Code、Cursor、OpenCode、Codex、Grok、Antigravity 六种 agent 的 staging 与启动器
- 哈希缓存校验与 AGENTPACK_FULL_VERIFY / REQUIRE_VERIFIED 开关
- MCP 依赖固定（限支持的 npx 场景）

## 适用场景

- 在项目中固定团队共享的 agent skills 与插件版本
- 为多个编程 agent 统一安装和启动同一组依赖
- 校验 staged 产物与锁文件记录一致

## 场景标签

 · 领域:开发者工具/agent 生态

## 证据(README 行号)

> L3: Pin skills and plugins for coding agents in one project manifest. Agentpack resolves packages, records commits and c
> L43: |Command|Agent|

## 星数曲线

```mermaid
xychart-beta
    title "olegpustovit/agentpack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `386917b68311` · [字段定义](../../DATASET.md)*
