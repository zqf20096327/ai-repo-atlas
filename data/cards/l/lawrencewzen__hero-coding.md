# lawrencewzen/hero-coding

⭐ 41 · Go · MIT · 推送 2026-10-11 · [GitHub](https://github.com/lawrencewzen/hero-coding) · 个人维护 · 中文 README

**极简自主编码 Agent 框架：投入需求文档，产出 git commit**

用 Go 编写的自主编码 agent 运行框架：监听 inbox/ 目录中的用户故事 Markdown 文件，为每个故事创建 git worktree，循环执行 Worker（ReAct 循环调用 OpenAI 兼容 Chat Completions 端点）、Verifier（运行故事声明的 shell 验证命令）、Reviewer（读取验证记录与 git diff 给出裁决）直至通过或重试耗尽，输出为通过审查的 git 分支。Plan 阶段设计上留在框架之外，由上游交互式编码 agent 会话产出故事文件。配置通过 YAML 分层完成，Worker 与 Reviewer 可指向不同提供商与模型。需从源码用 go build 编译运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- inbox/ 投入用户故事 → Worker→Verifier→Reviewer 循环 → git commit 分支产出
- 验证失败短路跳过 Reviewer LLM 调用，确定性测试退出码作为证据
- 护栏机制：工具调用上限、时间上限、循环检测、自动补提交
- Worker 与 Reviewer 可分别配置不同的 LLM 提供商与模型
- hero plan 可将高层计划拆解为带依赖关系的 DAG 故事并按序执行

## 适用场景

- 把写好验收标准的故事文件投入队列，让 agent 长时间自主完成编码并自动验证
- 让廉价模型执行、强模型评审以控制成本
- 用分层验证命令（构建/测试分级）自动把关代码改动

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: A minimal harness for autonomous coding agents. Drop a user story in `inbox/`, get git commits out.
> L53: A native ReAct loop driving an OpenAI-compatible Chat Completions endpoint. Tools (bash, read_file, write_file, edi
> L78: Reads the user story, the Verifier record, and `git log` + `git diff` since the base ref. Calls an OpenAI-compatibl

## 星数曲线

```mermaid
xychart-beta
    title "lawrencewzen/hero-coding 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-26 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ba440c3ab776` · [字段定义](../../DATASET.md)*
