# automagik-dev/genie

⭐ 345 · TypeScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/automagik-dev/genie) · [官网](https://docs.automagik.dev/genie) · 组织维护

**给开发者的编码 agent 工作流 CLI：一个任务进，一个 PR 出**

运行在 Claude Code、Codex 等编码 agent 之上的技能与工作流框架：以 /wish 接收一个已决定的任务，在独立 worktree 中执行，运行仓库自身检查，由未编写代码的 agent 审查提交，最后开启 pull request，合并权留给用户。更大规模的工作经 brainstorm→设计审查→wish→计划审查→work→实现审查的完整循环，设计、计划与裁定以 markdown 存入 git，任务状态存于每仓库一个 SQLite 文件。以签名二进制安装（Linux/macOS，Windows 不支持，WSL2 可用但未在测试矩阵）。README 说明了适用边界：小改动用 Genie 反而更慢（示例任务耗时 19.9 分钟、387,079 tokens），弱检查与不可信仓库不适用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- brainstorm/wish/work/review/council/fix 六个技能构成的完整循环，每道关口由未做该工作的独立 agent 审查
- 18 个技能 + 12 个保存工作流，技能安装到检测到的各 agent 技能目录
- 设计与计划以 markdown 落盘 git，任务状态存单 SQLite 文件，genie board 呈现看板
- 发布经 cosign 签名附 SLSA provenance，genie update 离线验证

## 适用场景

- 把一个已决定的任务交给 agent 端到端完成并产出待合并的 PR
- 较大功能走 brainstorm→设计审查→计划审查→分组执行→实现审查的流程
- 用独立审查 agent 在合并前核对代码是否满足计划标准

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: Give `/wish` one decided task. It checks that the task fits, builds it in its own worktree, runs your repository's o
> L14: Claude Code runs it as `/wish`, Codex as `$wish`, and other agents by name. Docs · Skills · Discord
> L106: |Genie|skills and saved workflows that keep plans in git, plus a CLI that keeps task state in one SQLite file|brai

## 星数曲线

```mermaid
xychart-beta
    title "automagik-dev/genie 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 344 --> 346
    line [345, 345]
```

2026-10-18 345 → 2026-10-26 345（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `693f1682e444` · [字段定义](../../DATASET.md)*
