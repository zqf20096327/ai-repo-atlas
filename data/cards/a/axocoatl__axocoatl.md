# axocoatl/axocoatl

⭐ 72 · Rust · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/axocoatl/axocoatl) · [官网](https://axocoatl.ai) · 个人维护

**无人值守运行编程 agent 并出具签名回执的 CI 工具**

用 Rust 编写的单一可执行文件，用于在沙箱中无人值守地运行编程 agent（Claude Code、Codex 或本地模型）。运行以 YAML loadout 定义 writer、检查与 reviewer；沙箱为 rootless Podman 容器、无直接网络、经守护进程的出口代理按路由放行。主机在最终文件上执行用户指定的测试命令，另一个模型审查变更，产出 CI 退出码、SHA-256 校验的记录与 Ed25519 签名的 in-toto 回执，可验证、可保留为分支或 PR。内置 fix/qa/audit 等 loadout，支持本地 Ollama 模型或 OpenRouter。限制：本地审查模型需较大内存，Ubuntu 22.04 及更早版本被拒绝安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Podman 沙箱隔离：无直接网络、非 root 用户、出口代理逐连接记录并拦截越权模型调用
- 主机在最终文件上运行用户检查命令，另一模型审查，产出 CI 退出码与 JUnit/JSON Lines 记录
- 每次运行产出 Ed25519 签名的 in-toto/DSSE 回执，可离线验证并与 checkout 比对
- 五个内置 loadout（fix/fix-claude-code/fix-codex/qa/audit），可用 YAML 自定义

## 适用场景

- 在 CI 中无人值守运行编程 agent 修 bug，由测试与审查模型把关
- 让本地小模型编写代码、更强模型审查，全程本地运行
- 需要可验证的变更回执与完整审计记录的自动化代码维护
- 把 agent 产物保留为分支或 PR 并附签名回执

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L6: Claude Code, Codex or a local model works in a sandbox its model credential never
> L83: the budgets and the prompt. `axocoatl run` hands one to the running daemon, which runs
> L106: - **A verdict for CI.** Exit codes: 0 pass, 1 checks failed, 2 needs attention, 3 usage,

## 星数曲线

```mermaid
xychart-beta
    title "axocoatl/axocoatl 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 70 --> 73
    line [71, 72, 72]
```

2026-10-18 71 → 2026-10-30 72（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `fb10ddd2d643` · [字段定义](../../DATASET.md)*
