# sublang-ai/slc

⭐ 41 · TypeScript · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/sublang-ai/slc) · 组织维护 · 中文 README

**自然语言到状态机的编译器：一段散文生成可运行多 agent 程序**

SubLang Compiler（slc）把一段英文或中文散文描述的工作流编译为 GEARS spec 条目、XState 状态机与可由 playbook CLI 运行的注册条目，驱动 AI 编码 agent 按角色执行。编译与执行通过用户已安装的 agent CLI（Claude Code、Codex、Gemini、OpenCode）进行，可按角色选择并可选第二 agent 审查每个编译步骤；无需判断的步骤在编译期改写为纯 shell 命令。要求 POSIX 平台、Node.js >= 23.6 与至少一个受支持的编码 agent CLI。以 npm 全局安装提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 散文 → GEARS 条目 → XState 状态机 → 可运行 playbook 的多阶段编译管线
- 通过 Claude Code / Codex / Gemini / OpenCode 等 agent CLI 编译与执行，可按角色选择
- 无需判断的步骤编译期改写为纯 shell 命令，不调用 LLM
- 每个中间产物为可读可编辑文件，附带绑定回 spec 的验证测试；支持增量重编译与双 agent 审查编译

## 适用场景

- 用一段自然语言描述工作流并生成可检查、可验证的多 agent 程序
- 让编码与审查 agent 在状态机约束下协作完成任务（如代码评审循环）
- 审计多 agent 工作流的控制流：谁执行、什么顺序、何时停止

## 场景标签

`多智能体` `工作流自动化` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L7: _The SubLang Compiler: describe a workflow in a paragraph of prose, get a
> L11: orchestration framework. `slc` compiles that paragraph into a spec, a
> L12: state machine, and a runnable **playbook** that drives AI coding agents

## 星数曲线

```mermaid
xychart-beta
    title "sublang-ai/slc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-28 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0ea284a63012` · [字段定义](../../DATASET.md)*
