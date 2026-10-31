# lee-to/ai-tester

⭐ 25 · Rust · MIT · 推送 2026-10-07 · [GitHub](https://github.com/lee-to/ai-tester) · 个人维护

**面向 agent 技能与系统提示的端到端行为测试 CLI**

Rust 编写的测试工具：在一次性 git 沙箱中运行真实 agent 场景，录制规范化的工具调用轨迹，并用声明式 YAML 断言（tool_called、tool_call_sequence、no_path_escape 等）评估行为。内置 Claude Code、OpenAI Codex CLI 适配器及通用 ACP agent 通道；支持技能、内联 system prompt、外部提示文件三种测试对象，提供 fixtures、JSON/Markdown 报告、确定性 0..100 评分的 benchmark 与自更新命令。沙箱仅为临时工作区隔离，非 OS 沙箱或网络边界。通过 cargo install 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每场景创建一次性 git 沙箱并录制完整工具调用轨迹
- 声明式 YAML 断言：tool_called / tool_call_sequence / no_path_escape / turn_count_at_most 等
- 多 runtime 适配：Claude Code、OpenAI Codex CLI、ACP agent
- benchmark 子命令计算确定性 0..100 评分，含效率因子与安全断言惩罚

## 适用场景

- 为 Claude 技能（SKILL.md）编写回归测试并接入 CI
- 验证裸系统提示在真实工具调用序列下的行为
- 跨 runtime（Claude/Codex/ACP）跑同一场景对比表现
- 检测 agent 是否出现路径逃逸、联网或破坏性命令等违规行为

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: > End-to-end behavioral testing for **skills**, **bare system prompts**, and agent runtimes. Run real scenarios in a
> L13: `ai-tester` creates a throwaway sandbox per scenario, runs the selected runtime, records every normalized turn and 
> L25: - **Multi-runtime.** Built-in adapters for Claude Code and OpenAI Codex through their installed CLIs, plus generic 

## 星数曲线

```mermaid
xychart-beta
    title "lee-to/ai-tester 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5cb7732a4f10` · [字段定义](../../DATASET.md)*
