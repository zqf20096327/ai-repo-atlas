# YanKaFei/ascii-h3-director

⭐ — · [GitHub]() · 个人维护 · 中文 README

**为 MiniMax H3 视频生成提供 ASCII 动态排版导演与确定性预览工具**

面向 MiniMax H3 视频模型的导演工具：将自由简报编译为 transformation chain 与面向时间的提示词，内置 7 项自动化检查的质量门（无 PASS 不进入付费生成）。同时提供零依赖的确定性 ASCII 渲染引擎（5×9 位图字体，可复现输出终端帧、SVG、PNG 与 contact sheet），支持 exit_state→entry_state 的续接契约与 checkSeam 接缝校验。以 DSH Cordis 插件和通用 Agent Skill 两种形态分发，CLI 提供 13 个子命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 简报→transformation chain 编译 + 7 项检查的质量门（付费生成前拦截）
- 确定性 ASCII 渲染引擎：5×9 位图字体、seeded、SHA-256 可复现
- 21 机制动效语法库与 FORM_SUCCESSORS 合法性表
- 续接契约：exit_state→entry_state + checkSeam 接缝违规报告

## 适用场景

- 在为 H3 付费生成前先用无 API key 的预览确认画面
- 制作需要跨片段无缝续接的 ASCII 动态排版短片
- 为编码类 Agent（读 SKILL.md）配置视频导演技能

## 场景标签

`视频生成` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L18: ASCII H3 Director is a directing tool for MiniMax H3. It compiles a free-form brief into a **transformation chain**
> L63: The installer copies `skill/` to `~/.agents/skills/ascii-h3-director/` and prints the self-check command. The two p
> L206: - **Node 18+** (`doctor` checks the major version explicitly)

## 星数曲线

```mermaid
xychart-beta
    title "YanKaFei/ascii-h3-director 星数(近 3 点)"
    x-axis ["2026-10-20", "2026-11-18", "2026-11-22"]
    y-axis "stars" 4 --> 7
    line [5, 6, 6]
```

2026-10-20 5 → 2026-11-22 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `da8e3c3596f0` · [字段定义](../../DATASET.md)*
