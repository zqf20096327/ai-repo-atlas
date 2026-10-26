# TOKTOKHAN-DEV/agent-company

⭐ 85 · HTML · MIT · 推送 2026-08-27 · [GitHub](https://github.com/TOKTOKHAN-DEV/agent-company) · [官网](https://www.agent-company.site) · 组织维护

**让 AI 编码代理团队像公司一样协作的 monorepo 模板**

由 TOKTOKHAN-DEV 维护的 pnpm+Turborepo monorepo 模板，面向使用 Claude Code、Codex、Cursor 等编码代理的开发者。核心机制：会话启动钩子自动注入硬规则、wiki 索引与两级记忆（短期→长期→wiki）；agents/registry.yaml 为每个代理声明运行时、模型与写入范围；出稿走确定性门禁（不含模型调用），代理只能到 in_review，出稿按钮由人按下；图像生成限定单一 Codex 路径并强制记录出处。内置 blog、blank、app-in-toss 三种模板，另含外部资产 intake 命令。限制：面向编码代理工作流，模板数量目前为三个。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SessionStart 钩子自动注入上下文与硬规则，两级记忆跨会话留存
- 每个代理独立进程运行，registry.yaml 声明运行时/模型/写入范围
- 出稿门禁为确定性函数（无 LLM 调用），出稿按钮仅人可按
- 单一图像生成路径 + 三层强制（类型/钩子/审计）记录资产出处

## 适用场景

- 用多个编码代理分工维护博客或迷你应用并做人审出稿
- 让代理团队保留跨会话的组织记忆与决策历史
- 接手半成品项目时用 intake 生成目录清单供代理按需读取

## 场景标签

`编码 Agent` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L13: > AI 팀이 굴리는 모노레포 템플릿.
> L39: |역할 혼재|에이전트마다 런타임 · 모델 · 쓰기 범위를 선언|`agents/registry.yaml`|
> L180: 런처가 `agents/registry.yaml` 에서 런타임과 모델을 읽고, `AGENT.md` 와 스킬 인덱스(폴더 스캔으로

## 星数曲线

```mermaid
xychart-beta
    title "TOKTOKHAN-DEV/agent-company 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 84 --> 86
    line [85, 85]
```

2026-10-18 85 → 2026-10-26 85（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `84beed01458a` · [字段定义](../../DATASET.md)*
