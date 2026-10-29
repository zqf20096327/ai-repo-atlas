# zxzvsdcj/spec-first-superpowers

⭐ 19 · Python · 推送 2026-04-17 · [GitHub](https://github.com/zxzvsdcj/spec-first-superpowers) · 个人维护

**Cursor Agent 技能：强制 AI 先写规范再写代码的工作流**

一个 Cursor Agent Skill（npx skills add 安装），用于约束 AI 编程遵循 spec-before-code 流程：模式选择、复杂度分级、会话恢复、规范编写（G1）、持久化规划（G2）、UI/UX 设计（G3）与 TDD 实现（G4）四个质量门。集成 Spec-Kit、OpenSpec、Superpowers、planning-with-files、ui-ux-pro-max 等项目，可选接入 MemPalace 做跨会话记忆与知识图谱。通过 /super-spec 命令在 Cursor 对话中调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四个质量门（G1-G4）：规范、规划、设计、TDD 实现
- v5 用内联自查清单替代子代理评审循环（约 30 秒）
- 可选 MemPalace 跨会话记忆与知识图谱集成
- 支持 Spec-Kit / OpenSpec 双模式与复杂度分级

## 适用场景

- 在 Cursor 中约束 AI 先产出规范再进入实现
- 跨会话恢复 AI 开发上下文与决策记录
- 以 TDD 流程执行 AI 编码任务

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: A Cursor Agent Skill that enforces spec-before-code workflow. Prevents the AI from skipping design and jumping strai
> L33: - `using-superpowers` + sub-skills (brainstorming, writing-plans, TDD, code-review, etc.)
> L121: |Spec-Kit|github/spec-kit|v0.7.1|GitHub's spec-driven framework (uv tool install)|

## 星数曲线

```mermaid
xychart-beta
    title "zxzvsdcj/spec-first-superpowers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `54d2f98453ee` · [字段定义](../../DATASET.md)*
