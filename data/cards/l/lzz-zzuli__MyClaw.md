# lzz-zzuli/MyClaw

⭐ 21 · Python · NOASSERTION · 推送 2026-08-10 · [GitHub](https://github.com/lzz-zzuli/MyClaw) · 个人维护 · 中文 README

**本地透明可控的 AI Agent 终端框架：状态机+沙箱+审计**

基于 LangGraph 的本地命令行智能体框架，用状态机组织模型决策与工具调用。面向关注 Agent 可靠性与安全边界的开发者：提供 6 类 JSONL 审计事件、重复工具检测与迭代阈值中断、三层记忆（用户画像/对话摘要/知识库）、workspace 目录沙箱与路径/环境变量/危险命令防御，以及 SKILL.md 技能扩展与离线评测（Scripted Model + Mock Tool，无需 API Key）。支持 OpenAI、Anthropic、Ollama 等多种模型接口；沙箱非操作系统级强隔离。Python 3.10+，git clone 或 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph 状态机组织推理与工具调用，失控循环可中断并人工续接
- 6 类 JSONL 审计事件与 trace/monitor/eval CLI 可观测能力
- 文件与 Shell 工具限定在 workspace/office/，含路径校验、环境变量白名单、危险命令拦截与超时
- 三层记忆与关键词+Embedding 混合检索，未配置时自动降级

## 适用场景

- 搭建有长期记忆的个人助手，记住偏好与项目知识
- 在受控目录内让 Agent 执行文件整理与 Shell 任务
- 复盘与审计 Agent 每一步的决策和工具调用

## 场景标签

`Agent 框架` `Agent 记忆` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L20: 它是一个基于 LangGraph 的本地智能体框架，用状态机组织推理和工具调用，用安全沙盒限制执行范围，并把关键行为写入审计日志。当 Agent 陷入循环时，MyClaw 会主动中断并把决定权交还给你。
> L134: MyClaw 用 LangGraph 把模型决策、工具执行和中断续接组织成可观察的状态机：

## 星数曲线

```mermaid
xychart-beta
    title "lzz-zzuli/MyClaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9a1a38a9c81e` · [字段定义](../../DATASET.md)*
