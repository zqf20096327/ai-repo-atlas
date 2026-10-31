# shamilkayal/ultragoal

⭐ 17 · JavaScript · MIT · 推送 2026-08-03 · [GitHub](https://github.com/shamilkayal/ultragoal) · [官网](https://www.npmjs.com/package/ultragoal) · 个人维护

**Claude Code/Codex 的目标循环插件：目标编译为可验证清单并自动守护**

面向 Claude Code 与 Codex 的 agent 循环管理插件（npm 安装）：将用户口述的意图经访谈编译为每行可由命令核验的 rubric，武装一个由独立验证子代理把关的循环——验证者未见工作过程、重跑检查并尝试证伪，通过门控阻止 agent 未达标即停。目标存于文件，跨 /clear 与重启续跑；每轮结束将经验以带溯源标签的形式存入仓库、经 git 共享给团队。提供 17 个 rubric 模板、invariants 长效复查、多目标 program 链及 headless/定时运行模式。机制依据引用 Anthropic/DeepSeek 等公开研究，README 自述验证边界为 prompt 层而非沙箱。

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

- 口述意图→访谈→命令可核验 rubric 的目标编译流程
- 独立 fresh-eyes 验证子代理与未达标禁停的门控
- 目标文件化：跨 /clear/重启/多会话续跑，每人独立门控
- 带溯源标签、经 git 团队共享的累积记忆与 invariants 复查

## 适用场景

- 让 agent 无人值守跑通宵构建或迁移，直到独立验证确认完成
- 把 p95 延迟、包体积等数值指标设为目标做爬山式优化
- 周期性任务（依赖升级、flake 测试排查）复用累积记忆越跑越省
- 不读代码也能依据验证日志与证据台账信任并接手 agent 工作

## 场景标签

`编码 Agent` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L11: **ultragoal is that loop, packaged — so a system, not you, does the verifying, remembering, and stopping.** You ram
> L54: An interactive installer walks you through it: choose **Claude Code**, **Codex**, or **both**. Claude Code remains 
> L51: npx ultragoal

## 星数曲线

```mermaid
xychart-beta
    title "shamilkayal/ultragoal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `81ecd904f4ca` · [字段定义](../../DATASET.md)*
