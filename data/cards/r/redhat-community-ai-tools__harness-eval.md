# redhat-community-ai-tools/harness-eval

⭐ 32 · Python · Apache-2.0 · 推送 2026-10-10 · [GitHub](https://github.com/redhat-community-ai-tools/harness-eval) · 组织维护

**对 AI 编程 agent 配置做确定性检查（lint/安全/门禁）的工具**

面向使用 AI 编程 agent 的仓库与 CI 流程：自动探测仓库使用的 agent 工具（Claude Code、Cursor、Copilot、Gemini CLI、Codex、OpenCode、Windsurf、Cline、fullsend），读取指令文件、skills、commands、hooks、MCP 配置等，构建统一组件图并运行 92 条确定性规则。提供四个主命令：harness-autonomy（输出 PASS/FAIL/REVIEW_REQUIRED 三态合并决策证据）、harness-gate、harness-security、harness-lint。默认离线、无 LLM、无网络调用，每次运行结果相同；OSV 查询与 LLM 评审为可选。通过 pip 安装，另提供 GitHub Action、pre-commit hook 等形式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨 9 种 agent 工具自动探测配置并构建统一组件图，规则可跨文件检查
- 92 条确定性规则，按 effect（block/policy/signal/advice）与 tier（gating/provisional/advisory）组织
- harness-autonomy 输出三态判决与 JSON/SARIF 证据（coverage、指纹、摘要），供自动合并策略使用
- 默认离线运行，不执行被扫描树中的任何内容，附威胁模型文档

## 适用场景

- 在 CI 中对 agent 配置变更做合并前的确定性检查
- 安全审查 agent 配置中的权限放宽、密钥提交与污点路径
- 为 ADLC（agent 驱动开发流程）提供可审计的配置健康证据
- 对 CLAUDE.md、skills、hooks、MCP 配置做质量 lint

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L9: Deterministic checks for the configuration that AI coding agents run with:
> L13: builds one component graph across them, and runs 92 deterministic rules

## 星数曲线

```mermaid
xychart-beta
    title "redhat-community-ai-tools/harness-eval 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-25 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `35e015474e43` · [字段定义](../../DATASET.md)*
