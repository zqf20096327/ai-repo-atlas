# ai-outfitter/outfitter

⭐ 19 · TypeScript · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/ai-outfitter/outfitter) · 组织维护

**编码 agent 的配置管理工具链：像 dotfiles 一样切换 agent 配置**

围绕 .agents/ 目录的配置工具链：从本地与远程 .agents 树解析配置，按 slug 组合 agent、技能与知识，并通过 pi、Claude Code、Codex CLI 等封装的 agent CLI 启动。.agents/ 目录本身为配置源，不依赖特定格式，可像代码一样提交与审查；配置分层合并（项目层覆盖用户层覆盖 pinned 远程目录），按 SHA 固定。支持在桌面、GitHub Actions、CI 定时与 Kubernetes 集群中运行同一套组合。要求 Node 22.19 及以上，Pi 内置。企业目录代码 (code/enterprise/) 采用单独商业许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从本地/远程 .agents 树按 slug 组合 agent、技能、知识与 MCP 配置
- 分层合并：项目 .agents/ 覆盖 ~/.agents/ 覆盖 pinned 远程目录，按 SHA 固定
- 通过封装 CLI 启动 pi、Claude Code、Codex CLI 等运行时
- 同一组合可运行于桌面、GitHub Actions、CI cron 与 Kubernetes

## 适用场景

- 团队共享统一的 agent 技能目录并通过 pull request 审查变更
- 在 CI 与集群中以与本地相同的 agent 配置运行自动化任务
- 个人与组织配置分层共存，按需覆盖而非复制

## 场景标签

 · 领域:开发者工具/agent 基础设施

## 证据(README 行号)

> L7: Outfitter is the toolchain for `.agents`: it resolves agent configuration from local and remote `.agents` trees, com
> L43: Pi is bundled and also hosts Outfitter's setup walkthrough. Install other runtime harnesses, such as

## 星数曲线

```mermaid
xychart-beta
    title "ai-outfitter/outfitter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c5b58e7c7f19` · [字段定义](../../DATASET.md)*
