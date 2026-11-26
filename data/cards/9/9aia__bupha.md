# 9aia/bupha

⭐ 3 · Rust · MIT · 推送 2026-11-25 · [GitHub](https://github.com/9aia/bupha) · [官网](https://9aia.com/bupha) · 个人维护

**为 agent 仓库提供 push-to-verdict CI 流水线的 tamias 集成组件**

bupha 不是独立产品，而是 tamias 的 CI 集成（type: bupha），以 tamias bundle 形式分发。它提供一条 push-to-verdict 流水线：webhook 等来源接收 push/PR，经签名校验与去重进入队列，按 sha 在 detached worktree 中运行，runner 支持 shell/dagger/gha/ssh/container/http 等方言，运行结果写回 forge 的 commit status。另提供 `uses: 9aia/bupha` 的 composite GitHub Action 用于轮询或读取状态。当前为 pre-1.0，仅支持 Linux + systemd，单机串行执行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- pluggable sources 接收 push/PR，按 sha 在 detached worktree 中运行
- 多种 runner：shell/script、dagger、ssh、container、gha、http
- 运行结果经 lasius-forge 端口写回 forge commit status
- 提供 composite GitHub Action，支持 wait/status 两种模式

## 适用场景

- 在本机为 agent 驱动的仓库执行 push 触发的 CI 流水线
- 在 GitHub Actions 工作流中等待/读取 CI 判定状态
- secrets 不离开本机的自托管 CI 场景

## 场景标签

 · 领域:开发者工具/CI

## 证据(README 行号)

> L6: **bupha is not a standalone product — tamias is.** bupha is the
> L16: Headless CI for agent-driven setups — pre-1.0, Linux + systemd. A


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `5c0097cb9092` · [字段定义](../../DATASET.md)*
