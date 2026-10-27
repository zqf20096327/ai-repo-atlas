# z3z1ma/10x

⭐ 23 · Python · MIT · 推送 2026-07-10 · [GitHub](https://github.com/z3z1ma/10x) · 个人维护

**面向 AI 编程代理的 Markdown 指令集：让代理澄清、记忆、验证与改进**

单文件 SKILL.md 形式的指令集，可加载到 Codex、OpenCode、Claude Code、Cursor、Gemini CLI 等 70+ 代理框架。它规定代理的工作方法：编码前质疑模糊需求、将仓库级上下文保存到 .10x/ 目录（决策/研究/工单/技能记录，纯 Markdown、git 版本化）、分离理解与执行两个循环、以证据验收变更、收尾时复盘沉淀知识。安装通过 npx skills add 或复制粘贴/git clone；无运行时、无服务、无数据库。作者声明指令约 5,400 词，代理会消耗 token 做审议与记录。

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

- 单文件 SKILL.md，兼容 Codex/Claude Code/Cursor/Gemini CLI/OpenCode 等 70+ 框架
- 在 .10x/ 目录沉淀决策、研究、工单、证据等可 grep 的工程上下文
- 外循环（澄清/规约/记录）与内循环（受限工单执行/证据验收）分离
- 附 autoresearch/ 实验装置：用 LLM 研究者+受试代理试验对候选指令做回归评估

## 适用场景

- 让 AI 编程代理跨会话保留决策与教训，避免重复解释
- 要求代理以证据而非主观判断验收变更
- 为模糊的新建项目工作流建立轻量的先澄清后执行流程

## 场景标签

 · 领域:AI 编程代理/开发工具

## 证据(README 行号)

> L15: It is one self-contained file: `SKILL.md`. Load it into Codex,
> L16: OpenCode, Claude Code, Cursor, Gemini CLI, or any harness that reads project

## 星数曲线

```mermaid
xychart-beta
    title "z3z1ma/10x 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 24
    line [22, 23]
```

2026-10-18 22 → 2026-10-27 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `eaf9a798552e` · [字段定义](../../DATASET.md)*
